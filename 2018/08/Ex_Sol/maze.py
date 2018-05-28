import os
from mazesolver import fileIO


def main():
    mazes = fileIO.get_maze_list()
    maze = fileIO.get_maze(mazes[0])

if __name__ == '__main__':
    main()