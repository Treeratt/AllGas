# standard libraries
import tkinter as tk
# local files
import data2_class
import data_reader2
import datadisplay  # for typehinting
import Graphs2

class ContinousRead(tk.Frame):
    def __init__(self, master: datadisplay.SensorGUI
                 , notebook):
        tk.Frame.__init__(self,notebook)
        self.master = master
        self.data = data2_class.SensorData()
        self.graphs = Graphs2.PyplotEmbed(self, self.data)
        self.graphs.pack()
        button_frame = tk.Frame(self)
        button_frame.pack(side='bottom')

        self.initialized = False
        self.reading = False
        self.continue_button = tk.Button(button_frame, text="read_continue", command=self.toggle_continuous_read)
        self.continue_button.pack(side='left')

    def toggle_continuous_read(self):
        if self.reading:
            self.after_cancel(self.reading)
            self.reading = False
            self.continue_button.config(text="Read")
            self.master.toggle_power_button.config(state='active')
            data_reader2.usb_write('P')
        else:
            data_reader2.usb_write('R')
            # disable Power on button
            self.continue_button.config(text="Stop Read")
            # self.continue_button.config(state='disabled')
            self.master.toggle_power_button.config(state='disabled')
            self.read_data(continous=True)

    def read_data(self, continous=True):
        if continous:
            self.reading = self.after(1000, self.read_data)
        packet_data = data_reader2.usb_read_data()
        print('data packet: ',packet_data)
        if packet_data:
            print(packet_data)
            self.data.add_data(packet_data)
            if not self.initialized:
                self.initialized = True
                self.graphs.init_data()
            else:
                self.graphs.updata_data()
