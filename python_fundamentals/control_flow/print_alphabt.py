#!/usr/bin/env python3
letters = ""
for code in range(ord('a'), ord('z') + 1):
    if chr(code) not in "qe":
        letters += chr(code)
print(letters)
