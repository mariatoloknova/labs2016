#!/usr/bin/python3

import sys

args = []
for arg in sys.argv[1:]:
    if not len(arg)%3:
        args.append(arg)
print(*args, sep = "\n")
