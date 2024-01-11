#!/usr/bin/python3
'''
Module Docs
'''


def canUnlockAll(boxes):
    '''
    Function Docs
    '''
    if (boxes):
        terminateLoop = False
        numOfBoxes = len(boxes)
        setOfKeys = {0}
        setOfKeys.update(boxes[0])
        visitedBoxes = {0}
        while not terminateLoop:
            keys = setOfKeys.copy()
            print(f"Set of keys copy = {keys}")
            for key in keys:
                if key not in visitedBoxes.copy() and key < numOfBoxes:
                    setOfKeys.update(boxes[key])
                    visitedBoxes.add(key)
                    print(f"set of Keys updated = {setOfKeys}")
                    print(f"visitedBoxes updated = {visitedBoxes}")
                    continue
            terminateLoop = True
        for n in range(numOfBoxes):
            if n not in setOfKeys:
                return False
        return True
    return False
