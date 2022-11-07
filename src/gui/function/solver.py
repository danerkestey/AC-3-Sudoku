from src.gui.function.ac3 import AC3
from src.gui.function.sudoku_class import Sudoku


def turnBoardToString(bo):
    string = ""
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            string += str(bo[i][j])
    return string


def turnStringToBoard(string):
    bo = []
    k = 9

    print(string)
    for i in range(len(string)):
        if i % k == 0:
            sub = string[i:i+k]
            lst = []
            for j in sub:
                print(j)
                lst.append(int(j))
            bo.append(lst)
    return bo


def solve(bo):
    grid = turnBoardToString(bo)
    print(bo)
    print(grid)
    print("----------")
    sudoku = Sudoku(grid)
    AC3_result = AC3(sudoku)

    if not AC3_result:
        print("Board has no solution")
        return False
    else:
        if sudoku.isFinished():
            print("AC3 was enough to solve this sudoku!")
            return True
        else:
            preprocessed = turnStringToBoard(str(sudoku))
            backTrack(preprocessed)


def backTrack(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if backTrack(bo):
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
