from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk



class Statistics(tk.Frame):
    def __init__(self, master, w=800, h=480):
        tk.Frame.__init__(self, master, width=w, height=h, background="#29b18a")
