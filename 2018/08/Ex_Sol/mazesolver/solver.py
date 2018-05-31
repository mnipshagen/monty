
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
    start = find_start_pos(grid)
    if not start:
        return False
    return solve_rec(grid, *start, randomised)
    

def solve_rec(grid, col, row, randomised=True):
    field = grid[row][col]
    if field == GOAL:
        return True
    if field in [WALL, PATH]:
        return False
    if field == FREE_PATH:
        grid[row][col] = PATH
    
    if randomised:
        random.shuffle(DIRECTIONS) # just for fun
    for direction in DIRECTIONS:
        ncol = col + direction[1]
        nrow = row + direction[0]
        if not (0 <= ncol < len(grid[0])) or not (0 <= nrow < len(grid)):
            continue
        if solve_rec(grid, ncol, nrow, randomised):
            return True
    
    if field != START:
        grid[row][col] = FREE_PATH
    return False


def find_start_pos(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == START:
                return x,y
    return False
