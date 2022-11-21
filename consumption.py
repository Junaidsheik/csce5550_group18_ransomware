import psutil
import datetime
import time
import schedule
import openpyxl
import os

pid = int(input("Enter Process ID: "))


def Alert():
    cpuusage = psutil.cpu_percent(interval=1)
    if cpuusage > 1:  # CPU consumption percentage
        print("Alert! CPU consumption is high", cpuusage)
    memusage = psutil.virtual_memory( ).percent
    if memusage > 50:  # Mem consumption percentage
        print("Memory consumption is high", memusage)


def monitor():
    time = datetime.datetime.now( ).strftime("%Y%m%d - %H:%M:%S")
    p = psutil.Process(pid)
    cpu = p.cpu_percent(interval=1) / psutil.cpu_count( )

    memory_mb = p.memory_full_info( ).rss / (1024 * 1024)
    memory = p.memory_percent( )

    path = r"C:\Users\Jshei\Desktop\Monitor_Result.xlsx"
    assert os.path.isfile(path)
    with open(path, "r") as f:
        pass
    file = openpyxl.load_workbook(path)
    sheet = file.active

    sheet.cell(column=1, row=sheet.max_row + 1, value=time)
    sheet.cell(column=2, row=sheet.max_row, value=pid)
    sheet.cell(column=3, row=sheet.max_row, value=cpu)
    sheet.cell(column=4, row=sheet.max_row, value=memory_mb)
    sheet.cell(column=5, row=sheet.max_row, value=memory)
    file.save(path)


schedule.every(1).second.do(Alert)
schedule.every(1).second.do(monitor)

while True:
    schedule.run_pending( )
    time.sleep(1)
