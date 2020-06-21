#import fauxmo
#import logging
#import time
#import sys
#import RPi.GPIO as GPIO 
from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import numpy as np
from functools import partial
import time




class ToggleButton(tk.Button):


    def __init__(self, parent, *args, command=None, **kwargs):
        super().__init__(parent, *args, **kwargs)



        self.on_image = ImageTk.PhotoImage(Image.open("UI/on_button.jpg"))
        self.off_image = ImageTk.PhotoImage(Image.open("UI/off_button.jpg"))



        self.ON_Config = {'bg': '#FFFFFF',
                 'relief': 'sunken',
                 'image': None,
                 'highlightbackground':'#FFFFFF',
                 'activebackground':'#FFFFFF',
                 'border':0,
                 'borderwidth':0,
                 'highlightthickness':0,
                 'fg':'#FFFFFF'
                 }

    
        self.OFF_Config = {'bg': '#FFFFFF',
                  'relief': 'raised',
                  'image': None,
                  'highlightbackground': '#FFFFFF',
                  'activebackground':'#FFFFFF',
                  'border':0,
                  'borderwidth':0,
                  'highlightthickness':0,
                  'fg':'#FFFFFF'
                 }


        self.toggled = False 
        self.config = self.OFF_Config
        self.config_button()

        self.bind("<Button-1>", self._toggle_helper)
        self.bind("<ButtonRelease-1>", self._toggle)
        self.command = command 

    

    def _toggle_helper(self, *args):
        return 'break'

    
    def _toggle(self, dummy_event):
        self.toggle()
        self.cmd()

    
    def toggle(self, *args):

        print("buttonState-->",self.toggled)

        if self.toggled:
            self.config = self.OFF_Config
        else:
            self.config = self.ON_Config
        
        self.toggled = not self.toggled
        #self.after(200,self.config_button)
        return 'break'

    
    def config_button(self):

        self['bg'] = self.config['bg']
        self['relief'] = self.config['relief']
        self['image'] = self.config['image']
        self['fg'] = self.config['fg']
        self['border'] = self.config['border']
        self['borderwidth'] = self.config['borderwidth']
        self['highlightthickness'] = self.config['highlightthickness']
        self['highlightbackground'] = self.config['highlightbackground']
        self['activebackground'] = self.config['activebackground']

        return "break"

    
    def __str__(self):
        #return f"{self['bg']}, {self['relief']}, {self['image']}"
        print("__str__ -->called")
    

    def cmd(self):
        self.command()



def button_placeholder():
    print('Toggle!!')


