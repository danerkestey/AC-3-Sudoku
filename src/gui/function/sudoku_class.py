import itertools

rows = "123456789"
cols = "ABCDEFGHI"


class Sudoku:
    def __init__(self, grid):
        game = list(grid)

        # generation of all the coords of the grid
        self.cells = list()
        self.cells = self.generate_coords()

        # generation of all the possibilities for each one of these coords
        self.possibilities = dict()
        self.possibilities = self.generate_possibilities(grid)

        # generation of the line / row / square constraints
        rule_constraints = self.generate_rules_constraints()

        # convertion of these constraints to binary constraints
        self.binary_constraints = list()
        self.binary_constraints = self.generate_binary_constraints(
            rule_constraints)

        # generating all constraint-related cells for each of them
        self.related_cells = dict()
        self.related_cells = self.generate_related_cells()

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

    def generate_coords(self):
        all_cells_coords = []

        # for A,B,C, ... ,H,I
        for col in cols:

            # for 1,2,3 ,... ,8,9
            for row in rows:

                # A1, A2, A3, ... , H8, H9
                new_coords = col + row
                all_cells_coords.append(new_coords)

        return all_cells_coords

    """
    Definition: Function to generate all possible values remaining for each cell
    Input:
        grid (string) - the current grid of the puzzle
    Returns:
        possibilities (dictionary) - A hashset of all possibilities for each cell
    """

    def generate_possibilities(self, grid):

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

    def generate_rules_constraints(self):

        row_constraints = []
        column_constraints = []
        square_constraints = []

        # get rows constraints
        for row in rows:
            row_constraints.append([col + row for col in cols])

        # get columns constraints
        for col in cols:
            column_constraints.append([col + row for row in rows])

        # get square constraints
        rows_square_coords = [cols[i:i+3] for i in range(0, len(rows), 3)]

        cols_square_coords = [rows[i:i+3] for i in range(0, len(cols), 3)]

        # for each square
        for row in rows_square_coords:
            for col in cols_square_coords:

                current_square_constraints = []

                # and for each value in this square
                for x in row:
                    for y in col:
                        current_square_constraints.append(x + y)

                square_constraints.append(current_square_constraints)

        # all constraints is the sum of these 3 rules
        return row_constraints + column_constraints + square_constraints

    """
    Definition: Function to generate the binary constraints based on the rule constraints
    Input:
        rules_constraints (list) - List of all rules constraints
    Returns:
        generated_binary_constraints (list) - List of all of the binary constraints
    """

    def generate_binary_constraints(self, rule_constraints):
        generated_binary_constraints = list()

        # for each set of constraints
        for constraint_set in rule_constraints:

            binary_constraints = list()

            # 2 because we want binary constraints
            # solution taken from :
            # https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements

            # for tuple_of_constraint in itertools.combinations(constraint_set, 2):
            for tuple_of_constraint in itertools.permutations(constraint_set, 2):
                binary_constraints.append(tuple_of_constraint)

            # for each of these binary constraints
            for constraint in binary_constraints:

                # check if we already have this constraint saved
                # = check if already exists
                # solution from https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list
                constraint_as_list = list(constraint)
                if(constraint_as_list not in generated_binary_constraints):
                    generated_binary_constraints.append(
                        [constraint[0], constraint[1]])

        return generated_binary_constraints

    """
    Definition: Function to generate the constraint-related cell for each one of the coordinates
    Input:
        None
    Returns:
        related_cells (dictionary) - A hashset of all related cells for each cell
    """

    def generate_related_cells(self):
        related_cells = dict()

        # for each one of the 81 cells
        for cell in self.cells:

            related_cells[cell] = list()

            # related cells are the ones that current cell has constraints with
            for constraint in self.binary_constraints:
                if cell == constraint[0]:
                    related_cells[cell].append(constraint[1])

        return related_cells

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
