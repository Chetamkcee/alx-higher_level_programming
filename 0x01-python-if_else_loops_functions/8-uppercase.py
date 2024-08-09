#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        unicode_value = ord(char)
        if 97 <= unicode_value <= 122:
            char = chr(unicode_value - 32)
        result = char
        print("{}".format(result), end="")
