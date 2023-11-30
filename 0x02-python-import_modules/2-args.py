#!/urs/bin/python3
# prints the number of and the list of its arguments
if_name_ =="_main_":
    import sys

    arg = sys.arg
    size = len(arg) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for i in range(1, size + 1);
        print("{}: {}".format(i, arg[i]))

    elif size == 0:
        print("{} arguments.".format(zize))

    else:
        print("{}argument.".format(size))
        print("{}: {}".format(size, arg[]))
