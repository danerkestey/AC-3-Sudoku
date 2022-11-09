import itertools

ROWS = "123456789"
COLS = "ABCDEFGHI"


class Sudoku:
    def __init__(self, grid):
        # generation of all the coords of the grid
        self.cells = list()
        self.cells = self.genCoords()

        # generation of all the possibilities for each one of these coords
        self.possibilities = dict()
        self.possibilities = self.genPossibilities(grid)

        # generation of the line / row / square constraints
        RULES = self.genRulesConstraints()

        # convertion of these constraints to binary constraints
        self.binaryConstraints = list()
        self.binaryConstraints = self.genBinaryConstraints(
            RULES)

        # generating all constraint-related cells for each of them
        self.related = dict()
        self.related = self.generateRelated()

        # prune
        self.pruned = dict()
        self.pruned = {v: list() if grid[i] == '0' else [
            int(grid[i])] for i, v in enumerate(self.cells)}

    """
    Definition: Function to generate all the coordinates of the cells
    Input:
        None
    Returns:
        A list of all cells in the format [LETTER][NUMBER]
    """

    def genCoords(self):
        coords = []

        # for A,B,C, ... ,H,I
        for col in COLS:

            # for 1,2,3 ,... ,8,9
            for row in ROWS:

                # A1, A2, A3, ... , H8, H9
                new = col + row
                coords.append(new)

        return coords

    """
    Definition: Function to generate all possible values remaining for each cell
    Input:
        grid (string) - the current grid of the puzzle
    Returns:
        possibilities (dictionary) - A hashset of all possibilities for each cell
    """

    def genPossibilities(self, grid):

        grid_as_list = list(grid)

        possibilities = dict()

        for index, coords in enumerate(self.cells):
            # if value is 0, then the cell can have any value in [1, 9]
            if grid_as_list[index] == "0":
                possibilities[coords] = list(range(1, 10))
            # else value is already defined, possibilities is this value
            else:
                possibilities[coords] = [int(grid_as_list[index])]

        return possibilities

    """
    Definition: Function to generates the constraints based on the rules of the game:
                Different values for every row, column and square
    Input:
        None
    Returns:
        list of the row, column and square constraints concatenated
    """

    def genRulesConstraints(self):

        rowConsts = []
        colConsts = []
        squareConsts = []

        # get rows constraints
        for row in ROWS:
            rowConsts.append([col + row for col in COLS])

        # get columns constraints
        for col in COLS:
            colConsts.append([col + row for row in ROWS])

        # get square constraints
        rowSquare = [COLS[i:i+3] for i in range(0, len(ROWS), 3)]

        colSquare = [ROWS[i:i+3] for i in range(0, len(COLS), 3)]

        # for each square
        for row in rowSquare:
            for col in colSquare:

                curr = []

                # and for each value in this square
                for x in row:
                    for y in col:
                        curr.append(x + y)

                squareConsts.append(curr)

        # all constraints is the sum of these 3 rules
        return rowConsts + colConsts + squareConsts

    """
    Definition: Function to generate the binary constraints based on the rule constraints
    Input:
        rules (list) - List of all rules constraints
    Returns:
        genBinConsts (list) - List of all of the binary constraints
    """

    def genBinaryConstraints(self, rules):
        genBinConsts = list()

        for constraint in rules:

            binaryConstraints = list()

            for t in itertools.permutations(constraint, 2):
                binaryConstraints.append(t)

            for c in binaryConstraints:
                constraint_as_list = list(c)
                if(constraint_as_list not in genBinConsts):
                    genBinConsts.append(
                        [c[0], c[1]])

        return genBinConsts

    """
    Definition: Function to generate the constraint-related cell for each one of the coordinates
    Input:
        None
    Returns:
        related (dictionary) - A hashset of all related cells for each cell
    """

    def generateRelated(self):
        related = dict()

        # for each one of the 81 cells
        for cell in self.cells:

            related[cell] = list()

            # related cells are the ones that current cell has constraints with
            for constraint in self.binaryConstraints:
                if cell == constraint[0]:
                    related[cell].append(constraint[1])

        return related

    """
    checks if the Sudoku's solution is finished
    we loop through the possibilities for each cell
    if all of them has only one, then the Sudoku is solved
    """

    def isFinished(self):
        for _, possibilities in self.possibilities.items():
            if len(possibilities) > 1:
                return False

        return True

    """
    returns a human-readable string
    """

    def __str__(self):

        output = ""
        for v in self.possibilities:
            if len(self.possibilities[v]) > 1:
                output += "0"
            else:
                output += str(self.possibilities[v][0])

        return output
