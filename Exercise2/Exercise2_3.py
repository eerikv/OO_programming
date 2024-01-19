# File name:    Exercise2_3.py
# Author:       Eerik Vainio
# Description:  A simple alarm clock.

import os, sched, time

alarm_time = []

# Asks user to set a time for the alarm
def set_alarm_time():
    alarm_input = input("Set a time for the alarm (HH:MM): ")
    return [int(alarm_input[0:2]), int(alarm_input[-2:])]

# Outputs the current local time, if alarm is ringing, outputs the alarm
def show_time(scheduler, alarm):
    os.system("cls")
    print(f'{time.localtime()[3]}:{time.localtime()[4]}:{time.localtime()[5]}')
    if(alarm[0] == time.localtime()[3] and alarm[1] == time.localtime()[4]):
        print("ALARM ALARM ALARM!!")
        
    # Recall the loop every 1 second
    scheduler.enter(1, 1, show_time, (scheduler, alarm))

alarm_time = set_alarm_time()
print(f'Alarm set for {alarm_time[0]}:{alarm_time[1]}. Starting clock...')

# Initialize scheduler
alarm_scheduler = sched.scheduler(time.time, time.sleep)

# Start scheduler after 2 seconds
alarm_scheduler.enter(2, 1, show_time, (alarm_scheduler, alarm_time))
alarm_scheduler.run()
    

    


