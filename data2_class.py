# standard library


import csv
import datetime
import struct

SENSORS = ['temperature', 'humidity', 'MQ 2', 'MQ 7', 'MQ 135', 'MQ 131']

class SensorData(object):  # Holds data and is updated by a SensorData object.
    def __init__(self): #Configure default.
        self.temperature = []
        self.humidity = []
        self.MQ_2 = []
        self.MQ_7 = []
        self.MQ_135 = []
        self.MQ_131 = []
        self.time = []
        self.time_pt = 0
        self.initialized = False
        date_started = datetime.datetime.now().strftime("%Y_%m_%d")
        print(date_started)
        self.filename = date_started+"_air_logging.csv"
        # fill out other attributes needed

        with open(self.filename, 'a') as self._file:
            self.writer = csv.writer(self._file)

            self.writer.writerow(['time', 'temperature', 'humidity', 'MQ 2', 'MQ 7', 'MQ 135', 'MQ 131'])
            # _file.close()  python.exe will execute this line before quiting

    def add_data(self, packet): #Function creation the parameter on every method it receives its value from the function invocation


        self.MQ_2.append(convert_bytes_to_float32(packet[0:4]))
        # print(self.MQ_2)

        self.MQ_7.append(convert_bytes_to_float32(packet[4:8]))
        # print(self.MQ_7)

        self.MQ_135.append(convert_bytes_to_float32(packet[8:12]))
        # print(self.MQ_135)

        self.MQ_131.append(convert_bytes_to_float32(packet[12:16]))
        # print(self.MQ_131)

        self.temperature.append(packet[16])
        # print(self.temperature)

        self.humidity.append(packet[17])
        # print(self.humidity)

        self.time_pt += 1
        self.time.append(self.time_pt)
        time = datetime.datetime.now().strftime("%H:%M:%S")

        with open(self.filename, 'a') as self._file:
            self.writer = csv.writer(self._file)
            self.writer.writerow([time, self.temperature[-1], self.humidity[-1], self.MQ_2[-1],
                                  self.MQ_7[-1], self.MQ_135[-1], self.MQ_131[-1]])


def convert_bytes_to_float32(_bytes):
    _float = struct.unpack('f', _bytes)
    return _float[0]
