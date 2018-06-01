"""
This module implements the classic game hangman.

The goal of the game for the player is to guess a word the computer chose at
random by guessing individual letters. If one of the letters is part of the
chosen word, the computer tells the player the positions of all occurences.

The game consists of multiple rounds where the player can guess a letter
when prompted to do so.

If the guessed letter is in the word the computer chose, the game state is
updated and the player is presented with the positions of the letters they
guessed correctly.

If the guess was wrong, that means it is not part of the guess word, it is
added to the list of wrong guesses.

If the player guesses all letters before the number of wrong guesses
exceeds the number of allowed misses, they win. Otherwise the computer
wins.
"""
import random
import string


MAX_MISSES = 5
<<<<<<< HEAD
RULES = """
Hello! Let's play a game of hangman!
I already picked a word, and you now have to guess letters.
But be warned, if you guess wrong more than {} times, you lose!
""".format(MAX_MISSES)
=======
RULES = (
    "Hello! Let's play a game of hangman!\n"
    "I already picked a word, and you now have to guess letters.\n"
    "But be warned, if you guess wrong more than {} times, you lose!\n"
    ).format(MAX_MISSES)
MSG_WIN = "Congratulations!"
MSG_LOSE = "Oh no! Good luck next time! The word was {}"
>>>>>>> f02e5a0dc271881fab8d9e89529da082c88d8fae


def get_art(lvl=0, width=16):
    """
    Returns an array of lines of a hangman ascii art.

    The lines depend on the given level. The higher the level, the more
    of the man is displayed. The Art allows for 5 levels max.

    Args:
        lvl: the level to which the man is to be drawn
        width: what minimum width the drawing should have

    Returns:
        A list of strings, each string representing one line of the drawing,
        formatted to be at least `width` wide.
    """
    art_top = [" _______",
               "|      |"]
<<<<<<< HEAD
    if lvl < 5:
        art_mid = ["|", "|", "|", "|"]
        if lvl > 0:
            art_mid[0] = "|     (_) "
        if lvl > 1:
            art_mid[1] = "|     /|  "
        if lvl > 2:
            art_mid[1] = "|     /|\ "
        if lvl > 3:
            art_mid[2] = "|      |  "
            art_mid[3] = "|     /   "

        art_bot = ["|___________",
                   "/|       | |"]
    else:
        art_mid = [
            "|     (_)   ",
            "|     /|\   ",
            "|      |    ",
            "|     / \   "
        ]
=======
            
    art_mid = ["|", "|", "|", "|"]
    art_bot = ["|___________",
                "/|       | |"]

    if lvl > 0:
        art_mid[0] = "|     (_) "
    if lvl > 1:
        art_mid[1] = "|     /|  "
    if lvl > 2:
        art_mid[1] = "|     /|\ "
    if lvl > 3:
        art_mid[2] = "|      |  "
        art_mid[3] = "|     /   "
    if lvl > 4:
        art_mid[3] = "|     / \   "
>>>>>>> f02e5a0dc271881fab8d9e89529da082c88d8fae
        art_bot = ["|____    ___",
                   "/|   \   | |"]

    form = lambda s: "{0:{width}s}".format(s, width=width)

    art = [form(s) for s in art_top] +\
          [form(s) for s in art_mid] +\
          [form(s) for s in art_bot]
    
    return art


def read_words(file="words.txt"):
    """
    Reads a list of words from a file.

    There needs to be one word per line, for this to work properly.

    Args:
        file: the file to read from

    Returns:
        An array of all the words in the file
    """
    with open(file, "r") as f:
        return f.read().lower().splitlines()


def pick_word(words):
    """
    Chooses a random entry from the given list.

    Args:
        words: the list of words to pick a word from
    
    Returns:
        One word from the list `words`
    """
    return random.choice(words)


<<<<<<< HEAD
def get_guess():
=======
def get_guess(guesses):
>>>>>>> f02e5a0dc271881fab8d9e89529da082c88d8fae
    """
    Asks the user for an input letter until it is a valid letter.

    If the input is more than one character, or is not from the ascii
    alphabet (a-z), we ask the user again. We only deal with lowercase
    letters.

    Returns:
        The input guess from the user
    """
    guess = ""
<<<<<<< HEAD
    while (len(guess) != 1) or (not guess in string.ascii_lowercase):
=======
    while ((len(guess) != 1) or 
            (not guess in string.ascii_lowercase) or 
            (guess in guesses)):
>>>>>>> f02e5a0dc271881fab8d9e89529da082c88d8fae
        guess = input("Which letter is your next guess? ").lower()

    return guess


