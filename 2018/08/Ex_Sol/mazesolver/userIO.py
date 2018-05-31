import os

from . import fileIO
from .solver import GOAL, START, WALL


SOLVE_A_MAZE = 0
CREATE_A_MAZE = 1
QUIT = 2


def show_welcome():
    help_line = lambda line: f"*{line:^78}*"
    
    help_text = (
        "This somewhat interactive program will let you choose a maze" + "\n"
        "of your liking. Our little solver will then do its best to" + "\n"
        "find a way through the maze. In the end it will show you the" + "\n"
        "result of the search and you can choose to save the solved" + "\n"
        "version to show all your friends how amazing your maze solving" + "\n"
        "skills are! ;)" + "\n"
        "You also have the possibility to design your own maze that our" + "\n"
        "solver will then attempt to solve for you." + "\n"
        "Have fun!"
    )
    help_text = help_text.splitlines()
    line_length = max(len(line) for line in help_text)
    help_text = [f"{line:<{line_length}}" for line in help_text]

    print(f"\n{'Maze Solver':*^80}")
    for line in help_text:
        print(help_line(line))
    print(f"{'':*^80}")

def menu():
    menu_line = lambda line: f"|{line:^78}|"

    menu_text = (
        "" + "\n"
        "You have the following options to choose from: "  + "\n"
        "" + "\n"
        "0) Choose an existing maze to be solved" + "\n"
        "1) Create your own maze" + "\n"
        "2) Exit" + "\n"
        ""
    )
    menu_text = menu_text.splitlines()
    line_length = max(len(line) for line in menu_text)
    menu_text = [f"{line:<{line_length}}" for line in menu_text]

    print(f"\n{'Main Menu':~^80}")
    for line in menu_text:
        print(menu_line(line))
    print(f"{'':~^80}\n")

    return get_user_choice("Please choose a menu option.", 3)



def present_mazes(maze_list, print_mazes=False):
    print("The following mazes are available:")
    for i, maze in enumerate(maze_list):
        maze_name = os.path.splitext(maze)[0]
        print(f"ID {i:<4} {maze_name}")
        if print_mazes:
            show_maze(fileIO.get_maze(maze))
        print()

def get_user_choice(msg, length):
    idx = -1
    while idx == -1:
        try:
            val = input(msg + "\n")
            idx = int(val)
            if not (0 <= idx < length):
                raise ValueError("Index out of range.")
        except ValueError:
            idx = -1
            print(f"Valid inputs are: {', '.join(range(length))}")

    return idx

def choose_maze():
    choice = input(
        "Would you like to see the mazes in full "
        "or only the names of the mazes? (f[ull]/n[ames])\n"
    ).lower()
    full = choice in ['f', 'full']
    
    maze_list = fileIO.get_maze_list()
    present_mazes(maze_list, full)
    msg = "Please enter the id of the maze you want to use."
    idx = get_user_choice(msg, len(maze_list))
    if not full:
        show_maze(fileIO.get_maze(maze_list[idx]))
        print()

    return maze_list[idx]

def show_maze(grid):
    for line in grid:
        print(" ".join(line))

def user_save(solved, grid):
    if not solved:
        print("Oh no, that's embarrassing. We found no way through the maze.")
        return False
    else:
        show_maze(grid)
        print("Wooho! There is the way!")
        print("Do you want to save the maze solution? (y/n)")
        return (input().lower() == 'y')

def create_maze():
    print(
        "Welcome to CREATE-A-MAZE!\n"
        "Enter your maze row by row. Make sure that all rows "
        "have the same length. Each maze needs to have a start "
        f"position ({START}) and a goal position ({GOAL}). Use "
        f"{WALL} for the walls of the maze. They are unpassable "
        "for the solver. It is suggested to surround the maze "
        "with walls for better readability.\n"
        "Just press enter (on an empty line) to end input.\n"
        "Please enter your maze now:"
    )
    maze = ""
    row = input()
    row_length = len(row)
    maze += row
    while row != '':
        row = input()
        if row == '':
            break
        if len(row) != row_length:
            print(f"Sorry, this row length {len(row)} had the wrong length. Should be {row_length}.")
            print("Maze so far:")
            show_maze(fileIO.build_maze(maze))
            continue
        
        maze += "\n" + row
    
    print("Your inputted maze:")
    show_maze(fileIO.build_maze(maze))

    maze_name = input("Give your maze a name!\n")

    return maze_name, maze
