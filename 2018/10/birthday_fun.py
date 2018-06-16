"""
This module is a test module for the BirthdayCalc class

Requires the module birthday_calc.
"""

from datetime import datetime
import birthday_calc

class TooOldError(Exception):
    """
    Error indicating the person is too old to exist.
    """
    pass

class TooYoungError(Exception):
    """
    Error indicating the person is too young to exist.
    """
    pass

# action options in the menu
OPTIONS = ['years','months','days','hours','minutes','seconds']


def show_welcome():
    """
    Shows welcome instructions to the user.
    """

    help_line = lambda line: f"*{line:^78}*"

    help_text = (
        "Hello friend!" + "\n"
        "Ever wondered how many months, days, hours, minutes or seconds" + "\n"
        "have passed since your birthday?" + "\n"
        "Have you completely lost track of the years?" + "\n"
        "Well, look no further! We have the ultimate solution for you!" + "\n"
        "Just enter your birth date and the fun starts!" + "\n"
    )
    help_text = help_text.splitlines()
    line_length = max(len(line) for line in help_text)
    help_text = [f"{line:<{line_length}}" for line in help_text]

    print(f"\n{' Birthday Calculator ':*^80}")
    for line in help_text:
            print(help_line(line))

    print(f"{'':*^80}")

def check_legit(bday):
    """
    Checks if the person can exist.

    Raises:
        TooOldError: if older than oldest person as of now (Chiyo Miyako)
        TooYoungError: if birth date is in the future
    """

    if bday < datetime(1901,5,2):
        raise TooOldError()

    elif bday > datetime.today():
        raise TooYoungError()

def get_bday():
    """
    Lets user enter their birth date and checks for its validity.

    Returns:
        calculator: BirthdayCalc object

    """

    valid = False

    while not valid:
        birthdate = input("Please enter your birth date as day, month, year! ")

        try:
            birthdate = str.split(birthdate,",")

            day,month,year = [int(n) for n in birthdate]
            calculator = birthday_calc.BirthdayCalc(day,month,year)
            check_legit(calculator.birthday())

            valid = True

        except ValueError:
            print("Invalid input. Enter as day, month, year and make sure the day exists.")
        except TooOldError:
            print("You should call the newspapers as you are older than the current oldest person! (congrats though)")
        except TooYoungError:
            print("Since you're from the future, can you travel back some more years and buy me some bitcoins? Kthxbye")

    return calculator

def evaluate_action(calculator, unit):
    """
    Executes an action called [unit]_since_birth on an object of BirthdayCalc class.

    Args:
        calculator: BirthdayCalc object
        action: name of the unit
    """

    try:
        # get function name
        func = getattr(calculator,f"{unit}_since_birth")

        # execute function and store result
        result = func()

        # print result
        print(f"It has been {result} {unit} since your birth! \n")

    except AttributeError:
        print(f"Method called {unit}_since_birth not found.")

def main():
    """
    Main birthday test function.
    """

    # display instructions
    show_welcome()

    # get birthday object
    calculator = get_bday()

    cont = 'y'
    while cont == 'y':

        valid = False
        while not valid:
            try:
                # get unit user wants to see their birthday in
                unit = input("What do you want to know? The years, months, days, hours, minutes or seconds since your birth? ")

                # check if unit is available
                if unit not in OPTIONS:
                    raise ValueError

                valid = True
            except ValueError:
                print("Please enter 'months', 'days', 'hours', 'minutes' or 'seconds'!")

        # execute respective function
        evaluate_action(calculator, unit)

        # continue asking for units, if wished for by user
        cont = input("You wanna continue? (y/n) ")
main()
