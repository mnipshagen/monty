"""
Implements configurable functionality to to solve a maze.

It offers backtracking functions to find a way through a maze.
It also defines several constants:
- The four directions as tuples which show their relative change to the current field.
- A list of those directions, which may change order during runtime
- The configurable parameters: WALL, START, GOAL, PATH, FREE_PATH, which represent
the corresponding parts of the maze, all as single characters.
"""
import random


UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
WALL = '#'
START = '*'
GOAL = 'G'
PATH = 'o'
FREE_PATH = ' '


def solve(grid, randomised=True):
    """
    Initialises the backtracking search through the maze.

    It first searches for the start position in the maze. If none is found it
    returns False. Otherwise it calls the recursive search through the maze.

    Args:
        grid: the maze to find a way through
        randomised: Whether to randomise the order in which the directions
            are checked or not
    
    Returns:
        True if a way was found, False otherwise.
    """
    start = _find_start_pos(grid)
    if not start: # end if there is no start pos
        return False

    # start recursive search with the unzipped start pos
    return _solve_rec(grid, *start, randomised)
    

def _solve_rec(grid, col, row, randomised=True):
    """
    Uses backtracking to recursively search a way through the maze.

    The function immediately returns if the goal was found or the current field
    is a wall or part of the path.
    It then marks the current field as part of the path. If randomised is
    True, it shuffles the list of directions to spice the search up a little.
    It then calls itself on one of the neighbouring fields, but checks first if
    the indices are still valid, in case the maze is not surrounded by walls.
    It returns immediately if one direction returns True. If all 4 directions
    do not lead to the goal, the field is marked as free again, and the function
    returns False.

    Args:
        grid: the maze to search in
        col: the column of the current field
        row: the row of the current field
        randomised: whether to randomise order of directions
    
    Returns:
        True if a way was found, False otherwise.
    """
    # save field for easier access
    field = grid[row][col]

    # check if we can even walk on this field or if it is the goal
    if field == GOAL:
        return True
    if field in [WALL, PATH]:
        return False
    
    # we are ready. mark the path.
    if field == FREE_PATH:
        grid[row][col] = PATH
    
    # shuffle the order in which we check directions. 
    # because there is (nearly) always more than one solution
    if randomised:
        random.shuffle(DIRECTIONS) # just for fun

    # check all for directions
    for direction in DIRECTIONS:
        # the neighbouring field's coordinates
        ncol = col + direction[1]
        nrow = row + direction[0]
        # if the field is out of bounds, skip it
        if not (0 <= ncol < len(grid[0])) or not (0 <= nrow < len(grid)):
            continue
        
        # if the direction lead to the goal, return true.
        if solve_rec(grid, ncol, nrow, randomised):
            return True
    
    # no direction lead to the goal. Free the field and return False
    if field != START:
        grid[row][col] = FREE_PATH
    return False


def _find_start_pos(grid):
    """
    Searches through the grid until the START is found.
    
    Args:
        grid: the maze to find the START in
    
    Returns:
        start pos as tuple of (row, col) if START was found, False otherwise.
    """
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == START:
                return x,y
    return False
