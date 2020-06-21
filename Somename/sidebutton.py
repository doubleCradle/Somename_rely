from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import numpy as np
from functools import partial




class ZButton(tk.Button):


    def __init__(self, parent, *args, command=None, **kwargs):
        super().__init__(parent, *args, **kwargs)



        #self.image = ImageTk.PhotoImage(Image.open("UI/button.jpg"))
        #self.off_image = ImageTk.PhotoImage(Image.open("UI/off_button.jpg"))
        self.buttonFont = font.Font(family='Helvetica', size=20)



        self.ON_Config = {'bg': '#29b18a',
                 'relief': 'sunken',
                 'image': None,
                 'highlightbackground':'#29B18A',
                 'activebackground':'#29B18A',
                 'font': self.buttonFont,
                 'text' : None,
                 'fg': '#FFFFFF',
                 'border':0,
                 'borderwidth':0,
                 'highlightthickness':0,
                 'width':80,
                 'compound':tk.CENTER 
                 }

    
        self.OFF_Config = {'bg': '#29b18a',
                  'relief': 'raised',
                  'image': None,
                  'highlightbackground': '#29B18A',
                  'activebackground':'#29B18A',
                  'font': self.buttonFont,                  
                  'text' : None,
                  'fg': '#FFFFFF',
                  'border':0,
                  'borderwidth':0,
                  'highlightthickness':0,
                  'width':00,
                  'compound':tk.CENTER                   
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

        if self.toggled:
            self.config = self.OFF_Config
        
        else:
            self.config = self.ON_Config
        
        self.toggled = not self.toggled
        self.config_button()
        return 'break'

    
    def config_button(self):

        self['bg'] = self.config['bg']
        self['fg'] = self.config['fg']
        self['relief'] = self.config['relief']
        self['image'] = self.config['image']
        self['font'] = self.config['font']
        self['highlightbackground'] = self.config['highlightbackground']
        self['activebackground'] = self.config['activebackground']
        self['border'] = self.config['border']
        self['borderwidth'] = self.config['borderwidth']
        self['text'] = self.config['text']
        #self['bg'] = self.config['bg']
        self['highlightthickness'] = self.config['highlightthickness']
        self['width'] = self.config['width']
        self['compound'] = self.config['compound']

        return "break"

    
    def __str__(self):
        #return f"{self['bg']}, {self['relief']}, {self['image']}"
        print("_sidebutton_str__ -->called_")
    

    def cmd(self):
        self.command()



def button_placeholder():
    print('Toggle!!')
