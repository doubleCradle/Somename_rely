from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
from functools import partial
from tryTogglebtn import ToggleButton
import time


from app import App 
from login import Login
from stats import Statistics
from sidepanel import ToolPanel
from about import About
from sidebutton import ZButton





class MainFrame(tk.Frame):
    def __init__(self, master, w, h):
        self.w = w
        self.h = h
        self.swidth = 0
        self.frame = tk.Frame.__init__(self, master, width=self.w, height=self.h,bg="#29b18a")
        self.canvas = Canvas(self.frame, bg="#29b18a", width=self.w, height=self.h)

        # self.toolpanel = ToolPanel(self, 100, self.h)
        # self.toolpanel.pack(side=tk.LEFT)

        # sbutton = tk.Button(self.toolpanel, width= 30, fg='#202020', bg='#202020', highlightbackground='#202020', highlightthickness=0, command=self.fold_window)
        # sbutton.pack(side=tk.TOP)

        buttonFont = font.Font(family='Helvetica', size=20)

        self.arrowimage = ImageTk.PhotoImage(Image.open("UI/teal4040.png"))
        #self.rarrowimage = ImageTk.PhotoImage(Image.open("UI/teal4040.png"))
        self.buttonimage = ImageTk.PhotoImage(Image.open("UI/button.jpg"))
        self.statsicon = ImageTk.PhotoImage(Image.open("UI/stats80.png"))
        self.appicon = ImageTk.PhotoImage(Image.open("UI/home80.png"))
        self.profileicon = ImageTk.PhotoImage(Image.open("UI/setting80.png"))

        #self.button = tk.Button(self.frame, image=self.arrowimage, fg='#65a2b5', bg='#65a2b5', highlightbackground='#FFFFFF', highlightthickness=0, command=self.switch_frame(MainFrame), relief=RAISED)
        #button.pack(side=tk.BOTTOM)
        #self.button.place(x=4,y=4)

        #self.toolpanel = ToolPanel(self, self.swidth, h)
        #self.toolpanel.pack(side=tk.LEFT, fill=tk.Y)
        # self.sbutton = tk.Button(self.toolpanel, image=self.buttonimage, font=buttonFont, text="Login", width=self.swidth, fg="#53713F", bg='#202020', highlightbackground='#202020', highlightthickness=0, command=self.open_tool, relief=RAISED, compound="center")
        self.sbutton = ZButton(self.frame, image=self.profileicon, command=lambda: [self.switch_frame(Login)])
        #self.sbutton.config(activebackground='#202020')
        self.sbutton.place(x=700,y=220)

        self.sbutton1 = ZButton(self.frame, image=self.appicon, command=lambda: [self.switch_frame(App)])
        self.sbutton1.place(x=700,y=50)
        #self.sbutton1.config(activebackground='#202020')
        #self.sbutton1 = 

        #self.sbutton1 = tk.Button(self.toolpanel, image=self.buttonimage, font=buttonFont, text="About", width=self.swidth, fg="#53713F", bg='#202020', highlightbackground='#202020', highlightthickness=0, command=lambda:[self.open_tool(tog=[1]),self.switch_frame(About)], relief=RAISED, compound="center")
        #self.sbutton1 = ZButton(self.frame, command=lambda: [self.switch_frame(About)])
        #self.sbutton1.place(x=4,y=420)

        self.sbutton1 = ZButton(self.frame, image=self.statsicon,command= lambda : [self.switch_frame(Statistics)])
        #self.sbutton1.config(activebackground='#202020')
        self.sbutton1.place(x=700,y=380)

        self.label = tk.Label(self.frame,bg="#29b18a", fg="white", font=("Helvetica",10), text="placeholder")
        self.label.place(x=670,y=4)

        self.set_label()



    def set_label(self):
        #currentTime = time.strftime('%H:%M:%S')
        currentTime = time.strftime("%b %d %Y %-I:%M %p")
        self.label['text'] = currentTime
        #print(currentTime)
        self.after(1000, self.set_label)


    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
    


    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()



    def fold_window(self):
        self.toolpanel.configure(width=0)



    def close_sidepanel(self):
        print("<<close_sidepanel>>")
        self.swidth = 0
        self.toolpanel.configure(width=self.swidth)
        #self.sbutton.configure(width=self.swidth)
        self.button.place(x=4,y=4)



    # def open_tool(self, tog=[0]):

    #     print("Click!")

    #     tog[0] = not tog[0]

    #     if tog[0]:
    #         #self.toolpanel = ToolPanel(self, 100, self.h)
    #         #self.toolpanel.pack(side=tk.LEFT)
    #         # button = tk.Button(self.toolpanel, width= 30, fg='#303030', bg='#202020', highlightbackground='#303030', highlightthickness=0, command=self.fold_window)
    #         # button.pack(side=tk.TOP)
    #         self.swidth = 150
    #         print("Side open")
    #         self.button.configure(relief=SUNKEN, image=self.rarrowimage)
    #         self.toolpanel.configure(width=self.swidth)
    #         print(self.swidth)
    #         self.sbutton.configure(width=self.swidth)
    #         self.button.place(x=self.swidth,y=4)
    #         self.button.configure(command=self.open_tool)
            

    #     else:

    #         self.swidth = 0

    #         print("side closed")
    #         self.button.configure(relief=RAISED,image=self.arrowimage)
    #         self.toolpanel.configure(width=self.swidth)
    #         self.sbutton.configure(width=self.swidth)
    #         self.button.place(x=4,y=4)
    #         #self.button.configure(command=self.open_tool)
