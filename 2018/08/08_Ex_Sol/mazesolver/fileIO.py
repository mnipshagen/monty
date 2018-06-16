"""
Functions to load and save mazes as well as convert between list and string.

This module offers two constants which can be changed from the outside.
MAZEFOLDER holds the path to the folder in which the maze files reside.
SAVEFOLDER is the name of the folder inside the MAZEFOLDER in which solved mazes are saved

This module offers functionality to read mazes from files, write them back to
files, and convert between the string representation of a maze and its list
representation. It can also list all available mazes.
"""
import os
from os import path


MAZEFOLDER = path.join(os.getcwd(), 'mazes')
SOLVEDFOLDER = "solved"


def get_maze_list():
    """
    Returns a list of all available mazes.

    Reads in all files that are inside the MAZEFOLDER, and returns their names
    as a list.

    Returns:
        List of filenames from the MAZEFOLDER
    """
    mazes = os.listdir(MAZEFOLDER)
    mazes = [maze for maze in os.listdir(MAZEFOLDER) if path.isfile(path.join(MAZEFOLDER, maze))]
    return mazes

def _load_maze(filename):
    """
    Returns the contents of the file in MAZEFOLDER with the name filename.

    Args:
        filename: the name of the mazefile to load
    
    Returns:
        the contents of the file as string
    """
    with open(os.path.join(MAZEFOLDER, filename)) as handle:
        return handle.read()

def build_maze(raw_maze):
    """
    Builds the 2D-list representation of a maze from its string form.

    Args:
        raw_maze: the maze in its string form as read from the user or its file
    
    Returns:
        The 2D grid that represents a maze
    """
    grid = raw_maze.splitlines()
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    return grid

def _stringify_maze(grid):
    """
    Converts a grid back into its string form

    Args:
        grid: the 2D grid maze representation

    Returns:
        The string version of the maze as it is in a file
    """
    return "\n".join(["".join(line) for line in grid])

def save_maze(grid, filename):
    """
    Saves the passed grid back into a file

    Appends the filename to the MAZEFOLDER path and writes into that file. If
    it exists, it is overwritten. The grid is stringified before written to the
    file.

    Args:
        grid: the 2d grid maze representation to be saved
        filename: the filename that the maze is going to be saved as 
            into the MAZEFOLDER
    """
    with open(path.join(MAZEFOLDER, filename), "w") as handle:
        handle.write(_stringify_maze(grid))

def save_solved(grid, filename):
    """
    Wrapper function to save a solved maze inside the SOLVED folder.

    It takes the grid of a maze, which should be solved, and the filename to 
    save it under. It first checks if the solved folder exists already and if
    it does not, create it. It then splits the filename into basename and 
    extension if it has one, and if the file already exists keeps adding
    incrementing numbers to the filename to not overwrite existing solutions.
    It then calls save_maze() with the filename appended to the SOLVED folder name.

    Args:
        grid: The 2d grid representation of the maze
        filename: the name the maze should be saved under in the solved folder

    Returns:
        save_maze(): whatever save_maze returns and just passes it on
    """
    save_path = path.join(MAZEFOLDER, SOLVEDFOLDER)
    if not path.exists(save_path):
        os.makedirs(save_path)
    
    # split into path + extension
    base_filename, extension = path.splitext(filename)
    solved_filename = base_filename
    ext = 0 # number to append if the file already to exists
    # increase number appendix until there is no more file with that name
    while path.exists(path.join(save_path, solved_filename + extension)):
        solved_filename = filename + "_" + str(ext)
    
    solved_filename = path.join(SOLVEDFOLDER, solved_filename + extension)
    return save_maze(grid, solved_filename)

def get_maze(filename):
    """
    Convenience function to get a grid from a file.

    Takes the filename of the maze to load, loads the maze from the file,
    and builds it into a grid. Then returns that grid.

    Args:
        filename: the file to load the maze from

    Returns:
        the grid representation of the maze
    """
    return build_maze(_load_maze(filename))
