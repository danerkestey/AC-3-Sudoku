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
    [gui.Submit(), gui.Button('Exit', button_color=('white', 'grey')), gui.Button('DefaultGame', button_color=('white', 'teal'))]]


window = gui.Window('--Sudoku Puzzle Solver--', layout, element_justification='c')

while True:
    event, values = window.read()
    
    if event in (None, 'Exit'):
        break
    else:
        print('hi')

window.close()


print(values[0])
box1 = SudokuPuzzleBox([[values[0][1] for i in range(0,3)], [values[1] for i in range(0,3)], [values[2] for i in range(0,3)]])
box1.printBox()


#SudokuSolver()


print(event, values[0], values[1], values[2] ,values[3])


