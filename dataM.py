import datetime
import json
import time


data_path = "usage.json"

last_program_time = time.time()

with open(data_path, "r") as file:
    usage_data = json.load(file)

def saveData():
    with open(data_path, "w") as file:
        json.dump(usage_data, file)


curr_date_str = str(datetime.datetime.now().date())
if curr_date_str not in usage_data:
    usage_data[curr_date_str] = {}
saveData()


def get_today(colors):
    programs = []
    for prog in usage_data[str(datetime.datetime.now().date())]:
        prog_time = 0
        if prog in [] : # dinge, die nicht aktiv sein können ausschließen
            continue
        for entry in usage_data[str(datetime.datetime.now().date())][prog]:
            prog_time += usage_data[str(datetime.datetime.now().date())][prog][entry]["duration"]
        programs.append([prog, prog_time])


    new_programs = programs
    if len(programs) > colors:
        new_programs.sort(key=lambda x: x[1], reverse=True)
        rest = sum(t[1] for t in new_programs[-(colors-1):])
        new_programs = new_programs[:-(colors-1)]
        new_programs.append(["Other", rest])
        new_programs.sort(key=lambda x: x[1], reverse=True)

    else:
        new_programs.sort(key=lambda x: x[1], reverse=True)
        
    return new_programs

def new_entry(program, duration, mouseDistance, mouseMovetime, keystrokes, typetime):
    global last_program_time

    curr_date_str = str(datetime.datetime.now().date())
    if curr_date_str not in usage_data:
        usage_data[curr_date_str] = {}
    if program not in usage_data[curr_date_str]:
        usage_data[curr_date_str][program] = {}

    usage_data[curr_date_str][program][str(last_program_time)] = {
        "duration" : duration,
        "mouseDistance" : mouseDistance,
        "mouseMovetime" : mouseMovetime,
        "keystrokes" : keystrokes,
        "typetime" : typetime
    }
    last_program_time = time.time()
    saveData()