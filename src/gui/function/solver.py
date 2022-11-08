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


def solve(bo):
    # Solves by backtracking
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
