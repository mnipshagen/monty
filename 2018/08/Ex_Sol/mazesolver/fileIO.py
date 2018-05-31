"""
Reads and writes mazes
"""
import os
from os import path

MAZEFOLDER = path.join(os.getcwd(), 'mazes')
SOLVEDFOLDER = "solved"

def get_maze_list():
    mazes = os.listdir(MAZEFOLDER)
    mazes = [maze for maze in os.listdir(MAZEFOLDER) if path.isfile(path.join(MAZEFOLDER, maze))]
    return mazes

def _load_maze(filename):
    with open(os.path.join(MAZEFOLDER, filename)) as handle:
        return handle.read()

def build_maze(raw_maze):
    grid = raw_maze.splitlines()
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    return grid

def _stringify_maze(grid):
    return "\n".join(["".join(line) for line in grid])

def save_maze(grid, filename):
    with open(path.join(MAZEFOLDER, filename), "w") as handle:
        handle.write(_stringify_maze(grid))

def save_solved(grid, filename):
    if not path.exists(path.join(MAZEFOLDER, SOLVEDFOLDER)):
        os.makedirs(path.join(MAZEFOLDER, SOLVEDFOLDER))
    solved_filename = path.join(SOLVEDFOLDER, filename)
    return save_maze(grid, solved_filename)

def get_maze(filename):
    return build_maze(_load_maze(filename))
