from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
#import numpy as np
#from functools import partial
#from rpi_server import *
from tryTogglebtn import ToggleButton
#from fstrings import f
#import time
#import datetime
#import RPi.GPIO as io



class ToolPanel(tk.Frame):
    def __init__(self, master, w, h):
        tk.Frame.__init__(self, master, width=w, height=h, background='#29b18a')
