import requests
import config
import json
import time
from collections import namedtuple
from datetime import datetime, timedelta

class API():

    def __init__(self):
        self.base_url = config.url

    def create_computer(self, name, intro_date, discon_date, company):
        if name == "null":
            name = ""

        if intro_date == "null":
            intro_date = ""

        if discon_date == "null":
            discon_date = ""

        if company == "null":
            company = ""
        else:
            company = self.get_company_code(company)

        payload = {
            "name": f"{name}",
            "introduced": f"{intro_date}",
            "discontinued": f"{discon_date}",
            "company": f"{company}"
        }

        self.response = requests.post(self.base_url,json=payload)


    def confirm_response_code(self, expected_code):

        if str(self.response) == f"<Response [{expected_code}]>":
            return True
        return False

    def delete_computer(self, url):
        self.response = requests.post(f"{url}/delete")

    def update_computer(self, name, intro_date, discon_date, company, url):
        if name == "null":
            name = ""

        if intro_date == "null":
            intro_date = ""

        if discon_date == "null":
            discon_date = ""

        if company == "null":
            company = ""
        else:
            company = self.get_company_code(company)

        payload = {
            "name": f"{name}",
            "introduced": f"{intro_date}",
            "discontinued": f"{discon_date}",
            "company": f"{company}"
        }

        self.response = requests.post(url, json=payload)


    def get_company_code(self, company):


        company_dict = {
                    "Apple Inc.": 1,
                    "Thinking Machines": 2,
                    "RCA": 3,
                    "Netronics": 4,
                    "Tandy Corporation": 5,
                    "Commodore International": 6,
                    "MOS Technology": 7,
                    "Micro Instrumentation and Telemetry Systems": 8,
                    "IMS Associates, Inc.": 9,
                    "Digital Equipment Corporation": 10,
                    "Lincoln Laboratory": 11,
                    "Moore School of Electrical Engineering": 12,
                    "IBM": 13,
                    "Amiga Corporation": 14,
                    "Canon": 15,
                    "Nokia": 16,
                    "Sony": 17,
                    "OQO": 18,
                    "NeXT": 19,
                    "Atari": 20,
                    "Acorn computer": 22,
                    "Timex Sinclair": 23,
                    "Nintendo": 24,
                    "Sinclair Research Ltd": 25,
                    "Xerox": 26,
                    "Hewlett-Packard": 27,
                    "Zemmix": 28,
                    "ACVS": 29,
                    "Sanyo": 30,
                    "Cray": 31,
                    "Evans &amp; Sutherland": 32,
                    "E.S.R. Inc.": 33,
                    "OMRON": 34,
                    "BBN Technologies": 35,
                    "Lenovo Group": 36,
                    "ASUS": 37,
                    "Amstrad": 38,
                    "Sun Microsystems": 39,
                    "Texas Instruments": 40,
                    "HTC Corporation": 41,
                    "Research In Motion": 42,
                    "Samsung Electronics": 43,
                    "invalid company": "aa"
        }
        return company_dict[company]
