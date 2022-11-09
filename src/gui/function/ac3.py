from src.gui.function.utils import isDifferent

"""
Definition: AC-3 Implementation for maintaining Arc Consistency
    Input:
        csp (Sudoku) - Current CSP definition of the Sudoku puzzle
    Returns:
        Whether or not the current problem is arc-consistent
"""


def AC3(csp):

    queue = list(csp.binaryConstraints)

    while queue:
        print(f"The queue length is: {len(queue)}")
        (cell1, cell2) = queue.pop(0)

        if removeInconsistentVals(csp, cell1, cell2):

            # if a cell has 0 possibilities, sudoku has no solution
            if len(csp.possibilities[cell1]) == 0:
                return False

            for cell in csp.related[cell1]:
                if cell != cell1:
                    queue.append((cell, cell1))

    return True


"""
Definition: Helper function to remove inconsistent values
    Input:
        csp (Sudoku) - Current CSP definition of the Sudoku puzzle
        cell1 (string) - The cell to check its possibilities
        cell2 (string) - The cell to check conflict with
    Returns:
        Whether or not a value has been removed
"""


def removeInconsistentVals(csp, cell1, cell2):
    removed = False

    # for each possible value remaining for the cell1 cell
    for value in csp.possibilities[cell1]:

        # if cell1's value is in conflict with cell2's possibilities for each possibility
        if not any([isDifferent(value, poss) for poss in csp.possibilities[cell2]]):

            # then remove cell1's value
            csp.possibilities[cell1].remove(value)
            removed = True

    return removed
