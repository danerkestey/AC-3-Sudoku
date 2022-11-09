import re
import numpy as np
from src.gui.style.entry_color_change import (
    backgroundToWhite,
    readonlyToWhite,
    fg_to_blue,
    reset_fg_to_black
)

# entry to read only mode


def read_only_mode(entry):
    entry.config(
        state='readonly',
        readonlybackground='white'
    )

# entry to normal mode


def normal_mode(entry):
    entry.config(
        state='normal'
    )


# delete value from entry
def delete_value(entry):
    entry.delete(0, 'end')

# insert value in entry


def insert_value(entry, n):
    entry.insert(0, " {}".format(n))

# format value "5" -> " 5"


def formatValue(entry):
    VALUE = entry.get()

    if re.match(r"(\d)", VALUE):
        delete_value(entry)
        insert_value(entry, VALUE)


# insert values in gui with readonly mode
def updateBoard(board, entryList):
    for i in range(9):
        for j in range(9):
            entry = entryList[i][j]

            normal_mode(entry)

            delete_value(entry)

            # readonly mode
            if board[i][j] > 0:
                insert_value(entry, board[i][j])
                read_only_mode(entry)
                readonlyToWhite(entry)
                reset_fg_to_black(entry)
            else:
                fg_to_blue(entry)
                backgroundToWhite(entry)


# write values in gui of hint_board
#   Speed solve
def updateValues(hint_board, entryList, isAC3=False):
    for i in range(9):
        for j in range(9):
            entry = entryList[i][j]

            # not in readonly mode
            if hint_board[i][j] > 0:
                delete_value(entry)
                insert_value(entry, hint_board[i][j])
                if isAC3:
                    reset_fg_to_black(entry)
                else:
                    fg_to_blue(entry)
                    backgroundToWhite(entry)


# delete all values from gui
# not disabled ones
def restart_board(board, entryList):

    for i in range(9):
        for j in range(9):

            if board is None:
                delete_value(entryList[i][j])
            elif board[i][j] == 0:
                delete_value(entryList[i][j])


# Clear all values from gui
# with disabled ones
def clear_all_board(board, entryList):
    for i in range(9):
        for j in range(9):
            entry = entryList[i][j]

            if board is not None:
                if board[i][j] > 0:
                    normal_mode(entry)

            delete_value(entry)
            fg_to_blue(entry)
            backgroundToWhite(entry)


# collect entry values from gui
#   for speed_visual_solve
def collect_entry_values(entryList):

    board = np.zeros((9, 9), dtype=int)

    for i in range(9):
        for j in range(9):
            formatValue(entryList[i][j])
            VALUE = entryList[i][j].get()
            try:
                board[i][j] = int(VALUE)
            except:
                pass
    return board
