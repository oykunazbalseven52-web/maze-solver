# Maze Solver

A terminal-based maze solver written in Python.
It uses Breadth-First Search (BFS) to find the shortest path.

## Features

- Finds the start and exit positions.
- Finds the shortest path using BFS.
- Displays the path using dots.
- Reports when no path exists.
- Checks for missing start or exit markers.

## Maze Symbols

- `#`: Wall
- Space: Walkable cell
- `S`: Start
- `E`: Exit
- `.`: Solution path

## Run

Requires Python 3. No external packages are needed.

```bash
python3 maze_solver.py
```

## Example Output

```text
Solved maze:
#######
#S....#
# ###.#
#   #E#
#######
```

## Data Structures

- Queue (`deque`): Stores cells waiting to be explored.
- Set: Tracks visited cells.
- Dictionary: Stores each cell's parent to reconstruct the path.
- List: Stores the maze and the solution path.
- Tuple: Represents a cell as `(row, column)`.

## How It Works

BFS explores cells in order of their distance from the start.
Because each move has the same cost, it finds the shortest path.
The solution is reconstructed by following parent cells from
the exit back to the start.

## Complexity

For a maze with R rows and C columns:

- Time: O(R × C)
- Space: O(R × C)

## What I Practiced

Python functions, loops, indexing, queues, sets, dictionaries,
and graph traversal with BFS.