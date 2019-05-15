''' A simple mock server for adsquare

    Execution syntax:

        python3.6 adsquare_mock_server.py
'''
import socket
from threading import Lock, Thread
import sys
import signal
from optparse import OptionParser
from datetime import datetime
from struct import unpack
from binascii import unhexlify


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

default_host = ""
default_port = 10000
max_clients = 100

default_debug = False
default_send_response = False

message_count = 0
total_data_length = 0
message_lock = Lock()

adsquare_mock_logfile = "adsquare_mock.log"
log_lock = Lock()


def signal_handler(signal, frame):
    print(f"Stopping server: {datetime.utcnow()}")
    print(f"Message receipt summary:")
    print(f"Number of messages received: {message_count}")
    print(f"Length of data             : {total_data_length}")
    sys.exit(0)


def decode_adsquare_binary_notification(message):
    '''
    decodes a string representation of the binary notification sent to adsquare and separates it into
    constituent parts
    example:
    1e00a651443ea3f84da8b2f8e9e1ad4483ae387b8c5a15a3bcb68d60bd72fda2
    1e00 = length of message in bytes excluding the 2 bytes for the length. In hex little endian
    a651443ea3f84da8b2f8e9e1ad4483ae387b = the spid with "-" removed. Plain text, not hex
    c5a15a3bcb68d60bd72fda2 = list of fixed length, 10 digit campaign codes. In hex little endian
    :param message: string representation of the binary notification sent to adsquare
    :return: tuple containing (expected numnber of campaigns, spid, List of integer campaign codes)
    '''
    length_raw = message[0:4]
    length_binary = unhexlify(length_raw)
    length_in_bytes = unpack('<H', length_binary)[0]
    # expected number of campaigns is (message length in bytes - 18 bytes for spid) / 4 bytes per
    # campaign
    expected_campaigns_count = int((length_in_bytes - 18) / 4)
    spid = message[4:40]
    campaign_codes_raw = message[40:]
    campaign_codes = []
    for i in range(0, len(campaign_codes_raw), 8):
        uh = unhexlify(campaign_codes_raw[i:i + 8])
        n = unpack('<I', uh)[0]
        campaign_codes.append(n)
    return (expected_campaigns_count, spid, campaign_codes)


def write_to_file(data):
    log_lock.acquire()
    with open("adsquare_mock.log", "a") as log_file:
        log_file.write(data.hex() + "\n")
        log_file.write(str(decode_adsquare_binary_notification(data.hex())) + "\n")
    log_lock.release()


def update_message_counts(message_length):
    global message_count
    global total_data_length

    message_lock.acquire()
    message_count += 1
    total_data_length += message_length
    message_lock.release()


def handle_connection(client_id, connection, client_address):

    try:
        print(f"Connection received from: {client_address}",  file=sys.stderr)

        # Receive the data
        while True:
            data = connection.recv(1024)
            if data:
                update_message_counts(len(data))
                print(f"{client_id}: Message no: {message_count}", file=sys.stderr)
                if debug:
                    write_to_file(data)
                if send_response:
                    print(f"{client_id, message_count}:sending data back to the client", file=sys.stderr)
                    connection.sendall(data)
            else:
                print(f"{client_id, message_count}: No more data, closing connection", file=sys.stderr)
                break

    finally:
        connection.close()


if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-H", "--hostname", dest="host", default=default_host,
                      help=f"ip address or hostname to listen to (listen on {default_host})")
    parser.add_option("-p", "--port", dest="port", type="int", default=default_port,
                      help=f"port to listen on {default_port})")
    parser.add_option("-r", "--send-response", dest="send_response", action="store_true", default=default_send_response,
                      help=f"flag to indicate a response is to be sent ({default_send_response})")
    parser.add_option("-d", "--debug", dest="debug", action="store_true", default=default_debug,
                      help=f"flag to indicate verbose debugging is required ({default_debug})")

    (options, args) = parser.parse_args()
    host = options.host
    port = options.port
    send_response = options.send_response
    debug = options.debug

    signal.signal(signal.SIGINT, signal_handler)

    if debug:
        with open("adsquare_mock.log", "a") as log_file:
            log_file.write(f"Starting adsquare mock server running on host:port {host}:{port}\n")

    # Listen for incoming connections
    server_address = (host, port)
    sock.bind(server_address)
    sock.listen(max_clients)

    print(f"Starting the test: {datetime.utcnow()}")
    print(f"Starting up on {host} port {port}")
    client_id = 1

    while True:
        connection, client_address = sock.accept()
        t = Thread(target=handle_connection, args=(client_id, connection, client_address))
        t.setDaemon(True)
        t.start()
        client_id += 1
