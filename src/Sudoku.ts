import { getPermutations, range } from "./utils";

const rows: string = "123456789",
  cols: string = "ABCDEFGHI";

export class Sudoku {
  cells: any[] = [];
  possibilities: any = {};
  rule_constraints: any[] = [];
  binary_constraints: any[] = [];
  related_cells: any = {};
  pruned: any = {};

  constructor(grid: string) {
    this.cells = this.generateCoords();
    this.possibilities = this.generate_possibilities(grid);
    this.rule_constraints = this.generate_rules_constraints();
    this.binary_constraints = this.generate_binary_constraints(
      this.rule_constraints
    );
  }

  generateCoords() {
    const all_cells_coords: string[] = [];
    for (const c of cols) {
      for (const r of rows) {
        const newCoords = r + c;
        all_cells_coords.push(newCoords);
      }
    }
    return all_cells_coords;
  }

  generate_possibilities(grid: string) {
    const gridList: string[] = grid.split(",");
    const possibilities = {};

    this.cells.forEach((value, index) => {
      if (gridList[index] === "0") {
        possibilities[value] = [range(1, 10)];
      } else {
        possibilities[value] = [parseInt(gridList[index])];
      }
    });

    return possibilities;
  }

  generate_rules_constraints() {
    const row_constraints: string[][] = [];
    const column_constraints: string[][] = [];
    const square_constraints: string[][] = [];

    // Get Row Constraints
    for (const r of rows) {
      const temp = [];
      for (const c of cols) {
        temp.push(r + c);
      }
      row_constraints.push(temp);
    }

    // Get Cols Constraints
    for (const c of cols) {
      const temp = [];
      for (const r of rows) {
        temp.push(r + c);
      }
      column_constraints.push(temp);
    }

    // Get Square Constraints
    const rows_square_coords = [];
    for (let i = 0; i < rows.length; i += 3) {
      const temp = [cols[i], cols[i + 1], cols[i + 2]];
      rows_square_coords.push(temp);
    }

    const cols_square_coords: string[][] = [];
    for (let i = 0; i < cols.length; i += 3) {
      const temp = [rows[i], rows[i + 1], rows[i + 2]];
      cols_square_coords.push(temp);
    }

    rows_square_coords.forEach((row) => {
      cols_square_coords.forEach((col) => {
        const current_square_constraints = [];

        for (const x of row) {
          for (const y of col) {
            current_square_constraints.push(x + y);
          }
        }

        square_constraints.push(current_square_constraints);
      });
    });

    return row_constraints
      .concat(column_constraints)
      .concat(square_constraints);
  }

  generate_binary_constraints(rules_constraints: any) {
    const generatedBinConsts: any[] = [];

    for (const constraint_set of rules_constraints) {
      const binary_constraints = [];

      for (const tuple_of_constraint of getPermutations(constraint_set, 2)) {
        binary_constraints.push(tuple_of_constraint);
      }

      for (const constraint of binary_constraints) {
        const constlist = Array.from(constraint);

        if (!generatedBinConsts.includes(constlist)) {
          generatedBinConsts.push([constlist[0], constlist[1]]);
        }
      }
    }

    return generatedBinConsts;
  }
}
