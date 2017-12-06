# standard libraries
import tkinter as tk
from tkinter import ttk
# local files
import data_reader2
import SingleRead
import ContinousRead


class SensorGUI(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        tk.Label(self, text='Data Logger').pack(side='top')

        # make notebook
        notebook = ttk.Notebook(self)
        single_read = SingleRead.SingleRead(self, notebook)
        notebook.add(single_read, text="Single Read")
        self.Continous_Read = ContinousRead.ContinousRead(self, notebook)
        notebook.add(self.Continous_Read, text ="Continous Read")

        notebook.pack(side='top', expand=True, fill=tk.BOTH)

        self.initialized = False
        self.calibrate_sensors = True
        self.power_read = False

        button_frame = tk.Frame(self)
        button_frame.pack(side='bottom')

        self.read_button = tk.Button(button_frame, text="calibrate_sensors", command=self.calibrate)
        self.read_button.pack(side='left')
        self.reading = False
       #self.continue_button = tk.Button(button_frame, text="read_continue", command=self.toggle_continuous_read)
       #self.continue_button.pack(side='left')

        self.power = True
        self.toggle_power_button = tk.Button(button_frame, text="Power On", command=self.toggle_power_read)
        self.toggle_power_button.pack(side='left')


    def calibrate(self):
        data_reader2.usb_write('O')

    def single_read(self):
        data_reader2.usb_write('T')
        self.read_data(continous=False)


    def toggle_power_read(self):
        if self.power:
            self.power = False
            self.toggle_power_button.config(text="Power Off")
            self.Continous_Read.continue_button.config(state='disabled')
            data_reader2.usb_write('F')
        else:
            self.power = True
            data_reader2.usb_write('N')
            self.Continous_Read.continue_button.config(state='active')
            self.toggle_power_button.config(text="Power On")


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


if __name__ == '__main__':
    app=SensorGUI()
    app.title("Gas Sensor Array")

    app.geometry("800x600")

    app.mainloop()


