from random import shuffle

def printBoard(positions):
    print ("""
    | %s | %s | %s |
    | %s | %s | %s |
    | %s | %s | %s |""" % tuple(positions))

def setInitialPosition():
    initialElements = [1, 2, 3, 4, 5, 6, 7, 8, "_"]
    shuffle(initialElements)
    return (initialElements, getEmptyPosition(initialElements))

def checkForSolved(position):
    return position == [1, 2, 3, 4, 5, 6, 7, 8, "_"]

def getEmptyPosition(position):
    return position.index("_")

def moveUp(state):
    position = list(state[0])
    emptyPosition = state[1]
    temp = position[emptyPosition - 3]
    position[emptyPosition - 3] = position[emptyPosition]
    position[emptyPosition] = temp
    return (position, emptyPosition - 3)

def moveDown(state):
    position = list(state[0])
    emptyPosition = state[1]
    temp = position[emptyPosition + 3]
    position[emptyPosition + 3] = position[emptyPosition]
    position[emptyPosition] = temp
    return (position, emptyPosition + 3)

def moveLeft(state):
    position = list(state[0])
    emptyPosition = state[1]
    temp = position[emptyPosition - 1]
    position[emptyPosition - 1] = position[emptyPosition]
    position[emptyPosition] = temp
    return (position, emptyPosition - 1)

def moveRight(state):
    position = list(state[0])
    emptyPosition = state[1]
    temp = position[emptyPosition + 1]
    position[emptyPosition + 1] = position[emptyPosition]
    position[emptyPosition] = temp
    return (position, emptyPosition + 1)

def getMoves(state):
    if (state[1] == 0): return [moveRight(state), moveDown(state)]
    elif (state[1] == 1): return [moveLeft(state), moveRight(state), moveDown(state)]
    elif (state[1] == 2): return [moveLeft(state), moveDown(state)]
    elif (state[1] == 3): return [moveRight(state), moveUp(state), moveDown(state)]
    elif (state[1] == 4): return [moveLeft(state), moveRight(state), moveUp(state), moveDown(state)]
    elif (state[1] == 5): return [moveLeft(state), moveUp(state), moveDown(state)]
    elif (state[1] == 6): return [moveRight(state), moveUp(state)]
    elif (state[1] == 7): return [moveLeft(state), moveRight(state), moveUp(state)]
    elif (state[1] == 8): return [moveLeft(state), moveUp(state)]


state = setInitialPosition()
printBoard(state[0])
print(getMoves(state))

# 0 1 2
# 3 4 5
# 6 7 8