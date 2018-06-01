from os import path
from mazesolver import fileIO, userIO, solver


def main():
    fileIO.MAZEFOLDER = path.join(path.dirname(path.abspath(__file__)), 'mazes')

    userIO.show_welcome()
    play = 'y'
    while play == 'y':
        option = userIO.menu()
        if option == userIO.SOLVE_A_MAZE:
            maze_name = userIO.choose_maze()
            grid = fileIO.get_maze(maze_name)
            solved = solver.solve(grid)
            if userIO.user_save(solved, grid):
                fileIO.save_solved(grid, maze_name)
        elif option == userIO.CREATE_A_MAZE:
            name, maze = userIO.create_maze()
            grid = fileIO.build_maze(maze)
            fileIO.save_maze(grid, name)
        elif option == userIO.QUIT:
            break

        play = input("Do you want to continue? (y/n)\n").lower()


if __name__ == '__main__':
    main()