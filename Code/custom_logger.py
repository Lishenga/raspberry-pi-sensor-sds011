import os
import requests
from datetime import datetime

DEBUG = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'logger.txt')

if DEBUG:
    END_POINT = 'http://localhost:8000/services/data/'
else:
    END_POINT = 'http://raspsensor.herokuapp.com/services/data/'


PAYLOAD_TEST = {
    "measured": "µg/m³",
    "pm_2_5": 32.1,
    "pm_10": 42.0,
    "created_at": str(datetime.now())
}


def send_to_server(payload):
    resp = requests.post(END_POINT, json=payload)
    if resp.status_code != 200:
        print('no saved')
    else:
        print('saved')
    print('here')


def register_data(timing, unit, values, local=False, server=True):
    if server:
        send_to_server({
            "measured": unit,
            "pm_2_5": values[1],
            "pm_10": values[0],
            "created_at": str(datetime.now())
        })

    if local:
        with open(FILE_PATH, 'a') as file:
            log = "{},\t\t\t{},\t\t\t{},\t\t\tµg/m³\n".format(str(datetime.now()), values[1], values[0])
            file.write(log)

# for x in range(5):
#     PAYLOAD_TEST['pm_10'] += x
#     send_to_server(PAYLOAD_TEST)
