# -*- coding: utf-8 -*-
import time
import psutil

'''
    Realtime CPU and Memory Monitoring
    to run use "Python3 cpu.py"
'''


def cpu_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)  # monitors cpu usage

    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)  # monitors cpu usage

    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\r Realtime CPU Usage: | |{cpu_bar}| {cpu_usage:.2f}%", end="")
    print(f" Realtime Memory Usage: | |{mem_bar}| {mem_usage:.2f}%", end="\r")


while True: # while until we ends
    cpu_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5) # time gap
