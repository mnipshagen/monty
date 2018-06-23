"""
This module starts a countdown with a really dramatic ending. Viewer discretion
is advised

Uses the time and webbrowser modules.
"""

import time
import webbrowser


class NegativeError(Exception):
    """ Just some error to avoid counting down from negative numbers. """
    pass

def countdown(seconds):
    """
    Counts down from seconds to 0, then becomes really dramatic.

    Args:
        seconds: second number to count down from
    """

    print("\nBRACE YOURSELF!\n") # you really should

    # countdown function
    while seconds > 0:
        # print time left
        print(seconds, "%s left!" %("seconds" if seconds > 1 else "second"))
        time.sleep(1) # pause
        seconds -= 1 # one more second passed

    print("\nAND BOOOOOM!")
    webbrowser.open('https://www.youtube.com/watch?v=DLzxrzFCyOs')


def countdown_starter():
    """ Gets a user input, checks for validity, then starts the countdown. """

    valid = False
    while not valid:
        try:
            # try casting to int
            seconds = int(input("Please enter the seconds to count down: "))

            # cannot count down properly from a negative number
            if seconds <= 0:
                raise NegativeError()

            # input was valid, so we can start the countdown and leave the loop
            valid = True
            countdown(seconds)

        except ValueError: # non-integer inputs produce ValueErrors
            print("Please type in only integer numbers!")
        except NegativeError:
            print("Please type in only positive numbers!")


# start main function
countdown_starter()
