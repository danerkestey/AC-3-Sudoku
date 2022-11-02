import { Sudoku } from "./Sudoku";
import { is_different } from "./utils";

export const remove_inconsistent_values = (
  csp: Sudoku,
  cell_i: string | number,
  cell_j: string | number
) => {
  let removed = false;

  for (const value of csp.possibilities[cell_i]) {
    let q = false;
    for (const poss of csp.possibilities[cell_j]) {
      if (is_different(value, poss)) q = true;
    }

    if (!q) {
      delete csp.possibilities[cell_i];
      removed = true;
    }
  }

  return removed;
};

export const ac3 = (csp: Sudoku, queue: any[] = []) => {
  if (queue.length === 0) {
    queue = Array.from(csp.binary_constraints);
  }

  while (queue) {
    const [xi, xj] = queue.shift();
  }
};
