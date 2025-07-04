# Python Sudoku Solver

A command-line Sudoku solver implemented in Python, leveraging a recursive backtracking algorithm to find solutions for standard 9x9 Sudoku puzzles. It also provides a clear visual representation of the board.

## Features

* **Backtracking Algorithm**: Efficiently solves Sudoku puzzles by trying possible numbers and backtracking when a path leads to an invalid state.
* **Board Validation**: Includes robust methods to check if a number can be legally placed in a given cell based on row, column, and 3x3 square rules.
* **Empty Cell Identification**: Quickly finds the next empty cell (represented by `0`) on the board.
* **Clear Board Representation**: The board can be printed to the console with empty cells displayed as asterisks (`*`) for easy readability.
* **Solvability Check**: Determines if a given puzzle is solvable or not.

## How It Works

The solver uses a depth-first search (DFS) approach with backtracking:

1.  **Find an Empty Cell**: It searches for the next available empty cell on the board.
2.  **Base Case**: If no empty cells are found, the puzzle is solved, and the function returns `True`.
3.  **Try Numbers**: For each empty cell, it attempts to place numbers from 1 to 9.
4.  **Validate Placement**: Before placing a number, it checks if the number is valid in its row, column, and the 3x3 subgrid.
5.  **Recursive Call**: If a number is valid, it's provisionally placed on the board, and the `solver` method recursively calls itself to solve the rest of the puzzle.
6.  **Backtracking**:
    * If the recursive call returns `True`, it means a solution was found down that path, so the current `solver` call also returns `True`.
    * If the recursive call returns `False` (meaning the current `guess` led to an unsolvable state), the number is removed from the cell (set back to `0`), and the loop continues to try the next `guess`.
7.  **No Solution**: If the loop finishes trying all numbers (1-9) for an empty cell and none lead to a solution, the current `solver` call returns `False`, triggering backtracking in the previous call.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Running the Solver

1.  **Save the code**: Copy the entire provided Python code into a file named `sudoku_solver.py` (or any other `.py` extension).

2.  **Open your terminal or command prompt**: Navigate to the directory where you saved the `sudoku_solver.py` file.

3.  **Run the script**:
    ```bash
    python sudoku_solver.py
    ```

The script will then print the initial puzzle, and if solvable, the completed puzzle.

## Code Structure

* **`Board` Class**:
    * `__init__(self, board)`: Initializes a `Board` instance with a 2D list representing the Sudoku puzzle.
    * `__str__(self)`: Allows you to `print()` a `Board` object directly, rendering it as a formatted string with `*` for empty cells.
    * `find_empty_cell(self)`: Iterates through the board to find the next empty cell (value `0`), returning its `(row, col)` coordinates or `None` if no empty cells are left.
    * `valid_in_row(self, row, num)`: Checks if `num` is already present in the specified `row`.
    * `valid_in_col(self, col, num)`: Checks if `num` is already present in the specified `col`.
    * `valid_in_square(self, row, col, num)`: Checks if `num` is already present in the 3x3 subgrid corresponding to `(row, col)`.
    * `is_valid(self, empty, num)`: A helper method that combines `valid_in_row`, `valid_in_col`, and `valid_in_square` to determine if `num` is a legal placement at `empty` (`(row, col)`).
    * `solver(self)`: The recursive backtracking function that attempts to solve the puzzle in place.

* **`solve_sudoku(board)` Function**:
    * The main entry point. It takes a raw 2D list `board`, creates a `Board` object, prints the initial state, calls the `solver`, and then prints the solved board or a message indicating it's unsolvable.

## Example Output

When you run the script with the provided `puzzle`, you will see output similar to this: