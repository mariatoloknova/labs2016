#!/usr/bin/python3

import sys
import os

pwd = os.getcwd()
if not sys.argv[1:]:
    print("Give me at least 1 file")
else:
    for dir in sys.argv[1:]:
        dirPath = pwd + "/" + dir
        if os.path.exists(dirPath) and os.path.isfile(dirPath):
            with open(str(dir), "r") as file:
                print(file.read())
        else:
            print("File", dirPath, "doesn't exist or it isn't a file")
