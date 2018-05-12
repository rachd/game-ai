from random import shuffle

def printBoard(positions):
    print ("""
    | %s | %s | %s |
    | %s | %s | %s |
    | %s | %s | %s |""" % tuple(positions))

def setInitialPosition():
    initialElements = [1, 2, 3, 4, 5, 6, 7, 8, "_"]
    shuffle(initialElements)
    return initialElements

printBoard(setInitialPosition())