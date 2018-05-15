def print_field(playing_field):
    """
    Makes a printout of the field
    """

    print() # empty line for better readability

    # go through all rows in the field
    for i,row in enumerate(playing_field):

        # get all items in the row and make a string with these items
        # this includes a single space before the first and after the last item
        # as well as a pipe (|) between the items
        row_string = ' ' + ' | '.join(row) + ' '
        print(row_string) # print row

        # if this is not the last row, print a line separator
        if i < len(playing_field) - 1:
            print('-' * len(row_string))

    print() # empty line for better readability

def initialize_field(size=3):
    """
    Creates and returns an empty tic tac toe field with measurements size x size
    """

    # make nested list with list comprehension
    return [[' ' for col in range(size)] for row in range(size)]

def check_victory(playing_field,row,col):
    """
    Checks if the player who just chose a field won the game in this turn
    """


    current_player = playing_field[row][col]

    size = len(playing_field)

    # check if the player won in the current row
    if playing_field[(row - 1 + size) % size][col] == current_player:
        if playing_field[(row + 1) % size][col] == current_player:
            return True

    # (if not) check if the player won in the current column
    if playing_field[row][(col - 1 + size) % size] == current_player:
        if playing_field[row][(col + 1) % size] == current_player:
            return True

    # (if not) check if player is on a diagonal
    # fields on the diagonal have either both even or both odd indices
    elif row % 2 == col % 2:

        # top left to bottom right diagonal (consists of fields 0,0 - 1,1 - 2,2)
        # therefore, we check for this diagonal if row equals to column
        if row == col:
            if playing_field[(row - 1 + size) % size][(col - 1 + size) % size] == current_player:
                    if playing_field[(row + 1) % size][(col + 1) % size] == current_player:
                        return True

        # bottom left to top right diagonal (consists of fields 2,0 - 1,1 - 0,2)
        # hence we check for this diagonal if row and column are different
        # (so 0,2 or 2,0)
        # special case: current field is 1,1. in this case we need to check both diagonals
        elif row != col or row == 1:

            if playing_field[(row - 1 + size) % size][(col + 1) % size] == current_player:
                    if playing_field[(row + 1) % size][(col - 1 + size) % size] == current_player:
                        return True

    return False



def game():
    """
    Main tic tac toe game
    """

    playing_field = initialize_field() # get 3x3 field

    turns = len(playing_field)**2 # there can only be as many turns as field

    current_player = 'X' # start with player X

    while turns > 0:
        print_field(playing_field) # first print the field

        input_check = False # variable indicating if player input is valid

        # get input. remain in this loop if just anything is wrong with it
        while input_check == False:
            chosen_field = input("Player " + current_player + ", choose a field (row, column)! ")
            chosen_field = chosen_field.split(',') # split input into list

            if len(chosen_field) == 2: # list needs to be of length 2 for row and column
                try:
                    # try to typecast input
                    row = int(chosen_field[0])
                    col = int(chosen_field[1])

                    # if typecast input is in range of 3x3 field and the chosen field is empty
                    if 0 <= row < 3 and 0 <= col < 3 and playing_field[row][col] == ' ':
                        input_check = True
                # catch error if input not number
                except ValueError:
                    pass # nothing to do here

        # set field to player's letter
        playing_field[row][col] = current_player

        # call function that checks if the player won
        if check_victory(playing_field,row,col) == True:

            # if the player won, congratulate and leave the loop
            print("Congrats Player " + current_player + "! You won!")
            print_field(playing_field)
            break

        # if we get this far, the field was set but nobody has won
        # switch to other player and continue
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

        turns -= 1

game()
