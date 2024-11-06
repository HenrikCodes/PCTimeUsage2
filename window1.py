# gerade am mouseoveraktion machen mit tooltip oder etwas anderem oder mausposition
import time
from ast import Import
from cgitb import text
from http.client import ImproperConnectionState
from sqlite3 import Time
import tkinter as tk
from tkinter.messagebox import YES
from turtle import color, up, width
from typing import Literal
import ttkthemes as ttk
import math
from screeninfo import get_monitors
from tkinter import simpledialog
from tkinter import messagebox

import dataM

class gui:
    def __init__(self):
        self.mcs = {'dbl': '#348888',
                    'bl' : '#22BABB',
                    'lbl': '#9EF8EE',
                    'or' : '#FA7F08',
                    'dor': '#F24405',
                    'tp' : '#FFFFFE'}

        self.font = ('arial', 8)

        self.root = tk.Tk()
        self.root.attributes('-alpha', 1)
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", self.mcs['tp'])
        
        self.monitor_width = get_monitors()[0].width
        self.monitor_height = get_monitors()[0].height
        self.window_height = int(self.monitor_height/30)

        self.root.title('')
        self.root.geometry(f'{self.monitor_width}x{self.window_height}+0+{self.monitor_height-self.window_height}')
        self.root.resizable(False, False)

        self.lw = 10
        self.yoff = self.window_height - int(self.lw/10) #- 100
        self.xoff = int(self.monitor_width/50)


        style = ttk.ThemedStyle(self.root)
        style.theme_use('clam')

        self.c = tk.Canvas(highlightthickness=0)
        self.c.config(bg=self.mcs['tp'])
        self.c.pack(fill=tk.BOTH, expand=YES)

        self.update_all()

    def get_input(self, progPath):
        # Show a warning message before asking for input
        messagebox.showwarning("Warning", f"{progPath} not in list of programs.")

        # Prompt the user for input
        user_input = simpledialog.askstring("Set new program name", f"{progPath} not in list of programs\nSet Name for program to:")
        print(f"user added {user_input} as program name for {progPath}")
        if user_input:
            return user_input
        else:
            return progPath
        


    def CreateToolTip(self):
        def enter_retext(event):
            text = ""
            x = self.root.winfo_pointerx()
            for i, stst in enumerate(self.ststp):
                if stst[0] < x <= stst[1]:
                    text = f'{self.programs[i][0]} - {time.strftime("%H:%M:%S", time.gmtime(self.programs[i][1]))}'
                    break
            self.c.itemconfig(self.main_text, text=text)
        def leave_retext(event):
            self.c.itemconfig(self.main_text, text=time.strftime("%H:%M:%S", time.gmtime(self.totalTime)))
        
        self.root.bind('<Enter>', enter_retext)
        self.root.bind('<Leave>', leave_retext)


    def update_all(self):
        self.programs = dataM.get_today(len(self.mcs)-1)
        self.const_factor = 1920/math.sqrt(3600*24) # * 10 ### ACHTUNG for better visibility the times 10
        self.totalTime = sum([t[1] for t in self.programs])+0.001
        self.factor = self.const_factor * math.sqrt(self.totalTime)/self.totalTime
        self.lastEnd = self.xoff -1 #1920/2-totalTime*factor/2
        self.ststp = []

        self.c.delete("all")
        # self.c = tk.Canvas(highlightthickness=0)
        self.main_text = self.c.create_text(self.xoff, self.yoff-int(self.font[1]/2), text=time.strftime("%H:%M:%S", time.gmtime(self.totalTime)),
                    font=self.font, fill='white', anchor='sw')      # font=("Small Fonts",7)
        for i, prog in enumerate(self.programs):
            self.c.create_line(self.lastEnd, self.yoff, self.lastEnd+self.factor*prog[1],
                        self.yoff, capstyle="round", width=self.lw, fill=(list(self.mcs.values())[i]))
            self.ststp.append([self.lastEnd, self.lastEnd+self.factor*prog[1]])
            self.lastEnd += prog[1]*self.factor

        self.CreateToolTip()
        


    def update_window(self):
        self.root.update()
        self.root.wm_attributes("-topmost", True)