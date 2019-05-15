from modules.ssh import SSHsession
from time import sleep
from datetime import datetime
from botocore.exceptions import ClientError


class SmartpipeStandardModules:

    def __init__(self, config_file, **config):
        self.ssh = SSHsession(**config)
        self.current_date = datetime.now()
        self.config_file = config_file
        self.config_backup_file = f"{self.config_file}.bak"

    def run_ssh_command(self, cmd_string):
        cmd = self.ssh.runcmd(cmd_string)
        return cmd

    def backup_config(self):
        self.backup(self.config_file, self.config_backup_file)

    def backup(self, origin, destination):
        self.ssh.runcmd(f'sudo sh -c "cp {origin} {destination}"')

    def set_log_level(self, loglevel):
        self.ssh.runcmd(f'sudo sh -c "sed -i \'/log_level/c\log_level = '
                        f'{loglevel}\' {self.config_file}"')

    def update_config(self, param, config_value):
        if config_value == "empty":
            config = ""
        else:
            config = config_value

        command = 'sudo sh -c "sed -i'
        command = command + " '/" + param + "/c\\" + param + "= " + config + " \\' {0}\""
        command = command.format(self.config_file)
        self.ssh.runcmd(command)

    def start_service(self, processname, sleepSecs=2):
        if not self.confirm_process_is_running(processname):
            self.ssh.runcmd(f'sudo systemctl start {processname}')
            sleep(sleepSecs)

    def stop_service(self, processname, sleepSecs=2):
        if self.confirm_process_is_running(processname):
            self.ssh.runcmd(f'sudo systemctl stop {processname}')
            sleep(sleepSecs)

    def restart_service(self, processname, sleepSecs=2):
        self.ssh.runcmd(f'sudo systemctl restart {processname}')
        sleep(sleepSecs)

    def confirm_process_is_running(self, processname):
        log_lines = self.ssh.runcmd(f"sudo systemctl is-active {processname}")
        if log_lines[0] == "active":
            return True
        else:
            return False

    def restore_config(self):
        self.restore(self.config_backup_file, self.config_file)

    def restore(self, copy, original):
        self.ssh.runcmd(f'sudo sh -c "cp {copy} {original}"')
        self.ssh.runcmd(f'sudo sh -c "rm -f {copy}"')

    def move_file_to(self, file_from, file_to):
        self.ssh.runcmd(f'sudo sh -c "mv {file_from} {file_to}"')

    def delete_file(self, file_name):
        self.ssh.runcmd(f'sudo sh -c "rm {file_name}"')

    def read_logs(self, message, log_location):
        loglines = self.ssh.runcmd(f"sudo sh -c \"grep \'{message}\' {log_location}\" ")
        return loglines

    def check_for_log_message_in_tail(self, tail, location, message):
        log = self.ssh.runcmd(f'sh -c "tail -{tail} {location} |grep \'{message}\'"')[0]

        if len(log) > 0:
            log = log.split("]:")[-1]

        return log

    def delete_file_in_s3_if_present(self, bucket, key, key_filter):
        bucket_conn = self.s3_res.Bucket(bucket)
        file_present = self.confirm_file_in_s3(bucket, key)
        if file_present:
            objects_to_delete = []
            for obj in bucket_conn.objects.filter(Prefix=key_filter):
                objects_to_delete.append({'Key': obj.key})
            bucket_conn.delete_objects(
                Delete={
                    'Objects': objects_to_delete
                }
            )

    def confirm_file_in_s3(self, bucket, key):
        try:
            self.s3.get_object(Bucket=bucket, Key=key)
            return True
        except ClientError as e:
            if e.response["Error"]["Code"] == "NoSuchKey":
                print(f"Error: File {key} was not found")
                return False
            else:
                raise

    def load_winlog_into_s3_bucket(self, file_date, file_path, bucket_name, key):
        self.s3.upload_file(f"{file_path}", bucket_name, key)
