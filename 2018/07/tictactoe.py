def init_grid(size=3):
    """Returns an empty Tic-tac-toe grid with measurements size x size"""

    # make nested list with list comprehension
    return [[' ' for col in range(sze)] for row in range(size)]


def print_grid(grid):
    """Prints the grid"""

    # empty line for better readability
    print()

    # go through all rows in the field
    for i,row in enumerate(grid):
        # get all items in the row and make a string with these items
        # this includes a single space before the first and after the last item
        # as well as a pipe (|) between the items
        row_string = ' ' + ' | '.join(row) + ' '
        print(row_string) # print row

        # if this is not the last row, print a line separator as well
        if i < len(grid) - 1:
            print('-' * len(row_string)

    # empty line for better readability
    print()


def get_input(grid, current_player):
    """ Get the field the player wants to play

    Get a row and column seperated by a comma from the player. The player
    is asked until he chooses a valid, free field of the grid.

    Args:
        grid: The tic tac toe game field
        current_player: the symbol of the player

    Returns:
        The row and column as a tuple
    """

    input_check = False
    size = len(grid)

    # get input. remain in this loop if just anything is wrong with it
    while input_check = False:
        chosen_field = input("Player " + current_player + ", choose a field (row, column)! ")

        # split up into list
        chosen_field = chosen_field.split(',')

        # list needs to be of length 2 (standing for row and column)
        if len(chosen_field) == 2:
            # try to typecast input
            try:
                row = int(chosen_field[0])
                col = int(chosen_field[1])

                # input is ok if typecast input is in range of grid and the chosen field is empty
                if 0 <= row < size and 0 <= col < size and grid[row][col] == ' ':
                    input_check = True
                else:
                    raise ValueError()

            # catch error if input is not a number
            except ValueError:
                print(("Please make sure that you are choosing "
                    "an empty cell and that your indices are "
                    "inside the grid's boundaries (0-indexed)."))

    # return the chosen field
    return row,col


def check_win(grid,row,col):
    """Returns True if current player has won.

    Given the cell that was just populated, it checks the row, column and
    diagonal of that field for a win condition.

    The win condition is to have the whole row/column/diagonal filled with
    one player's symbol.

    Args:
        grid: the tic tac toe game field
        row: the row of the cell to check
        col: the column of the cell to check

    Returns:
        True if a win condition is met
    """

    return check_row(grid,row,col) or check_col(grid,row,col) or check_diag(grid,row,col)


def check_row(grid,row,col):
    """
    Is handed coordinates row,col of a field in the grid
    Returns True if all fields in the same row are occupied by the same player
    as this field
    """

    current_player = grid[row][col]
    return grid[row].count(current_player) == len(grid)

def check_col(grid,col,row):
    """Returns true if the column of the current cell is in win condition.

    Counts the occurences of the cell's player's marker and if it is equal
    to the size of the grid, the player has won.

    Args:
        grid: the tic tac toe game field
        row: the row of the cell to check
        col: the column of the cell to check

    Returns:
        True if a win condition is met
    """

    current_player = grid[row][col]
    size = len(grid)
    count = 0

    # go through all fields in the column manually and increase count if they're
    # occupied by the same player as the chosen field
    for i in range(size):
        count += grid[i][col] == current_player

    return count == size

def check_diag(grid,row,col):
    """Returns true if the diagonal of the current cell is in win condition.

    Counts the occurences of the cell's player's marker and if it is equal
    to the size of the grid, the player has won.

    Checks in which diagonal the cell is, and then counts occurences in
    this diagonal.

    Args:
        grid: the tic tac toe game field
        row: the row of the cell to check
        col: the column of the cell to check

    Returns:
        True if a win condition is met
    """
    
    size = len(grid)
    current_player = grid[row][col]

    # first diagonal, for which holds: row == col (e.g. 0,0 1,1 2,2)
    if row == col:
            count = 0
            for i in range(size):
                count += grid[i][i] == current_player

            if count == size:
                return True

    # second diagonal, for which holds: row + col == size - 1 (e.g. 0,2 1,1 2,0)
    # size being the length of the grid in one dimension
    if row + col == size - 1:
            count = 0
            for i in range(size):
                count += grid[i][size - 1 - i] == current_player

            if count == size:
                return True

    return False

def game():
    """Runs the main game loop

    Initialised the empty play field, and then allows up to grid size ^ 2
    turns until the game is over. When a win condition is met, the loop
    breaks and the game is over.
    """

    # there can only be as many turns as fields in the grid
    turns = len(grid)**2

    # start with player X
    current_player = 'X'

    # repeat while there are still free fields
    while turns > 0:

        # first print the field
        print_grid(grid)

        # call function to get field indices through player input
        row, col = get_input(grid, current_player)

        # set chosen field to player's letter
        grid[row][col] = current_player

        # call function that checks and returns if the player won now
        if check_win(grid,row,col,current_player) == True:
            # if the player won, congratulate and leave the loop
            print("Congrats Player " current_player + "! You won!")
            break

        # if we get this far, the field was set but nobody has won yet
        # switch to other player and continue
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

    else:
        print("Well played you two. It's a draw.")
    # whether someone won or or there are no fields left, print the grid one last time
    print_grid(grid)

# run game
game()
