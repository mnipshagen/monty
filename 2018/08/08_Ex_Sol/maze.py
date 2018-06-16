"""
This module contains the main maze program.

The module expects the modules 'fileIO', 'userIO' and 'solver' from the package
'mazesolver' to be available.

It uses the functions offered in those modules to form a 
fully functioning maze solver application.
"""

from os import path
from mazesolver import fileIO, userIO, solver


def main():
    """
    Main maze function. Contains a loop in which the player is repeatedly able
    to choose between solving a maze, creating a maze and exiting the program.
    """

    # Set the mazefolder to the absolute path of a folder called 'mazes'
    # that is at the same location as the maze.py script
    fileIO.MAZEFOLDER = path.join(path.dirname(path.abspath(__file__)), 'mazes')

    # display a welcome message to the user explaining the program
    userIO.show_welcome()

    play = 'y'

    # repeat for as long as the user decides to continue
    while play == 'y':

        # show user the menu options and get option chosen by the user
        option = userIO.menu()

        # if user wants a maze to be solved
        if option == userIO.SOLVE_A_MAZE:
            # let user choose a maze to solve
            maze_name = userIO.choose_maze()
            # import the chosen maze
            grid = fileIO.get_maze(maze_name)
            # solve the maze
            solved = solver.solve(grid)
            # give user the choice to save the solved maze
            if userIO.user_save(solved, grid):
                fileIO.save_solved(grid, maze_name)

        # if user wants to create a maze themselves
        elif option == userIO.CREATE_A_MAZE:
            # get maze name and new raw input maze from the user
            name, maze = userIO.create_maze()
            # create maze from the raw input maze
            grid = fileIO.build_maze(maze)
            # save the maze in a new file
            fileIO.save_maze(grid, name)

        # user wants to quit
        elif option == userIO.QUIT:
            # quit loop
            break

        # let user to decide whether to continue solving/creating a maze or not
        play = input("Do you want to continue? (y/n)\n").lower()


# if this is the module currently executed (not imported)
if __name__ == '__main__':
    # run main function
    main()
