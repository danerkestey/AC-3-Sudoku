from itertools import permutations as perm

ROWS = "123456789"
COLS = "ABCDEFGHI"


class Sudoku:
    def __init__(self, grid):
        self.cells = self.genCoords()

        self.domain = self.genDomain(grid)

        RULES = self.genRulesConstraints()
        self.binaryConstraints = self.genBinaryConstraints(
            RULES)

        self.related = self.generateRelated()

    """
    Definition: Function to generate all the coordinates of the cells
    Input:
        None
    Returns:
        A list of all cells in the format [LETTER][NUMBER]
    """

    def genCoords(self):
        coords = []

        for col in COLS:
            for row in ROWS:
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

    def genDomain(self, grid):

        grid_as_list = list(grid)

        possibilities = dict()

        for index, coords in enumerate(self.cells):
            if grid_as_list[index] == "0":
                possibilities[coords] = list(range(1, 10))
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

        # Get all of the row constraints
        for row in ROWS:
            rowConsts.append([col + row for col in COLS])

        # Get all of the column constraints
        for col in COLS:
            colConsts.append([col + row for row in ROWS])

        # Get all of the square constraints
        rowSquare = [COLS[i:i+3] for i in range(0, len(ROWS), 3)]
        colSquare = [ROWS[i:i+3] for i in range(0, len(COLS), 3)]

        for row in rowSquare:
            for col in colSquare:
                curr = []
                for x in row:
                    for y in col:
                        curr.append(x + y)
                squareConsts.append(curr)

        # Return the concatenation of all 3 constraints
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

            # Get all 2-set permutations of the constraint
            for t in perm(constraint, 2):
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
        for _, possibilities in self.domain.items():
            if len(possibilities) > 1:
                return False

        return True

    """
    returns a human-readable string
    """

    def __str__(self):

        output = ""
        for v in self.domain:
            if len(self.domain[v]) > 1:
                output += "0"
            else:
                output += str(self.domain[v][0])

        return output
