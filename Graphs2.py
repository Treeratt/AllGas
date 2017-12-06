import tkinter as tk
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


FRAME_COLOR = 'pink'
GRAPH_COLOR = 'black'

class PyplotEmbed(tk.Frame):

    """
     Class that will make a tkinter frame with a matplotlib plot area embedded in the frame
     """
    def __init__(self, master, data):
        tk.Frame.__init__(self, master=master)
        self.data = data  # alias data into class
        self.figure_bed, (self.top_axes, self.bottom_axes) = plt.subplots(2, 3)
        self.figure_bed.set_facecolor(FRAME_COLOR)
        self.top_axes[0].set_facecolor(GRAPH_COLOR)
        self.top_axes[1].set_facecolor(GRAPH_COLOR)
        self.top_axes[2].set_facecolor(GRAPH_COLOR)
        self.bottom_axes[0].set_facecolor(GRAPH_COLOR)
        self.bottom_axes[1].set_facecolor(GRAPH_COLOR)
        self.bottom_axes[2].set_facecolor(GRAPH_COLOR)


        self.canvas = FigureCanvasTkAgg(self.figure_bed, master=self)
        self.canvas._tkcanvas.config(highlightthickness=0)
        plt.tight_layout()
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        self.l = None


    def init_data(self):
        self.temp_line, = self.top_axes[0].plot(self.data.time, self.data.temperature, color="white")
        self.top_axes[0].set_ylim(0, 50)
        self.top_axes[0].set_title('TEMPERATURE', fontsize=10)
        self.top_axes[0].set_ylabel('Celsius')
        # self.temp_line, = self.bottom_axes[2].plot(self.data.time, self.data.temperature, color="white")

        self.hum_line, = self.top_axes[1].plot(self.data.time, self.data.humidity, color="yellow")
        self.top_axes[1].set_ylim(0, 100)
        self.top_axes[1].set_title('HUMIDUTY', fontsize=10)
        # self.top_axes[1].set_xlabel('t (s)')
        self.top_axes[1].set_ylabel('Humiduty %')
        # self.hum_line, = self.bottom_axes[2].plot(self.data.time, self.data.humidity, color="yellow")

        self.MQ_2_line, = self.top_axes[2].plot(self.data.time, self.data.MQ_2, color="green")
        self.top_axes[2].set_ylim(0,200)
        self.top_axes[2].set_title('MQ_2', fontsize=10)
        # self.top_axes[1].set_xlabel('t (s)')
        self.top_axes[2].set_ylabel('ppm')
        # self.hum_line, = self.bottom_axes[2].plot(self.data.time, self.data.humidity, color="yellow")


        self.MQ_7_line, = self.bottom_axes[0].plot(self.data.time, self.data.MQ_7,color="red")
        self.bottom_axes[0].set_ylim(0, 50)
        self.bottom_axes[0].set_title('MQ_7',fontsize=10)
        self.bottom_axes[0].set_xlabel('t (s)')
        self.bottom_axes[0].set_ylabel('ppm')

        self.MQ_135, = self.bottom_axes[1].plot(self.data.time, self.data.MQ_135,color="m")
        self.bottom_axes[1].set_ylim(0, 2000)
        self.bottom_axes[1].set_title('MQ_135',fontsize=10)
        self.bottom_axes[1].set_xlabel('t (s)')
        self.bottom_axes[1].set_ylabel('ppm')
        #self.air_line, = self.bottom_axes[2].plot(self.data.time, self.data.air, color="m")


        self.MQ_131_line, = self.bottom_axes[2].plot(self.data.time, self.data.MQ_131, color="blue")
        self.bottom_axes[2].set_ylim(0, 50)
        self.bottom_axes[2].set_title('MQ_131', fontsize=10)
        self.bottom_axes[2].set_xlabel('t (s)')
        self.bottom_axes[2].set_ylabel('ppb')
        plt.tight_layout()
        self.canvas.draw()


    def updata_data(self):

        self.temp_line.set_ydata(self.data.temperature)
        self.temp_line.set_xdata(self.data.time)
        self.top_axes[0].set_xlim(0, self.data.time[-1])


        self.hum_line.set_ydata(self.data.humidity)
        self.hum_line.set_xdata(self.data.time)
        self.top_axes[1].set_xlim(0, self.data.time[-1])

        self.MQ_2_line.set_ydata(self.data.MQ_2)
        self.MQ_2_line.set_xdata(self.data.time)
        self.top_axes[2].set_xlim(0, self.data.time[-1])

        self.MQ_7_line.set_ydata(self.data.MQ_7)
        self.MQ_7_line.set_xdata(self.data.time)
        self.bottom_axes[0].set_xlim(0, self.data.time[-1])

        self.MQ_135.set_ydata(self.data.MQ_135)
        self.MQ_135.set_xdata(self.data.time)
        self.bottom_axes[1].set_xlim(0, self.data.time[-1])

        self.MQ_131_line.set_ydata(self.data.MQ_131)
        self.MQ_131_line.set_xdata(self.data.time)
        self.bottom_axes[2].set_xlim(0, self.data.time[-1])

        # print('+++++++++++++++++++')
        # print(self.data.humidity)
        # print(self.data.time)
        plt.tight_layout()
        self.canvas.draw()



