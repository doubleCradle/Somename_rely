from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import numpy as np
from functools import partial
#from rpi_server import *
from tryTogglebtn import ToggleButton
from sidebutton import ZButton
#from fstrings import f
import time
import datetime
import RPi.GPIO as io

class App(tk.Frame):

    def __init__(self, master, w=800, h=480):

        tk.Frame.__init__(self, master, width=w, height=h, background="#29b18a")
        #self.frame = tk.Frame(master)
        #frame.pack()
        #Label(root, text = 'The Box', font =('Verdana', 15)).grid(row=0, column=200, sticky="NSEW")
        self.photo = ImageTk.PhotoImage(Image.open("UI/gfan100.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("UI/fan100.png"))
        self.roundrect = ImageTk.PhotoImage(Image.open("UI/roundrectangle.png"))

        self.fan = ImageTk.PhotoImage(Image.open("UI/fan100.png"))

        self.on_images = ["UI/fan100.png", "UI/ac100.png", "UI/fridge100.png", "UI/lamp100.png"]
        self.off_images = ["UI/gfan100.png", "UI/gac100.png", "UI/gfridge100.png", "UI/glamp100.png"]
        self.labels = list()
        #self.ulabel = tk.Label(self, image=self.roundrect, font =('Helvetica', 15), fg="#000000", bg="#29b18a")
        #self.ulabel.place(x=145,y=170)

        self.buttons = list()

        self.on_image = list()
        self.off_image = list()

        io.setmode(io.BOARD)

        self.pins = [3, 7, 11, 13]
        self.pinstates = [0, 0, 0, 0]


        for i in range(4):
            #print(self.buttons)  #---> Aye! this is for debug, does nothing.
            #self.buttons.append(ToggleButton(self, command=partial(self.togggle,i)))
            #self.buttons.append(ToggleButton(self, image=self.fan, command=partial(self.togggle,i)))
            self.on_image.append(ImageTk.PhotoImage(Image.open(self.on_images[i])))
            self.off_image.append(ImageTk.PhotoImage(Image.open(self.off_images[i])))
            self.labels.append(tk.Label(self, image=self.roundrect, font =('Helvetica', 15), fg="#000000", bg="#29b18a"))
            self.buttons.append(ToggleButton(self, image=self.off_image[i], command=partial(self.togggle,i)))
            self.buttons[i].place(in_=self.labels[i], relx=0.5, rely=0.5, anchor=CENTER)
            #self.buttons[-1].grid(row=10,column=i)
            #self.buttons[int(-1/2)].place(x=200*int(i),y=200)
            io.setup(self.pins[i], io.OUT)

            self.pinstates[i] = io.input(self.pins[i])

        #self.trybtn = ToggleButton(self, image=self.fan, command=partial(self.togggle,2))
        #self.trybtn.place(in_=self.labels[2], relx = 0.5, rely=0.5, anchor=CENTER)


        print("Pinstates=",self.pinstates)

        #self.buttons[0].place(x=110,y=210)
        #self.buttons[1].place(x=350,y=210)
        #self.buttons[2].place(x=110,y=310)
        #self.buttons[3].place(x=350,y=310)


        self.labels[0].place(x=200,y=150)
        self.labels[1].place(x=200,y=300)
        self.labels[2].place(x=475,y=150)
        self.labels[3].place(x=475,y=300)

        #self.after(100,self.get_states)
        self.update_display()



    def get_states(self):
        for i in range(4):
            self.pinstates[i] = io.input(self.pins[i])
            if self.pinstates[i]==1:
                self.buttons[i].toggled=False
                self.buttons[i].configure(image=self.off_image[i])
            if self.pinstates[i]==0:
                self.buttons[i].toggled=True
                self.buttons[i].configure(image=self.on_image[i])
            #print("NewButtonSet-->",self.buttons[i].image)
            print("NewButtonState-->",self.buttons[i].toggled)
        print("New pinstates", self.pinstates)
        self.update_display()


    def update_display(self):
        #self.after(200,self.get_states)
        #for i in range(4):
        #    if self.pinstates[i]==1:
                #self.buttons[i].toggled=False
        #        self.buttons[i].image=self.photo
        #    if self.pinstates[i]==0:
        #        #self.buttons[i].toggled=True
        #        self.buttons[i].image=self.photo2
        self.after(200,self.get_states)



    def togggle(self, n):
        print(n, " is Pressed & its state is-", self.buttons[n].toggled)
        #io.setmode(io.BOARD)
        #io.setup(self.pins[n], io.OUT)
        if self.buttons[n].toggled == True:
            io.output(self.pins[n], False)
            print("Hey! On!")

        if self.buttons[n].toggled == False:
            io.output(self.pins[n], True)
            print("Hey! OFF!")


        #self.get_states() #print("New Pinstates",self.pinstates)



    
    def toggle(self, n, tog=[0]):
        # if button["image"] == self.photo:
        #     button["image"] = self.photo2

        # if self.buttons[n]["image"] == self.photo:
        #     buttons[n]["image"] = self.photo2

        #print(n,"Hello"


        tog[0] =  not tog[0]

        print(n)

        if tog[0]:

            self.buttons[n].configure(image=self.photo2)
            print("ON")
        
        else:
            self.buttons[n].configure(image=self.photo)
            print("OFF")
