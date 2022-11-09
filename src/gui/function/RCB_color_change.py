from src.gui.style.entry_color_change import *
from .utils import *

'''
    { R : Row, C : Column, B : Box }

    Change color of Row, Column, and Box
    Use by : src\\gui\\sudoku_gui.py
'''

"""
Definition: Function to highlight color of the selected cell
    Input:
        readonlyBoard (list) - The display board
        x (int) - x position of the entry
        y (int) - y position of the entry
    Returns:
        None
"""


def changeColor(entryList, readonlyBoard, x, y):
    # Get all color indices
    POS = getColorPos(x, y)

    for _ in range(len(POS)):
        pos = POS.pop()

        if readonlyBoard[pos[0]][pos[1]]:
            readonlyToLightBlue(entryList[pos[0]][pos[1]])
        else:
            backgroundToLightBlue(entryList[pos[0]][pos[1]])

    # Change current selected color
    if readonlyBoard[x][y]:
        readonlyToBlue(entryList[x][y])
    else:
        backgroundToBlue(entryList[x][y])


"""
Definition: Function to remove highlight color of the previous selection
    Input:
        readonlyBoard (list) - The display board
        x (int) - x position of the entry
        y (int) - y position of the entry
    Returns:
        None
"""


def resetColor(entryList, readonlyBoard, x, y):
    # Get all color indices
    POS = getColorPos(x, y)

    for _ in range(len(POS)):
        pos = POS.pop()

        if readonlyBoard[pos[0]][pos[1]]:
            readonlyToWhite(entryList[pos[0]][pos[1]])
        else:
            backgroundToWhite(entryList[pos[0]][pos[1]])
