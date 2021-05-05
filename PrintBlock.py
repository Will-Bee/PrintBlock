import os, sys


def printBlock(unnamed_variable):
    """
    Args:
        oneorzerolmao ([int]): [1 for BLOCKING print, else: UNBLOCKING print]
    """
    if oneorzerolmao == True:
        sys.stdout = open(os.devnull, 'w')
        
    else:
        sys.stdout = sys.__stdout__



### examples

print("okay")
printBlock(True)
print("This is not printing")

print("this is no printing too")
printBlock(False)
print("This will print")
