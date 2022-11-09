from src.gui.function.ac3 import AC3
from src.gui.function.sudoku_class import Sudoku


def turnBoardToString(bo):
    string = ""
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            string += str(bo[i][j])
    return string


def turnStringToBoard(string):
    board = []
    k = 9

    for i in range(len(string)):
        if i % k == 0:
            sub = string[i:i+k]
            lst = []
            for j in sub:
                lst.append(int(j))
            board.append(lst)
    return board


def getHintBoard(gameBoard, originalBoard, hintBoard):
    for i in range(len(hintBoard)):
        for j in range(len(hintBoard[0])):
            if gameBoard[i][j] != originalBoard[i][j]:
                hintBoard[i][j] = 0
    return hintBoard.copy()


"""
Definition: Function to solve the Sudoku problem using backtracking
    Input:
        board (list) - Current arc-consistent instance of the Sudoku puzzle
    Returns:
        Whether or not the puzzle was solved
"""


def solve(board):
    # Solves by backtracking
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


"""
Definition: Function to check if a current cell is valid
    Input:
        board (list) - Current arc-consistent instance of the Sudoku puzzle
        num (int) - Current value in the board
        pos (list) - Tuple representing the position of the number
    Returns:
        Whether or not the cell is valid
"""


def valid(board, num, pos):
    # Check if the position is consistent in the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check if the position is consistent in the column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check if the position is consistent in the square
    squareX = pos[1] // 3
    squareY = pos[0] // 3

    for i in range(squareY * 3, squareY * 3 + 3):
        for j in range(squareX * 3, squareX * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


"""
Definition: Function to find the first empty position
    Input:
        board (list) - Current arc-consistent instance of the Sudoku puzzle
    Returns:
        (i, j) - Position of the first empty cell
"""


def findEmpty(board):
    for i, b in enumerate(board):
        for j in range(len(b)):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None
