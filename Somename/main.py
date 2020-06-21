from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk


from mainframe import MainFrame

import RPi.GPIO as io




def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))





root = tk.Tk()
root.geometry('800x480')
root.wm_title("AMX Automation Labs")
root["bg"] = "#29b18a"

print(root['bg'])


io.setmode(io.BOARD)

pins=[3,7,11,13]



print("[-]Getting pins down.... Ahh, This Power Outage!!")
#for i in range(4):
#    io.setup(pins[i],io.OUT)
#    io.output(pins[i],1)
print("[+]Taken down all the pins!")
print("Ready!")




root.attributes("-fullscreen",True)

root.bind('<Motion>',motion)
    
mainframe = MainFrame(root, 800, 480)
mainframe.pack(side="left", fill="y")

root.mainloop()
