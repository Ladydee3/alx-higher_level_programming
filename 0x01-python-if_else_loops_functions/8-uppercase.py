#!/usr/bin/python3

def to_upper(character):
    if 97 <= ord(character) <= 122:
        return ord(character) - 32
    else:
        return ord(character)

def uppercase(string):
    string_new = ""
    for char in string:
        string_new += chr(to_upper(char))
    print(string_new)
