import pynput
import time
import math
from screeninfo import get_monitors


class mouse_tracker:
    def __init__(self):
        self.lastMousePosition = pynput.mouse.Controller().position
        self.screenMMperPixel = get_monitors()[0].width_mm / get_monitors()[0].width

        self.mouse_dead_time = 1
        self.distance = 0
        self.start_time = time.time()   
        
    def track_mouse(self):
        if time.time()-self.start_time < self.mouse_dead_time:
            self.newMousePosition = pynput.mouse.Controller().position
            # print(type(self.newMousePosition))
            if self.newMousePosition == None:
                return False
            if self.lastMousePosition != self.newMousePosition:
                self.distance += math.dist(self.lastMousePosition, self.newMousePosition)*self.screenMMperPixel
                self.lastMousePosition = self.newMousePosition
            return False
        
        else:
            self.start_time = time.time()
            dist = self.distance
            self.distance = 0
            return dist
        