import psutil
import win32gui
import win32process
import time
import json



class process_tracker:
    settings_path = "settings.json"
    def __init__(self):
        self.processStartTime = time.time()
        
        with open(self.settings_path, "r") as file:
            self.settings = json.load(file)
        self.programs = self.settings["programNames"]

        self.lpname = ""


    def saveSettings(self):
        with open(self.settings_path, "w") as file:
            self.settings["programNames"] = self.programs
            json.dump(self.settings, file)

    def get_program_name(self, prog, gui):

        if prog not in self.programs:
            self.programs[prog] = gui.get_input(prog)
            self.saveSettings()

        return self.programs[prog]

    def get_active_program_executable(self):
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        # Remove any negative process IDs
        if pid < 0:
            return pid, "None"

        # Find the process and get its executable path
        try:
            process = psutil.Process(pid)
            executable_path = process.exe()
            return pid, executable_path
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return pid, "None"

    def process_change(self, gui):
        pid, ppath = self.get_active_program_executable()
        pname = self.get_program_name(ppath, gui)
        change_detect = False
        if ppath == "":
            return change_detect, None, None
        delta_t = 0
        forRet = None
        if pname != self.lpname:
            # print(ppath)
            delta_t = time.time()-self.processStartTime
            if pname in self.settings["ignorePrograms"]:
                pass
            elif (delta_t) < 0.1:
                pass
            else:
                change_detect = True
                forRet = self.lpname
                # print(f"{round(time.time()-self.processStartTime, 5):>7} s  -  {lp[1]}")
            self.lpname = pname
            self.processStartTime = time.time()


        return change_detect, delta_t, forRet