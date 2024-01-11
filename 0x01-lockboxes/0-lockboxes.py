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
                print(key)
                setOfKeys.add(key)
        print(setOfKeys)
        for n in range(numOfBoxes):
            if n not in setOfKeys:
                return False
        return True