def print_game_state(turn, misses, guess_word, guesses):
    """
    Print the current state of the game.

    It displays a short header, and the ASCII art depending on how many
    misses there were already. It then displays the game state information:
    - How many misses we made
    - The current state of the guess word
    - The letters that were misses

    Args:
        turn: In which turn we are
        misses: how many misses are left
        guess_word: the current guess word
        guesses: the list of mistaken letters
    """
    # missed holds how many misses we made already
    missed = MAX_MISSES - misses

    # and empty line at the start
    space = ""
    header = "HANGMAN - THE GAME: Turn {}".format(turn)
    lines = [space] + [header] + get_art(missed)
    lines[2] += "MISSED: {} / {}".format(missed, MAX_MISSES)
    lines[3] += "GUESS THE WORD!"
    lines[4] += " ".join(guess_word)
    lines[6] += "Misses so far: " + ", ".join(guesses)
    
    # print the game state
    for line in lines:
        print(line)


def update_guess_word(word, guess_word, guess):
    """
    Updates the guess_word with the newly guessed letter.

    By iterating over the word and comparing each character, we can find
    all occurences of that letter and can replace the underscores in the
    guess word for each found occurence.

    E.g. if the word is 'hello' and the guess_word was ['_', 'e', '_', '_', '_']
    and the guess was 'l', the result will be ['_', 'e', 'l', 'l', '_']

    The function modifies the list in place.

    Args:
        word: the target word
        guess_word: the current state of the guess word
        guess: the guessed letter
    
    Returns:
        the updated state of the guess word. Though unnecessary, since lists
        are passed by reference and altered directly.
    """
    for i, letter in enumerate(word):
        if letter == guess:
            guess_word[i] = letter

    return guess_word


def print_guide():
    """Prints the rules of the game"""
    print(RULES)


def check_win(guess_word):
    """
    Returns True if the player has won.

    The player has won if there are no underscores left to guess.

    Args:
        guess_word: the current state of the guess word

    Returns:
        True in case of win, False otherwise.
    """
    return not "_" in guess_word


<<<<<<< HEAD
def game_end(won, word):
    """
    Prints a message depending on whether the player has won.
    
    Args:
        won: Boolean whether the player has won
        word: The target word
    """
    win_msg = "Congratulations!"
    lose_msg = "Oh no! Good luck next time! The word was {}"

    msg = win_msg if won else lose_msg.format(word)
    print(msg)


def init_guess_word(length):
    """
    Returns the initial guess word state.

    The guess word is initialised with underscores, one for each letter
    of the target word.

    Args:
        length: the length of the target word
    
    Returns:
        The initialised guess word, a list of `length` underscores
    """
    return ["_"] * length


def init():
    """
    Initialises our game world.
=======
def init():
    """Initialises our game world.
>>>>>>> f02e5a0dc271881fab8d9e89529da082c88d8fae

    Sets the default values for the game state variables, and then return
    them as a tuple. This includes to read the words from the file, picking
    a target word at random and initialising the guess word, as well as
    printing the guide to the game.

    Returns:
        The tuple that forms the game state.
    """
    turn = 0
    words = read_words()
    the_word = pick_word(words)
<<<<<<< HEAD
    guess_word = init_guess_word(len(the_word))
=======
    guess_word = ['_'] * len(the_word) # works because strings are immutable
>>>>>>> f02e5a0dc271881fab8d9e89529da082c88d8fae
    misses = MAX_MISSES
    guesses = []

    print_guide()

    return turn, the_word, guess_word, misses, guesses


def game():
    """
    Runs the game loop.

    This function puts it all together to form the whole game. It initialises
    the game state values, and sets the default win state (false).
    It then loops until either the player has won, or the player missed all
    his allowed mistakes.
    In each loop we print the current state of the game, and get a new guessed
    letter. If it was a correct guess, we update the guess word and check
    whether the player has won, otherwise we decrement our allowed mistakes.

    Once the loop ends we print the game world one last time, and print
    the end of game message.
    """
    turn, word, guess_word, misses, guesses = init()
<<<<<<< HEAD
    won = False

    while not won and misses > 0:
        print_game_state(turn, misses, guess_word, guesses)
        guess = get_guess()

        if guess in word:
            guess_word = update_guess_word(word, guess_word, guess)
            won = check_win(guess_word)
=======

    while not check_win(guess_word) and misses > 0:
        print_game_state(turn, misses, guess_word, guesses)
        guess = get_guess(guesses)

        if guess in word:
            guess_word = update_guess_word(word, guess_word, guess)
>>>>>>> f02e5a0dc271881fab8d9e89529da082c88d8fae
        else:
            guesses += guess
            misses -= 1
        
        turn += 1

    print_game_state(turn, misses, guess_word, guesses)
<<<<<<< HEAD
    game_end(won, word)
=======
    
    print( MSG_WIN if check_win(guess_word) else MSG_LOSE.format(word) )
    
>>>>>>> f02e5a0dc271881fab8d9e89529da082c88d8fae


# we can continue the game until the player quits
cont = "y"
while cont == "y":
    game() # play a game!
    # on a y or Y we continue
    cont = input("Do you want to play again? (y/n): ").lower()