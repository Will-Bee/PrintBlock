import os, sys


def printBlock(unnamed_variable):
    """
    Args:
        oneorzerolmao ([int]): [1 for BLOCKING print, else: UNBLOCKING print]
    """
    if oneorzerolmao == 1:
        sys.stdout = open(os.devnull, 'w')
        
    else:
        sys.stdout = sys.__stdout__





print("okay")
printBlock(1)
print("This is not printing")

print("this is no printing too")
printBlock(0)
print("This will print")