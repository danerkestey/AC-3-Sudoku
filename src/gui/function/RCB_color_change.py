from src.gui.style.entry_color_change import *
from .utils import *

'''
    { R : Row, C : Column, B : Box }

    Change color of Row, Column, and Box
    Use by : src\\gui\\sudoku_gui.py
'''

# Highlight RCB as per current selection


def change_RCB_color(entryList, readonlyBoard, x, y):
    # POS - all RCB indexs
    _POS = getColorPos(x, y)

    for i in range(len(_POS)):
        POS = _POS.pop()

        if readonlyBoard[POS[0]][POS[1]]:
            readonly_bg_to_lightblue(entryList[POS[0]][POS[1]])
        else:
            bg_to_lightblue(entryList[POS[0]][POS[1]])

    # change current selected color
    if readonlyBoard[x][y]:
        readonly_bg_to_blue(entryList[x][y])
    else:
        bg_to_blue(entryList[x][y])


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
