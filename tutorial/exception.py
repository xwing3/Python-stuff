"""
    try:
       You do your operations here;
       ......................
    except ExceptionI:
       If there is ExceptionI, then execute this block.
    except ExceptionII:
       If there is ExceptionII, then execute this block.
       ......................
    else:
       If there is no exception then execute this block.

The try-finally Clause
    You can use a finally: block along with a try: block.
    The finally block is a place to put any code that must execute, whether the try-block raised an exception or not.
    You cannot use else clause as well along with a finally clause.
    When an exception is thrown in the try block, the execution immediately passes to the finally block.
    After all the statements in the finally block are executed, the exception is raised again and is handled in the except statements if present in the next higher layer of the try-except statement.
Argument of an Exception
    An exception can have an argument, which is a value that gives additional information about the problem.
    The contents of the argument vary by exception. You capture an exception's argument by supplying a variable in the except clause as follows
         try:
           You do your operations here;
           ......................
        except ExceptionType, Argument:
           You can print value of Argument here...

    This variable receives the value of the exception mostly containing the cause of the exception.
    The variable can receive a single value or multiple values in the form of a tuple. This tuple usually contains the error string, the error number, and an error location.
"""

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument

# Call above function here.
temp_convert("xyz");