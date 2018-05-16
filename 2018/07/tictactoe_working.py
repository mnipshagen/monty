def init_grid(size=3):
    """
    Creates and returns an empty Tic-tac-toe grid with measurements size x size
    """

    # make nested list with list comprehension
    return [[' ' for col in range(size)] for row in range(size)]


def print_grid(grid):
    """
    Prints the grid
    """

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
            print('-' * len(row_string))

    # empty line for better readability
    print()


def get_input(grid, current_player):
    """
    Makes player specify row and column of a field until input is valid
    Returns the indices of the chosen field
    """

    input_check = False
    size = len(grid)

    # get input. remain in this loop if just anything is wrong with it
    while input_check == False:
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

            # catch error if input is not a number
            except ValueError:
                # nothing else to do here
                pass

    # return the chosen field
    return row,col


def check_win(grid,row,col):
    """
    Is handed coordinates row,col of a field in the grid
    Calls functions that check if the player who just chose the field won the
    row, the column or a diagonal corresponding to it
    Returns True if the player just won the game accordingly
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

def check_col(grid,row,col):
    """
    Is handed coordinates row,col of a field in the grid
    Returns True if all fields in the same column are occupied by the same player
    as this field
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
    """
    Is handed coordinates row,col of a field in the grid
    Returns True if field is on a diagonal and if all fields on the corresponding
    diagonal(s) are occupied by the same player as this field
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
    """
    Main Tic-tac-toe game
    """

    # get grid
    grid = init_grid()

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
        if check_win(grid,row,col) == True:
            # if the player won, congratulate and leave the loop
            print("Congrats Player " + current_player + "! You won!")
            break

        # if we get this far, the field was set but nobody has won yet
        # switch to other player and continue
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

        # one field was occupied, so decrease counter
        turns -= 1

    # whether someone won or or there are no fields left, print the grid one last time
    print_grid(grid)

# run game
game()
