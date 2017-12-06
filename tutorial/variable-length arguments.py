"""
variable length arguments
An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments.
This tuple remains empty if no additional arguments are specified during the function call.

"""


def printinfo(arg1, *varargs):
    print arg1
    for var in varargs:
        print var

printinfo("test","lala","lala1")
printinfo(100)
