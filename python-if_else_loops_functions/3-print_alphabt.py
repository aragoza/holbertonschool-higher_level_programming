#!/usr/bin/python3

for i in range(26):
    if chr(i + 97) == 'e' or chr(i + 97) == 'q':
        continue
    print("{:c}".format(i + 97), end="")
