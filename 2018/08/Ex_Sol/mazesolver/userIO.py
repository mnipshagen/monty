"""
This module handles the user interactions in the maze program.

The module expects the modules 'fileIO' and 'solver' (from own package)

Functions:
    show_welcome(): Show welcome instructions to user.
    menu(): Show menu options to user, lets them choose one.
    present_mazes(): Presents maze IDs, maze names (and, if wished for,
                     complete mazes) to the user
    get_user_choice(): Lets user choose valid ID of a maze.
    choose_maze(): Shows all maze choices to user, lets user choose one.
    show_maze(): Prints a maze line by line.
    user_save(): Makes user choose if they want a (solved) maze saved.
    create_maze(): Lets the user enter a new maze row by row.
"""


import os

from . import fileIO
from .solver import GOAL, START, WALL

# constants matching the options of solving a maze, creating a maze or
# quitting the program to a number
SOLVE_A_MAZE = 0
CREATE_A_MAZE = 1
QUIT = 2


def show_welcome():
    """Displays an instructing welcome message to the user."""


    # define functions that formats a line of the help text to be put between
    # two pipes and have a length of 78 characters
    help_line = lambda line: f"*{line:^78}*"

    # text to present to the user
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
    # get text as a list and normalize line lengths
    help_text = help_text.splitlines()
    line_length = max(len(line) for line in help_text)
    help_text = [f"{line:<{line_length}}" for line in help_text]

    # print first line
    print(f"\n{'Maze Solver':*^80}")
    # use help_line() to format all lines in the text, then print
    for line in help_text:
        print(help_line(line))
    # print last line
    print(f"{'':*^80}")

def menu():
    """
    Displays the main menu and instuctions to the user, then lets them choose
    an option.

    Returns:
        get_user_choice("Please choose a menu option.", 3): Option chosen by
                                                            the user
    """

    # define functions that formats a line of the menu text to be put between
    # two pipes and have a length of 78 characters
    menu_line = lambda line: f"|{line:^78}|"

    # text to present to the user
    menu_text = (
        "" + "\n"
        "You have the following options to choose from: "  + "\n"
        "" + "\n"
        "0) Choose an existing maze to be solved" + "\n"
        "1) Create your own maze" + "\n"
        "2) Exit" + "\n"
        ""
    )
    # get text as a list and normalize line lengths
    menu_text = menu_text.splitlines()
    line_length = max(len(line) for line in menu_text)
    menu_text = [f"{line:<{line_length}}" for line in menu_text]

    # print first line
    print(f"\n{'Main Menu':~^80}")
    # use menu_line() to format all lines in the text, then print
    for line in menu_text:
        print(menu_line(line))
    # print last line
    print(f"{'':~^80}\n")

    # let user choose a menu option and return the choice
    return get_user_choice("Please choose a menu option.", 3)



def present_mazes(maze_list, print_mazes=False):
    """
    Shows the available maze IDs and maze names to the user. Is able to show the
    corresponding mazes as well.

    Args:
        maze_list: list of all available mazes
        print_maze: boolean indicating if the mazes should be shown as well.
                    defaults to False.

    """


    print("The following mazes are available:")

    # go through all mazes in the list and assign an index to each of them
    for i, maze in enumerate(maze_list):

        # show maze name and ID
        maze_name = os.path.splitext(maze)[0]
        print(f"ID {i:<4} {maze_name}")

        # show the corresponding mazes as well if this option was chosen
        if print_mazes:
            show_maze(fileIO.get_maze(maze))

        print()


def get_user_choice(msg, length):
    """
    Makes user choose an existing index of a maze.

    Args:
        msg: Message to be shown to user when asked for input of an index
        length: length of maze list, so valid indices are between 0 and length-1

    Returns:
        idx: index of chosen maze
    """

    idx = -1

    # let user enter an ID as long as the ID is not valid
    while idx == -1:

        # get maze index by user input
        try:
            val = input(msg + "\n")
            idx = int(val)

            # raise an error if maze index cannot be matched to a maze
            if not (0 <= idx < length):
                raise ValueError("Index out of range.")

        # show available maze indices to user if index was invalid
        except ValueError:
            idx = -1
            print(f"Valid inputs are: {', '.join(range(length))}")

    # return index of chosen maze
    return idx

def choose_maze():
    """
    Lets the user choose a maze to solve out of a list of mazes.

    Return:
        maze_list[idx]: maze with ID 'idx' chosen by the user
    """

    # let user choose whether to display only the maze names or the complete
    # mazes and save this choise in 'full' as True/False
    choice = input(
        "Would you like to see the mazes in full "
        "or only the names of the mazes? (f[ull]/n[ames])\n"
    ).lower()
    full = choice in ['f', 'full']

    # get all mazes
    maze_list = fileIO.get_maze_list()
    # show all the maze IDs and, if user chose to, corresponding mazes
    present_mazes(maze_list, full)

    # let user choose a maze id and check input
    msg = "Please enter the id of the maze you want to use."
    idx = get_user_choice(msg, len(maze_list))

    # show only chosen maze to user if they did not decide to show all the mazes
    if not full:
        show_maze(fileIO.get_maze(maze_list[idx]))
        print()

    # return the maze chosen by the user
    return maze_list[idx]

def show_maze(grid):
    """
    Prints a maze line by line.

    Args:
        grid: the maze
    """

    # go through each line of the maze
    for line in grid:
        # add a space between characters for readability and print
        print(" ".join(line))


def user_save(solved, grid):
    """
    Make user choose if they want to save the solved maze and returns choice.

    Args:
        solved: boolean indicating whether maze was solved or not
        grid: the maze

    Returns:
        True if user decides to save the maze by typing 'y'
        False if user decides to not save the maze by not typing 'y' or if the
        maze was not solved
    """

    # no way was found through the maze so there is no solved maze to save
    if not solved:
        print("Oh no, that's embarrassing. We found no way through the maze.")
        return False

    # if maze was solved
    else:
        # show solved maze to the user
        show_maze(grid)
        print("Wooho! There is the way!")

        # ask if user wants to save maze and return choice (True/False)
        print("Do you want to save the maze solution? (y/n)")
        return (input().lower() == 'y')


def create_maze():
    """
    Lets the user enter a new maze row by row and returns it and its name.

    Returns:
        maze_name: name of the new maze
        maze: new maze as string
    """

    # show instructions to user
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
    # create empty maze
    maze = ""

    # get a new row, get its length and add to the maze
    row = input()
    row_length = len(row)
    maze += row

    # if row is not empty (user is not finished yet)
    while row != '':

        # get a new row
        row = input()

        # break loop if new row is empty (user is finished)
        if row == '':
            break

        # all rows of the maze need to have the samze length
        if len(row) != row_length:

            # print message and current maze to remind user to put in rows of
            # fitting length
            print(f"Sorry, this row length {len(row)} had the wrong length. Should be {row_length}.")
            print("Maze so far:")
            show_maze(fileIO.build_maze(maze))
            # go back to beginning of the loop
            continue

        # if length was fitting we are now able to add the new row to the maze
        maze += "\n" + row

    # show finished maze to the user
    print("Your inputted maze:")
    show_maze(fileIO.build_maze(maze))

    # make user choose name for the maze
    maze_name = input("Give your maze a name!\n")

    # return maze name and new maze (as string)
    return maze_name, maze
