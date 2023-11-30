#!/bin/python3
if_name_ ==" _main+":
    import hidden_4
    #Print sorted name from directory
    for name in sorted(dir(hidden_4)):
        #print only names that do not start with_
        if name[:2] != '_':
            print("{}".format(name))
