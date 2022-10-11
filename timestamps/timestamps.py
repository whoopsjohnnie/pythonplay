
import os
import sys

from os.path import exists
from pathlib import Path

from parsedate import parsedate

if not sys.argv:
    print("No arguments given")
    print("Example: python ./timestamps.py ./timestamps1.txt")
    exit()

if len(sys.argv) <= 1:
    print("No arguments given")
    print("Example: python ./timestamps.py ./timestamps1.txt")
    exit()

tsfile = sys.argv[1]

if not tsfile:
    print("No timestamps file given")
    print("Example: python ./timestamps.py ./timestamps1.txt")
    exit()

timestamps = []

try:
    # Using readlines()
    timestampsfile = open(tsfile, 'r')
    timestamps = timestampsfile.readlines()
except:
    print("Unable to open file " + tsfile + " for reading")
    print("Example: python ./timestamps.py ./timestamps1.txt")
    exit()

count = 0
# Strips the newline character
for timestamp in timestamps:
    if timestamp and len(timestamp.strip()) > 0:
        # print("Line: {} '{}'".format(
        #     len(timestamp.strip()), 
        #     timestamp.strip()
        # ))
        parsed = parsedate(timestamp.strip()) 
        # print(parsed)
        if not parsed:
            print("Failed to parse line: {}".format(timestamp.strip()))
            # exit()
            continue

        if parsed:
            parsedfilename = parsed[0]
            parsedfiledate = parsed[1]
            if parsedfilename and parsedfiledate:
                if exists("./" + parsedfilename):
                    print( " File or folder " + parsedfilename + " does exist")
                    # print(parsedfilename)
                    # print(parsedfiledate)
                    path = Path("./" + parsedfilename)
                    # print( path )
                    # print( path.is_file() )
                    if path.is_file(): 
                        os.system("touch -t " + parsedfiledate + " " + "./" + parsedfilename)
                    elif path.is_dir():
                       os.system("touch -t " + parsedfiledate + " " + "./" + parsedfilename) 
                # else:
                #     print( " File or folder " + parsedfilename + " does not exist")
