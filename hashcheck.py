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
#
# Step 1: Run the file hashcheck.py
#
# Step 2: Provide the specific directory which you want to get the hash check.
#
# Step 3: You can compare the hashcheck with the orignal hash and hash after changes has been done, if any.
#
# we are using sha512 hashing
#######################################################################################################################
import hashlib
import os
from checksumdir import dirhash

directory = r"C:\Users\Jshei\Desktop\monitoring_group18"
hashcheck = dirhash(directory, 'sha512')

print ("Sha512 hash for the entire directory is:  " + hashcheck)
