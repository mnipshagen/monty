"""
Reads and writes mazes
"""
import os
from os import path

MAZEFOLDER = path.join(os.getcwd(), 'mazes')

def get_maze_list():
    mazes = os.listdir(MAZEFOLDER)
    mazes = [maze for maze in os.listdir(MAZEFOLDER) if path.isfile(path.join(MAZEFOLDER, maze))]
    return mazes

def load_maze(filename):
    with open(os.path.join(MAZEFOLDER, filename)) as handle:
        return handle.read()

def build_maze(raw_maze):
    grid = raw_maze.splitlines()
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    return grid

def stringify_maze(grid):
    pass

def save_maze(maze, filename):
    pass

def save_solved(maze, filename):
    pass

def get_maze(filename):
    return build_maze(load_maze(filename))

def save_maze_grid(grid, filename, solved=True):
    pass
