import React from "react";
import Square from "./Square";

type IProps = {
  startGrid: number[][];
  grid: number[][];
  onChange: any;
  disabled: boolean;
};

const Board: React.FC<IProps> = ({ startGrid, grid, onChange, disabled }) => {
  const renderSquares = () => {
    const squares: any[] = [];

    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        const index = `${i},${j}`;
        squares.push(
          <Square
            style={
              startGrid[i][j] === 0 ? { color: "red" } : { color: "black" }
            }
            key={index}
            id={index}
            onChange={onChange}
            value={grid[i][j] === 0 ? "" : grid[i][j].toString()}
            disabled={disabled}
          />
        );
      }
    }

    return squares;
  };

  return <div className="sudoku-grid shadow">{renderSquares()}</div>;
};

export default Board;
