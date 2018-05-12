def printBoard(positions):
    print ("""
    | %s | %s | %s |
    | %s | %s | %s |
    | %s | %s | %s |""" % tuple(positions))

printBoard([1, 2, 3, 4, 5, 6, 7, 8, "_"])