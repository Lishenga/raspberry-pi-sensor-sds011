import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen
# import requests
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


def make_post(payload):
    request = Request(END_POINT, urlencode(payload).encode())
    return urlopen(request).read().decode()


def register_data(timing, unit, values, local=False, server=True):
    if server:
        try:
            make_post({
                "measured": unit,
                "pm_2_5": values[1],
                "pm_10": values[0],
                "created_at": str(datetime.now())
            })
            print('Enviado al servidor')
        except:
            print('Se perdió conexion pero se guardó localmente')

    if local:
        with open(FILE_PATH, 'a') as file:
            log = "{},\t\t\t{},\t\t\t{},\t\t\tµg/m³\n".format(str(datetime.now()), values[1], values[0])
            file.write(log)
