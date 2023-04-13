#!/usr/bin/python3
"""
captures stdin line by line and computes
"""
import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
x = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            y = x
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                y += 1
            try:
                file_size += int(tokens[-1])
                if y == x:
                    x += 1
            except FileNotFoundError:
                if y == x:
                    continue
        if x % 10 == 0:
            print("file size is: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("file size is: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("file size is: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
