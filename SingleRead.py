# standard libraries
import tkinter as tk
# local files

import data2_class
import data_reader2
import struct


class SingleRead(tk.Frame):
    def __init__(self, master, notebook):
        tk.Frame.__init__(self,notebook)
        tk.Label(self,text="Gas reading: ", font=20).pack(side='top')
        self.data = data2_class.SensorData()


        button_frame = tk.Frame(self)
        #self.single_button.pack(side='left')
        left_frame = tk.Frame(self)
        left_frame.pack(padx=50)

        #self.reading = False
        #self.single_button = tk.Button(button_frame, text="single_read", command=self.single_read)
       #self.single_button.pack(side='left')


        self.mq7_label = tk.Label(left_frame, text="MQ 7:     ppm", font=84)
        self.mq7_label.pack(side='top')

        self.mq135_label = tk.Label(left_frame, text="MQ 135:     ppm", font=84)
        self.mq135_label.pack(side='top')

        self.mq2_label = tk.Label(left_frame, text="MQ 2:     ppm", font=84)
        self.mq2_label.pack(side='top')

        self.mq131_label = tk.Label(left_frame, text="MQ 131:     ppm", font=84)
        self.mq131_label.pack(side='top')

        button_frame = tk.Frame(self)
        button_frame.pack(side='bottom')

        self.single_button = tk.Button(button_frame, text="single_read", command=self.single_get_data)
        self.single_button.pack(side='left')

    def single_read(self):
        data_reader2.usb_write('T')
        #self.read_data(continous=False)
        pass

    def single_get_data(self):
        # read usb
        packet = data_reader2.usb_read_data()
        print(packet)

        mq2_value = convert_bytes_to_float32(packet[0:4])
        self.mq2_label.config(text="MQ 2: {:0.0f} ppm".format(mq2_value))

        mq7_value = convert_bytes_to_float32(packet[4:8])
        self.mq7_label.config(text="MQ 7: {:0.0f} ppm".format(mq7_value))

        mq135_value = convert_bytes_to_float32(packet[8:12])
        self.mq135_label.config(text="MQ 135: {:0.0f} ppm".format(mq135_value))

        mq131_value = convert_bytes_to_float32(packet[12:16])
        self.mq131_label.config(text="MQ 131: {:0.0f} ppm".format(mq131_value))

def convert_bytes_to_float32(_bytes):
    _float = struct.unpack('f', _bytes)
    return _float[0]


