import re

"""
is_different
checks if two cells are the same
"""


def is_different(cell_i, cell_j):
    result = cell_i != cell_j
    return result


def ONLY_DIGIT(e):
    if len(e) <= 2:
        if re.match(r"(\d).", e):
            return False
        if re.match(r"( (\d)|(\d)|(\d) )", e):
            return True
        elif e == " ":
            return True
        elif e == "":
            return True
        else:
            return False
    else:
        return False


def getColorPos(x, y) -> set:
    pos = set()

    # Add row indexs
    for i in range(9):
        pos.add((x, i))

    # Add columns indexs
    for i in range(9):
        pos.add((i, y))

    # Add box indexs
    box_x = x // 3
    box_y = y // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            pos.add((j, i))

    return pos
