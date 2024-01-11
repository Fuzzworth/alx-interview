#!/usr/bin/python3
'''
Module Docs
'''


def canUnlockAll(boxes):
    '''
    Function Docs
    '''
    if (boxes):
        numOfBoxes = len(boxes)
        setOfKeys = {0}
        for box in boxes:
            for key in box:
                result = setOfKeys.add(key)
        for n in range(numOfBoxes):
            if n not in setOfKeys:
                return False
        return True
