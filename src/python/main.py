#Sodoku Solver Main & Utils

import PySimpleGUI as gui
from solver import SudokuSolver, SudokuPuzzleBox

gui.theme('GrayGrayGray')

layout = [ 
    [gui.Text('Please enter the puzzle to solve!!!')],
    [gui.Text('A', size = (0, 0)), gui.InputText()],
    [gui.Text('B', size = (0, 0)), gui.InputText()],
    [gui.Text('C', size =(0, 0)), gui.InputText()],
    [gui.Text('D', size =(0, 0)), gui.InputText()],
    [gui.Text('E', size =(0, 0)), gui.InputText()],
    [gui.Text('F', size =(0, 0)), gui.InputText()],
    [gui.Text('G', size =(0, 0)), gui.InputText()],
    [gui.Text('H', size =(0, 0)), gui.InputText()],
    [gui.Text('I ', size =(0, 0)), gui.InputText()],
    [gui.Submit(), gui.Cancel()]]


window = gui.Window('--Sudoku Puzzle Solver--', layout, element_justification='c')
event, values = window.read()
window.close()



box1 = new SudokuPuzzleBox()


SudokuSolver()


print(event, values[0], values[1], values[2] ,values[3])


