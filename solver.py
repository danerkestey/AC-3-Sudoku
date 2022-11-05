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
            num+=1

class SudokuSolver:
    def __init__(self, poggers):
        self.poggers = poggers