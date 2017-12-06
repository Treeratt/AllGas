# file = open("C:\Users\Use\Documents\PSoC Creator\Workspace02\Design01.cydsn\main.c")
""" Communicate with a USB device for a PSoC electrochemical device
"""
# standard libraries
# installed libraries

import usb.core
import usb.util
#import usb.backend.libusb0
import usb.backend

vendor_id = 0x04B4
product_id = 0x8051
dev = usb.core.find(find_all=True)
for cfg in dev:
    # print(cfg)
    pass



device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
device.set_configuration()

endpoint = device[0][(0, 0)]
#print(endpoint)

def usb_read_data():
    try:
        return device.read(0x82, 18, timeout=1000)
    except Exception as e:
        print("usb error: ", e)
        return None
def usb_write(message):
    try:
        device.write(1, message)
    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    while True:
        try:
            data = usb_read_data()
            if data:
                print(data)
        except Exception as e:
            print("pass", e)