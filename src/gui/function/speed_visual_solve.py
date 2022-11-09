from time import sleep

from .solver import *
from .entry_operations import (
    insertValue,
    deleteValue,
    updateValues)

from src.gui.style.entry_color_change import (
    backgroundToRed,
    backgroundToGreen,
    textToWhite
)

IS_CLEAR = None
IS_VISUAL = None
SOLVED_BOARD = None
ENTRY_LIST = None
MASTER = None
RUN = True

selectTime = 0.00
greenTime = 0.05
redTime = 0.04


def stop_solving():
    global RUN
    RUN = False


"""
Definition: Function to set up global values for the boards and other attributes
    Input:
        master - The master GUI frame
        entryList - The current values entered into the puzzle
        solvedBoard - The solution board
        isClear - Whether or not the board should be emptied
        isVisual (boolean) - Whether the solve is visual or instantaneous
    Returns:
        None
"""


def setupVisualSolve(master, entryList, solvedBoard, isClear, isVisual):
    global IS_CLEAR, IS_VISUAL, SOLVED_BOARD, ENTRY_LIST, MASTER, RUN

    IS_CLEAR = isClear
    IS_VISUAL = isVisual
    SOLVED_BOARD = solvedBoard
    ENTRY_LIST = entryList
    MASTER = master
    RUN = True


"""
Definition: Function to solve the puzzle and update the GUI
    Input:
        board - The current board to solve
    Returns:
        None
"""


def speedSolve(board):
    # If the game will be solved instantly and the user entered values,
    # find the solution and update the GUI with it
    if not IS_VISUAL and IS_CLEAR:
        solve(board)
        updateValues(board, ENTRY_LIST)
        return

    # If the game will be solved instantly and the game was generated,
    # update the GUI with the solved board
    if not IS_VISUAL:
        updateValues(SOLVED_BOARD, ENTRY_LIST)

    # Visual Solve
    if IS_VISUAL:
        find = findEmpty(board)

        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):

            if IS_VISUAL and RUN:   # select
                backgroundToRed(ENTRY_LIST[row][col])
                textToWhite(ENTRY_LIST[row][col])
                deleteValue(ENTRY_LIST[row][col])
                insertValue(ENTRY_LIST[row][col], i)
                MASTER.update()
                sleep(selectTime)

            if valid(board, i, (row, col)):

                if IS_VISUAL and RUN:   # green / valid
                    backgroundToGreen(ENTRY_LIST[row][col])
                    deleteValue(ENTRY_LIST[row][col])
                    insertValue(ENTRY_LIST[row][col], i)
                    MASTER.update()
                    sleep(greenTime)

                board[row][col] = i

                if speedSolve(board):
                    updateValues(SOLVED_BOARD, ENTRY_LIST)
                    return True

                board[row][col] = 0

                if IS_VISUAL and RUN:
                    backgroundToRed(ENTRY_LIST[row][col])
                    textToWhite(ENTRY_LIST[row][col])
                    deleteValue(ENTRY_LIST[row][col])
                    insertValue(ENTRY_LIST[row][col], 0)
                    MASTER.update()
                    sleep(redTime)

        return False
