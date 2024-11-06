import time

from WindowTracker import process_tracker
from moustracker import mouse_tracker
from Keylistener import keyboard_tracker
from window1 import gui
import dataM

mouse_dist = 0
mouse_movetime = 0
last_dist = 0
delta_mouse_time = time.time()

total_keystrokes = 0
typing_time = 0
last_keys = 0
delta_keys_time = time.time()

# ohne globale variablen

mouse_tracker = mouse_tracker()
keyboard_tracker = keyboard_tracker()
process_tracker = process_tracker()
gui = gui()

while True:
    gui.update_window()
    changed, duration, prog = process_tracker.process_change(gui)
    if changed:
        # print(f"{prog} with duration {duration}")
        dataM.new_entry(program=prog, duration=duration, mouseDistance=mouse_dist, mouseMovetime=mouse_movetime,
                        keystrokes=total_keystrokes, typetime=typing_time)

        gui.update_all()
        
        mouse_dist = 0
        last_dist = 0
        mouse_movetime = 0
        delta_mouse_time = time.time()

        total_keystrokes = 0
        last_keys = 0
        typing_time = 0
        delta_keys_time = time.time()

    distance = mouse_tracker.track_mouse()
    if distance != False:
        if last_dist != 0 and distance != 0:
            mouse_movetime += time.time()-delta_mouse_time

        last_dist = distance
        mouse_dist += distance
        delta_mouse_time = time.time()

    keystrokes = keyboard_tracker.track_keys()
    if keystrokes != False:
        if last_keys != 0 and keystrokes != 0:
            typing_time += time.time()-delta_keys_time

        last_keys = keystrokes
        total_keystrokes += keystrokes
        delta_keys_time = time.time()