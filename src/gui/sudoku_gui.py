import tkinter as tk
import numpy as np

from .style._style import STYLE
from .style.entry_color_change import board_fg_to_blue

from .function.utils import *
from .function.RCB_color_change import *
from .function.generate_game import genGame
from .function.entry_operations import (
    updateBoard,
    formatValue,
    delete_value,
    restart_board,
    clear_all_board,
    collect_entry_values)
from .function.valid_entry_color_change import isValid
from .function.speed_visual_solve import *


class GUI(STYLE):
    def __init__(self, _master):
        super().__init__()

        # root Window
        self._master = _master

        # Game Board Entry boxes
        self.entryList = [[" " for i in range(9)] for j in range(9)]

        # Game Boards
        self.gameBoard = None
        self.readonlyBoard = np.zeros((9, 9), dtype=int)
        self.solvedBoard = None

        # Entry Queue
        self.entryQueue = []

        # Current Selected Position by User
        self.c_pos_x = None
        self.c_pos_y = None

        # Permission
        self.isClear = True
        self.visualRunning = False

        # Register new Function
        self.only_digit = self._master.register(ONLY_DIGIT)

        # Is Running
        self.running = False

    # bind function with input boxes to update current position

    def start_running(self):
        self.running = True

    def stop_running(self):
        self.running = False

    def updateCurrPos(self, x, y):
        self.c_pos_x = x
        self.c_pos_y = y

    """
    Definition: Function to generate an empty board
        Input:
            None
        Returns:
            None
    """

    def generateEmptyBoard(self):
        boardFrame = tk.Frame(self._master)
        boardFrame.grid(row=0, column=0, pady=2)

        # Defines the space between the rows/columns, we want a larger space after 3 boxes
        rowsCount = 0
        for i in range(9):
            colsCount = 0
            for j in range(9):
                # Add space between the rows or columns when the current cell is the 4th one
                if (rowsCount + 1) % 4 == 0 and rowsCount != 0:
                    canvas = tk.Canvas(boardFrame, width=1,
                                       height=1, bg="white")
                    canvas.grid(row=rowsCount, column=colsCount)
                    rowsCount += 1

                if (colsCount + 1) % 4 == 0 and colsCount != 0:
                    canvas = tk.Canvas(boardFrame, width=1,
                                       height=1, bg="white")
                    canvas.grid(row=rowsCount, column=colsCount)
                    colsCount += 1

                # Define the input boxes
                entry = tk.Entry(
                    boardFrame,
                    width=2,
                    font=("Helvetica", 30),
                    bg="white",
                    relief="ridge",
                    validate="key",
                    validatecommand=(self.only_digit, '%P'))

                entry.grid(row=rowsCount, column=colsCount)

                # Update the current position of the cell when the user clicks on the box
                entry.bind("<Button-1>", lambda e=None, x=i,
                           y=j: self.entryOnLeftClick(x, y))
                entry.bind("<Button-2>", lambda e=None, x=i,
                           y=j: self.entryOnRightClick(x, y))

                entry.insert(0, " ")
                colsCount += 1
                # Update the entries with the user input
                self.entryList[i][j] = entry
            rowsCount += 1

    """
    Definition: Function to generate the right side panel
        Input:
            None
        Returns:
            None
    """

    def rightPanel(self):

        # Define the right-side panel frame
        panelFrame = tk.Frame(self._master, bg="white")

        # Define GUI for the Title
        title = tk.Frame(panelFrame, bg="white")
        titleLabel = tk.Label(title,
                              text="SUDOKU",
                              fg=self.Option_title["fg"],
                              bg=self.Option_title["bg"],
                              font=self.Option_title["font"]
                              )
        titleLabel.grid(row=0, column=0)
        title.grid(row=0, column=0)

        option = tk.Frame(panelFrame, bg="white")

        # Define the buttons for a random new new game
        newGame = tk.LabelFrame(option, text="  NEW GAME ")
        self.OptionFrameAddStyle(newGame)

        # Button to create an easy game
        easyGame = tk.Button(newGame, text="Easy",
                             command=lambda: self.gameGenerationAction(41))

        self.OptionButtonAddStyle(easyGame)  # Add styles to button

        easyGame.grid(row=0, column=0, padx=self.optionButtonPadX,
                      pady=self.optionButtonPadY)

        # Button to create a hard game
        hardGame = tk.Button(newGame, text="Hard",
                             command=lambda: self.gameGenerationAction(56))

        self.OptionButtonAddStyle(hardGame)  # Add styles to button

        hardGame.grid(row=0, column=1, padx=self.optionButtonPadX,
                      pady=self.optionButtonPadY)

        newGame.grid(row=0, column=0, pady=self.optionFramePadY)

        # Defines GUI to clear the game
        clear = tk.LabelFrame(option, text="  CLEAR  ")
        self.OptionFrameAddStyle(clear)

        # Button to restart the game
        restartGame = tk.Button(
            clear, text="Restart", command=self.restartAction)

        self.OptionButtonAddStyle(restartGame)  # Add styles to the button

        restartGame.grid(
            row=0, column=0, padx=self.optionButtonPadX, pady=self.optionButtonPadY)

        # Button to clear the game
        clearGame = tk.Button(
            clear, text="Clear All", command=self.clearAction)

        self.OptionButtonAddStyle(clearGame)  # Add styles to the button

        clearGame.grid(
            row=0, column=1, padx=self.optionButtonPadX, pady=self.optionButtonPadY)

        clear.grid(row=1, column=0, pady=self.optionFramePadY)

        # Define GUI to solve the game
        solve = tk.LabelFrame(option, text="  SOLVE  ")
        self.OptionFrameAddStyle(solve)

        # Button to solve the game in a visual iteration
        visual = tk.Button(solve, text="Visual",
                           command=lambda: self.speed_visual_solve_button_action(True))

        self.OptionButtonAddStyle(visual)  # Add styles to the button

        visual.grid(
            row=0, column=0, padx=self.optionButtonPadX, pady=self.optionButtonPadY)

        # Button to solve the game instantaneously
        speed = tk.Button(solve, text="Speed",
                          command=lambda: self.speed_visual_solve_button_action(False))

        self.OptionButtonAddStyle(speed)  # Add styles to the button

        speed.grid(
            row=0, column=1, padx=self.optionButtonPadX, pady=self.optionButtonPadY)

        solve.grid(row=2, column=0, pady=self.optionFramePadY)

        # Define the GUI for the AC-3 CSP preprocessing
        csp = tk.LabelFrame(option, text="  AC3  ")
        self.OptionFrameAddStyle(csp)

        # Button to run the AC-3 Algorithm
        ac3 = tk.Button(csp, text="AC3",
                        command=lambda: self.ac3_action())

        self.OptionButtonAddStyle(ac3)  # Add styles to the button

        ac3.grid(
            row=0, column=0, padx=self.optionButtonPadX, pady=self.optionButtonPadY)

        csp.grid(row=3, column=0, pady=self.optionFramePadY)
        option.grid(row=1, column=0)
        panelFrame.grid(row=0, column=1, padx=10)

    """
    Definition: Function to define actions to perform when user left clicks
        Input:
            x (int) - x position of the entry
            y (int) - y position of the entry
        Returns:
            None
    """

    def entryOnLeftClick(self, x, y):
        if not self.visualRunning:
            # Add current position to the entryQueue
            self.addToQueue(x, y)

            # update current position to be the passed in coordinate
            self.updateCurrPos(x, y)

            # Remove the highlight from the previously selected cell
            if len(self.entryQueue) == 2:
                entry = self.entryList[self.entryQueue[0]
                                       [0]][self.entryQueue[0][1]]

                formatValue(entry)

                # Reset the previously selected cell
                resetColor(self.entryList, self.readonlyBoard,
                           self.entryQueue[0][0], self.entryQueue[0][1])

                # If the current input is wrong, change the text colour to red
                if self.solvedBoard is not None:
                    isValid(
                        entry, self.solvedBoard[self.entryQueue[0][0]][self.entryQueue[0][1]])

            # Highlight the current cell
            changeColor(self.entryList, self.readonlyBoard, x, y)

    def entryOnRightClick(self, x, y):
        # remove value of current cell
        delete_value(self.entryList[x][y])

    """
    Definition: Function to randomly generate a game
        Input:
            dif (int) - The difficulty of the game selected
        Returns:
            None
    """

    def gameGenerationAction(self, dif):
        if not self.running:
            # Update global boards with the new board
            self.gameBoard, self.solvedBoard, self.readonlyBoard = genGame(
                dif)

            # Insert Values in the GUI
            updateBoard(self.gameBoard, self.entryList)

            self.isClear = False
            self.entryQueue.clear()

    def restartAction(self):
        # Stop Visual Solving
        stop_solving()

        # Just remove user input values not readonly ones
        restart_board(self.gameBoard, self.entryList)

    def clearAction(self):
        # Stop Visual Solving
        stop_solving()

        # clear all game
        clear_all_board(self.gameBoard, self.entryList)

        # reset all boards fill with 0
        self.gameBoard = None
        self.readonlyBoard = np.zeros((9, 9), dtype=int)
        self.solvedBoard = None

        self.isClear = True
        self.entryQueue.clear()

    def ac3_action(self):
        grid = turnBoardToString(self.gameBoard)
        sudoku = Sudoku(grid)
        AC3_result = AC3(sudoku)

        if not AC3_result:
            print("Board has no solution")
        else:
            if sudoku.isFinished():
                print("AC3 was enough to solve this sudoku!")
            else:
                print(
                    "AC3 was not enough to solve this problem on its own, starting backtracking!")

        preprocessed = turnStringToBoard(str(sudoku))
        self.solvedBoard = getHintBoard(
            preprocessed,
            self.gameBoard,
            self.solvedBoard
        )
        self.gameBoard = preprocessed.copy()

        update_values(
            self.gameBoard,
            self.entryList,
            True
        )

        self.isClear = False

        # clear Queue
        self.entryQueue.clear()

    # +---------------------------------------------+
    # |         Speed & Visual Solve Action         |
    # +---------------------------------------------+

    def speed_visual_solve_button_action(self, is_visual):
        # if visual call and virual solve already running then it return
        if is_visual and self.running:
            return

        # running -> True | if visual call
        if is_visual:
            self.start_running()

        self.visualRunning = True

        # Game Not Generate collect values from input box
        if self.isClear:
            board = collect_entry_values(self.entryList)
            self.gameBoard = board.copy()
        else:
            # copy current generated board
            board = self.gameBoard.copy()

        b = board.copy()

        # setup environment
        setup_visual_solve(self._master, self.entryList,
                           self.solvedBoard, self.isClear, is_visual)

        # Solving
        speed_visual_solve(board)

        # visual call then current selected cell to blue
        if is_visual:
            board_fg_to_blue(self.entryList, self.gameBoard)

        # delete temp boards
        del b, board

        self.visualRunning = False

        # running -> False | if visual call
        if is_visual:
            self.stop_running()

    # FILO to store last clicked entry
    def addToQueue(self, x, y):
        if len(self.entryQueue) == 2:
            self.entryQueue.pop(0)
        self.entryQueue.append([x, y])
