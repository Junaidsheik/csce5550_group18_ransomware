# CSCE5550_group18_ransomware
Monitoring Code for Ransomeware


#  Instructions:
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
#
Image with the virus in virus.txt
![test1](https://user-images.githubusercontent.com/53267660/202780012-6e88c7b5-d141-4595-84c7-64b33f523295.jpg)
#
Image without the virus in virus.txt
![test2](https://user-images.githubusercontent.com/53267660/202780016-b26ee48e-0b96-454a-b83f-6a0c4afd6414.jpg)

# Hashing:
# Also, we are monitoring the CRUD operations of the files/folders in a specific directory.
![g1](https://user-images.githubusercontent.com/53267660/204113186-cc9c23c7-e2cd-4941-94ae-956f2c112e13.jpg)
#
# Real-Time CPU and Memory Monitoring:
![g2](https://user-images.githubusercontent.com/53267660/204113225-4aae2981-50e6-465d-a21a-269da4d621be.jpg)



