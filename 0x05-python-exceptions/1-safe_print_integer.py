#!/usr/bin/python3
def safe_print_interger(value):
    try:
        print("{:d}".format(value))
        return true
    except (ValueError, TypeError):
        return false