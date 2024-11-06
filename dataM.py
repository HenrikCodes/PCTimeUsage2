import datetime
import json
import time

# a = [1,2,3,4]
# print(a[-2:])
# raise


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
    program_times = []
    programs = []
    for prog in usage_data[str(datetime.datetime.now().date())]:
        prog_time = 0
        if prog in [] : # dinge, die nicht aktiv sein können ausschließen
            continue
        for entry in usage_data[str(datetime.datetime.now().date())][prog]:
            prog_time += usage_data[str(datetime.datetime.now().date())][prog][entry]["duration"]
        programs.append(prog)
        program_times.append(prog_time)

    new_programs = []
    if len(program_times) > colors:
        new_program_times = program_times
        new_program_times.sort()
        rest = sum(new_program_times[:-4])
        new_program_times = new_program_times[-4:]
        new_program_times.append(rest)
        new_program_times.sort()

        for el in new_program_times:
            if el in program_times:
                index = program_times.index(el)
                new_programs.append([programs[index], el])
            else:
                new_programs.append(["Other", rest])
    else:
        for i, prog in enumerate(programs):
            new_programs.append([prog, program_times[i]])

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