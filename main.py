# Sodoku Solver Main & Utils

import PySimpleGUI as gui
from solver import SudokuSolver, SudokuPuzzleBox


def buildPuzzle(values):
    puzzle = [['0'] * 9 for _ in range(9)]

    for i in range(9):
        row = values[i]

        for j in range(9):
            puzzle[i][j] = row[j]

    return puzzle


gui.theme('GrayGrayGray')

layout = [
    [gui.Text('Please enter the puzzle to solve!!!')],
    [gui.Text('A', size=(0, 0)), gui.InputText()],
    [gui.Text('B', size=(0, 0)), gui.InputText()],
    [gui.Text('C', size=(0, 0)), gui.InputText()],
    [gui.Text('D', size=(0, 0)), gui.InputText()],
    [gui.Text('E', size=(0, 0)), gui.InputText()],
    [gui.Text('F', size=(0, 0)), gui.InputText()],
    [gui.Text('G', size=(0, 0)), gui.InputText()],
    [gui.Text('H', size=(0, 0)), gui.InputText()],
    [gui.Text('I ', size=(0, 0)), gui.InputText()],
    [gui.Submit(), gui.Button('Exit', button_color=('white', 'grey')), gui.Button('DefaultGame', button_color=('white', 'teal'))]]


window = gui.Window('--Sudoku Puzzle Solver--',
                    layout, element_justification='c')

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break
    else:
        puzzle = buildPuzzle(values)
        print(puzzle)


window.close()
