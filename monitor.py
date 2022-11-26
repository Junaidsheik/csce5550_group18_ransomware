#################################
#################################
#### group_18_ransomware.py#######
#### Group 18###Prof. Tunc###UNT##
#### CSCE 5550####FA22############
#################################
#################################
# Disclaimer: Ransomware is ILLEGAL. Do not run in production environments.
# This ransomware program was built for educational purposes as part of a research project. If you use
# this then it is at your own risk.
# This code is for monitoring the virus in a secure environment
# Author: Junaidsheik
# Version 1.1 11/18/2022
#######################################################################################################################
#######################################################################################################################
# Instructions:
# Step 1: Select one directory consist of files (txt,pdf,py,...etc.)
#
# Step 2: Run the file monitor.py
#
# We are using the malware monitoring which is mostly done by the tools like snort, norton, comodo ..etc.
#
# If the file has a Malware suppose a string, this program scans the Malware in each line of the file.
# If the Malware is in the program, it matches with the file then it detects it else the file is clean
#
# Also we are monitoring the file size and date (time will be calculated as per the Unix epoch timestamp)
# i.e. January 1st, 1970 till now.
# The Unix epoch (or Unix time or POSIX time or Unix timestamp) is the number of seconds that have elapsed
# since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (in ISO 8601: 1970-01-01T00:00:00Z).
#
# The current file time and size in stored in FileData.txt in .csv format If the current time and size of the file
# and original size and time of the file is matching then it file is Clean And if the current time and size of the
# file and original size and time of the file is not matching then it file is infected

# Step 3 : Also, we are monitoring the CRUD operations of the files/folders in a specific directory.
#######################################################################################################################

# -*- coding: utf-8 -*-
import glob
import re
import os
import csv
import time
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Checking the malware patterns
######################################################
#### Malware Dectection Section Start###############
######################################################
def MalwareCheck():
    global p
    print("***************************************************")
    print("***********Checking for Malware***********")
    print("***************************************************") \
        # Checks all the files in directory
    # extension can be replaced to : .py, .word, .pdf, .txt, .rtf .....etc.
    programs = glob.glob("*.txt")  # use any file extension or scan specific folder
    for p in programs:
        thisFileInfected = False
        file = open(p, "r")
        lines = file.readlines()
        file.close()
    for line in lines:
        if (re.search("Your files have been infected",
                      line)):  # change the malware string if you're looking of another malware
            # here we detect the virus
            print("Alert virus found in the file: " + p)
            thisFileInfected = True
    if (thisFileInfected == False):
        print(p + " No Virus is found in this file")


def getFileData():
    # collecting original file size and date last modified. Will be saved to a .txt file

    programs = glob.glob('*.txt')  # use any file extension or scan specific folder
    programsList = []
    for p in programs:
        # saves the current file size, date with milliseconds in Unix epoch format "19314......"
        programSize = os.path.getsize(p)
        programModified = os.path.getmtime(p)
        programData = [p, programSize, programModified]

        programsList.append(programData)
    return programsList


def WriteFileData(programs):
    # writes the other files data in FileData.txt
    if (os.path.exists("FileData.txt")):
        return
    with open("FileData.txt", "w") as file:
        # stores the data in .CSV format (coma seperated values)
        wr = csv.writer(file)
        wr.writerows(programs)


# saving the initial results in a .txt file
WriteFileData(getFileData())


######################################################
#### Malware Dectection Section Ends###############
######################################################


######################################################
#### Monitoring Section Start###############
######################################################
def MonitoringChanges():
    print(" ")
    print("********************************************")
    print("***********Print Heuristic Values***********")
    print("********************************************") \
 \
        # compares current file size, time for  each line in file.txt

    with open("FileData.txt") as file:
        fileList = file.read().splitlines()
    originalFileList = []
    for each in fileList:
        items = each.split(',')
        originalFileList.append(items)

    # get current data

    currentFileList = getFileData()

    # compare the old with new data

    for c in currentFileList:
        # comaparing the size and date of current file with original file
        for o in originalFileList:
            if (c[0] == o[0]):
                # file name matched
                if (str(c[1]) != str(o[1]) or str(c[2] != o[2])):
                    # file size, time not matched
                    print("***********Alert files are not matching***********")
                    # print the data in each file
                    print("Current values = " + str(c))
                    print("Original Values = " + str(o))
    else:
        print("File " + c[0] + " is changed")


MalwareCheck()
MonitoringChanges()
######################################################
#### Monitoring Section Ends###############
######################################################




######################################################
############### files monitoring starts###############
######################################################

##### CRUD of the files/folders in a directory will be monitores here"
print(" ")
print("***************************************************")
print("*****Monitoring Changes for Files and Folders******")
print("***************************************************")


class Filecheck(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'event type: {event.event_type} path : {event.src_path}')

    def on_created(self, event):
        print(f'event type: {event.event_type} path : {event.src_path}')

    def on_deleted(self, event):
        print(f'event type: {event.event_type} path : {event.src_path}')


if __name__ == "__main__":
    event_handler = Filecheck()
    observer = Observer()
    observer.schedule(event_handler, path='xxxxxxxxx', recursive=False) # Assign the path to monitor the CRUD ops.
    observer.start()

    try:
        while True:
            time.sleep(1)
    except  KeyboardInterrupt:
        observer.stop()
    observer.join()

######################################################
############### files monitoring starts###############
######################################################


# EACH OF THE BELOW STEPS IS COMMENTED OUT ON
# PURPOSE SO YOU DO NOT ENCRYPT YOUR OWN PC ON ACCIDENT AND REQUIRES
### MANUAL ENGAGEMENT.###

### COMMENT EACH STEP OUT ONE AT A TIME SO YOU CAN WATCH EACH STEP WORK.###
### WHEN YOU ARE READY FOR USE, YOU MAY UNCOMMENT THEM ALL SO IT WORKS ON ONE RUN.###
