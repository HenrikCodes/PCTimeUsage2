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
import random
from screeninfo import get_monitors


import dataM


mcs = {'dbl': '#348888',
       'bl' : '#22BABB',
       'lbl': '#9EF8EE',
       'or' : '#FA7F08',
       'dor': '#F24405',
       'tp' : '#FFFFFE'}

font = ('arial', 15)


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text, position, color):
        self.text = text
        if self.tipwindow or not self.text:
            return
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.update()
        tw.wm_attributes("-topmost", True)
        tw.wm_geometry("+%d+%d" % (position-(tw.winfo_width()/4), monitor_height-(window_height)))
        label = tk.Label(tw, text=self.text, justify='left', fg='white',
                      background=color, relief=tk.SOLID, borderwidth=0,
                      font=font)
        label.pack(ipadx=2)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget):
    toolTip = ToolTip(widget)
    def enter(event):
        x = root.winfo_pointerx()
        for i, stst in enumerate(ststp):
            if stst[0] < x < stst[1]:
                text = f'{programs[i][0]} - {time.strftime("%H:%M:%S", time.gmtime(programs[i][1]))}'
                xpi = (stst[0]+stst[1])/2
                break
        toolTip.showtip(text, xpi, list(mcs.values())[i])
    def leave(event):
        toolTip.hidetip()

    def enter_retext(event):
        x = root.winfo_pointerx()
        for i, stst in enumerate(ststp):
            if stst[0] < x < stst[1]:
                text = f'{programs[i][0]} - {time.strftime("%H:%M:%S", time.gmtime(programs[i][1]))}'
                break
        c.itemconfig(main_text, text=text)
    def leave_retext(event):
        c.itemconfig(main_text, text=time.strftime("%H:%M:%S", time.gmtime(totalTime)))
    
    widget.bind('<Enter>', enter_retext)
    widget.bind('<Leave>', leave_retext)


root = tk.Tk()
root.attributes('-alpha', 1)
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", mcs['tp'])

monitor_width = get_monitors()[0].width
monitor_height = get_monitors()[0].height
window_height = int(monitor_height/30)

root.title('')
root.geometry(f'{monitor_width}x{window_height}+0+{monitor_height-window_height}')
root.resizable(False, False)

c = tk.Canvas(highlightthickness=0)
lw = 10
yoff = window_height - int(lw/2)
xoff = int(monitor_width/50)

programs = dataM.get_today()
const_factor = 1920/math.sqrt(3600*24)
totalTime = sum([t[1] for t in programs])+0.001
factor = const_factor * math.sqrt(totalTime)/totalTime
lastEnd = xoff #1920/2-totalTime*factor/2
ststp = []

main_text = c.create_text(xoff, yoff-int(font[1]/2), text=time.strftime("%H:%M:%S", time.gmtime(totalTime)),
              font=font, fill='white', anchor='sw')      # font=("Small Fonts",7)
for i, prog in enumerate(programs):
    c.create_line(lastEnd, yoff, lastEnd+factor*prog[1],
                  yoff, capstyle="but", width=lw, fill=(list(mcs.values())[i]))
    ststp.append([lastEnd, lastEnd+factor*prog[1]])
    lastEnd += prog[1]*factor

c.config(bg=mcs['tp'])
c.pack(fill=tk.BOTH, expand=YES)


CreateToolTip(root)



def update_total_time():
    c.itemconfig(main_text, text=time.strftime("%H:%M:%S", time.gmtime(totalTime)))

style = ttk.ThemedStyle(root)
style.theme_use('clam')

while True:
    root.update()
    root.wm_attributes("-topmost", True)