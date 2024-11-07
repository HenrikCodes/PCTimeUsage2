from pynput import keyboard
import time
import string


class keyboard_tracker:
    def __init__(self) -> None:
        self.eventlistener = keyboard.Events()
        self.eventlistener.start()

        self.keys_dead_time = 3
        self.eventcount = 0
        self.start_time = time.time()

    def track_keys(self):
        if time.time()-self.start_time < self.keys_dead_time:
            self.event = self.eventlistener.get(0.01)
            if "Release" == str(self.event).split("(")[0]:
                if str(self.event.key)[1:-1] in str(string.printable):
                    self.eventcount += 1
            return False

        else:
            self.start_time = time.time()
            typespeed = self.eventcount
            self.eventcount = 0
            return typespeed
