from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk




class Login(tk.Frame):

    def __init__(self, master, w=800, h=480):
        tk.Frame.__init__(self, master, width=w, height=h, background='#29b18a')

        label = tk.Label(self, text = 'The Box', font =('Helvetica', 30), fg="#53713F", bg="#202020", highlightbackground="#202020")
        label.place(x=250,y=5)


        ulabel = tk.Label(self, text = 'Username', font =('Helvetica', 15), fg="#53713F", bg="#202020")
        ulabel.place(x=150,y=200)

        plabel = tk.Label(self, text = 'Password', font =('Helvetica', 15), fg="#53713F", bg="#202020")
        plabel.place(x=150,y=250)
