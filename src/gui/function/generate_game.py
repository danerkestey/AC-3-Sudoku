import numpy as np
from random import sample
from .solver import *

# Game Possible : 362880

"""
Definition: Function to randomly generate a game
    Input:
        dif (int) - The difficulty of the game selected
    Returns:
        None
"""


def genGame(dif):

    # Define an empty board
    board = np.zeros((9, 9), dtype=int)

    # Define an empty solved board (will be updated with values)
    solvedBoard = np.zeros((9, 9), dtype=int)

    # Add random number to first row
    board[0] = sample(range(1, 10), 9)

    # Solve the Board
    solve(board)

    # Convert the boards to a 1D array
    board = board.flatten()
    solvedBoard = solvedBoard.flatten()

    # Remove values as per dificulty
    for i in sample(range(81), dif):
        solvedBoard[i] = board[i]
        board[i] = 0

    # Reshape the 1D array to a 2D matrix
    board = np.reshape(board, (9, 9))
    solvedBoard = np.reshape(solvedBoard, (9, 9))

    # Add False where value 0
    readOnlyBoard = np.not_equal(board, 0)

    return board, solvedBoard, readOnlyBoard
