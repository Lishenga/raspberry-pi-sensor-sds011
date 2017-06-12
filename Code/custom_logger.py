import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'logger.txt')


def register_data(timing, unit, values):
    with open(FILE_PATH, 'a') as file:
        log = "Waited {} secs\nValues measured in {}:    PM2.5  {} , PM10 {} \n".format(timing, unit, values[1], values[0])
        file.write(log)


for x in range(5):
    register_data(2, 'µg/m³', [30 + x, x + 20.5])
