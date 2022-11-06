# AC-3 Solver function for the sudoku puzzle #

class SudokuPuzzleBox:
    def __init__(self, puzzleBox):
        self.puzzleBox = puzzleBox

    def turnTo2DList(puzzle):
        # Accepts a List of strings
        ret = []
        for lvl in puzzle:
            temp = []
            for c in lvl:
                temp.append(int(c))
            ret.append(temp)
        return ret

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
