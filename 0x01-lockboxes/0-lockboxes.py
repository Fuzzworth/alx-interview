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
            for key in setOfKeys:
                if key not in visitedBoxes and key < numOfBoxes:
                    setOfKeys.update(boxes[key])
                    visitedBoxes.add(key)
                    continue
            terminateLoop = True
            print(setOfKeys)
            for n in range(numOfBoxes):
                if n not in setOfKeys:
                    return False
            return True
    return False
