from sudoku import Sudoku
from ac3 import AC3
from backtrack import recursive_backtrack_algorithm
from utils import fetch_sudokus, print_grid

# AC-3 Solver function for the sudoku puzzle #


class SudokuPuzzleBox:
    def __init__(self, puzzleBox):
        self.puzzleBox = puzzleBox

    def printBox(self):
        num = 0
        for i in self.puzzleBox:
            if num < 3:
                print(i)
            else:
                print()
                num = 0
            num += 1


class SudokuSolver:
    def __init__(self, poggers):
        self.poggers = poggers


def turnToString(puzzle):
    # Accepts a List of strings
    ret = ""
    for lvl in puzzle:
        ret += lvl
    return ret


def solve(grid, index, total):

    print("\nSudoku {}/{} : \n{}".format(index, total, print_grid(grid)))

    print("{}/{} : AC3 starting".format(index, total))

    # instanciate Sudoku
    sudoku = Sudoku(grid)

    # launch AC-3 algorithm of it
    AC3_result = AC3(sudoku)

    # Sudoku has no solution
    if not AC3_result:
        print("{}/{} : this sudoku has no solution".format(index, total))

    else:

        # check if AC-3 algorithm has solve the Sudoku
        if sudoku.isFinished():

            print("{}/{} : AC3 was enough to solve this sudoku !".format(index, total))
            print("{}/{} : Result: \n{}".format(index, total, sudoku))

        # continue the resolution
        else:

            print("{}/{} : AC3 finished, Backtracking starting...".format(index, total))

            assignment = {}

            # for the already known values
            for cell in sudoku.cells:

                if len(sudoku.possibilities[cell]) == 1:
                    assignment[cell] = sudoku.possibilities[cell][0]

            # start backtracking
            assignment = recursive_backtrack_algorithm(assignment, sudoku)

            # merge the computed values for the cells at one place
            for cell in sudoku.possibilities:
                sudoku.possibilities[cell] = assignment[cell] if len(
                    cell) > 1 else sudoku.possibilities[cell]

            if assignment:
                print("{}/{} : Result: \n{}".format(index, total, sudoku))

            else:
                print("{}/{} : No solution exists".format(index, total))
