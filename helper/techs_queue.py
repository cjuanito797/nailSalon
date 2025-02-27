import django
import os
from datetime import datetime, date
import sys

sys.path.append ("../NailSalon")
os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'NailSalon.settings')
django.setup ( )

from Scheduling.models import timeSlots
from Appointments.models import Sale
FILE_DIR = "helper/techs_queue"

_WAIT_QUEUE = []
_WORK_QUEUE = []

#QUEUE CONTROL FUNCTIONS----------------------------------------------
# Build fresh queue in every day at open time salon open
def build_fresh_wait_queue(today_date: date, filedir=FILE_DIR): # change to queue of all tech of the day()
    timeslots = []                      # NEED CHANGE TODAY DATE
    temp = list(timeSlots.objects.filter(date=today_date).values('tech', 'arrive_time'))
    for t in temp:
        if t['arrive_time'] != None:
            t['arrive_time'] = datetime.combine(date.min, t['arrive_time']) - datetime.min
            timeslots.append(t)
        
    lines = "_WAIT\n"
    sorted_list = sorted(timeslots, key=lambda x: x['arrive_time'])
    for sl in sorted_list:
        lines += f"{sl['tech']}:0\n"
    lines += "_WORK\n"
    f = open(filedir, "w")
    f.write(lines)
    f.close()

# Clockin (backup) tech who arrive after fresh queue is created
def clock_tech_after_fresh_build(email):
    read_temp()
    low_priority = 0
    if len(_WAIT_QUEUE) > 0:
        low_priority = _WAIT_QUEUE[-1][1]
        
    if len(_WORK_QUEUE) > 0:
        if low_priority < _WORK_QUEUE[-1][1]:
            low_priority = _WORK_QUEUE[-1][1]
    _WAIT_QUEUE.append( (email, low_priority) )
    save_queue()

# Move chosen technician from Wait queue into Work queue
def wait_to_work(email):
    read_temp()
    if len(_WAIT_QUEUE) >=1:
        for i in _WAIT_QUEUE:
            if i[0] == email:
                a = _WAIT_QUEUE.remove(i)
                _WORK_QUEUE.append( (i[0], i[1]+1) )
        save_queue()
        return len(_WAIT_QUEUE)
    else:
        return 0

# Move chosen technician from Work queue into Wait queue
def work_to_wait(email):
    read_temp()
    if len(_WORK_QUEUE) >=1:
        for i in _WORK_QUEUE:
            if i[0] == email:
                a = _WORK_QUEUE.remove(i)
                _WAIT_QUEUE.append(i)
        save_queue()
        return len(_WAIT_QUEUE)
    else:
        return 0



#BASIC FUNCTIONS-----------------------------------------------------------
# Retrieve technician waiting
def get_WAIT_queue(filedir=FILE_DIR):
    read_temp(filedir)
    return _WAIT_QUEUE

# Retrieve technician working
def get_WORK_queue(filedir=FILE_DIR):
    read_temp(filedir)
    return _WORK_QUEUE
     
# Sort data then write temp file
def save_queue(filedir=FILE_DIR):
    #Sort Tuple
    global _WAIT_QUEUE
    global _WORK_QUEUE
    _WAIT_QUEUE = (sorted(_WAIT_QUEUE, key = lambda x: x[1]))
    _WORK_QUEUE = (sorted(_WORK_QUEUE, key = lambda x: x[1]))
    #then write them in file
    write_temp(filedir)

# Read temp file
def read_temp(filedir=FILE_DIR):
    global _WAIT_QUEUE
    global _WORK_QUEUE
    
    if os.stat(filedir).st_size != 0:
        f = open(filedir, "r")
        lines = f.readlines()
        f.close()
        
        _WAIT_QUEUE = []
        _WORK_QUEUE = []
        
        read_flag = 0
        for line in lines:
            line = line.replace('\n', '')
            if (line == "_WAIT"):
                pass
            else:
                if line != "_WORK" and read_flag == 0:
                    _WAIT_QUEUE.append(to_tuple(line))
                elif line == "_WORK":
                    read_flag = 1
                else:
                    _WORK_QUEUE.append(to_tuple(line))
    else:
        _WAIT_QUEUE = []
        _WORK_QUEUE = []

# Write temp file
def write_temp(filedir=FILE_DIR):
    data = ""
    data += "_WAIT\n"
    for i in _WAIT_QUEUE:
        data += f"{str(i[0])}:{str(i[1])}\n"
    data += "_WORK\n"
    for i in _WORK_QUEUE:
        data += f"{str(i[0])}:{str(i[1])}\n"
    f = open(filedir, "w")
    f.write(data)
    f.close()

# Split formatted string data into tuple  "email:priority" -> ("email", priority)
def to_tuple(line:str) -> tuple:
    temp_str = []
    temp_num =  []
    z = 0
    for c in line:
        if (c != ':' and z == 0):
            temp_str.append(c)
        elif (c == "\n"):
            break
        else:
            z = 1
            if (z==1) and c != ":" :
                temp_num = c
    return ( ((''.join(temp_str)), int(temp_num)) )

# Function to sort the list of tuples by its second item
def Sort_Tuple():
    global _WAIT_QUEUE
    global _WORK_QUEUE
    _WAIT_QUEUE = (sorted(_WAIT_QUEUE, key = lambda x: x[1]))
    _WORK_QUEUE = (sorted(_WORK_QUEUE, key = lambda x: x[1]))



def main():
    #build_fresh_wait_queue(date(2022,12,11))
    
    #global _WAIT_QUEUE
    #print(_WAIT_QUEUE)
    pass
    
if __name__ == '__main__':
    main()