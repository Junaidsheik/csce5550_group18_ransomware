# csce5550_group18_ransomware
Monitoring Code for Ransomeware


# Instructions:
# Step 1: Select one directory consist of files (txt,pdf,py,...etc.)
#
# Step 2: Run the file monitor.py
#
# We are using the signature base monitoring which is mostly done by the tools like snort, norton, comodo ..etc.

# If the file has a signature suppose a string, this program scans the signature in each line of the file.
# If the signature in the program matches with the file then it detects it else the file is clean
#
# Also we are monitoring the file size and date (time will be calculated as per the Unix epoch timestamp) i.e. January 1st, 1970 till now.
# The Unix epoch (or Unix time or POSIX time or Unix timestamp) is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (in ISO 8601: 1970-01-01T00:00:00Z).
#
# The current file time and size in stored in FileData.txt in .csv format
# If the current time and size of the file and original size and time of the file is matching then it file is Clean
# And if the current time and size of the file and original size and time of the file is not matching then it file is infected
