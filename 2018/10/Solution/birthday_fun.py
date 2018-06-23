"""
This module is a test module for the BirthdayCalc class

Requires the module birthday_calc.
"""

from datetime import datetime
import birthday_calc

class ImpossiblePersonError(Exception):
    """ Error indicating a person can't exist. """
    pass

# action options in the menu
OPTIONS = ['years','months','days','hours','minutes','seconds', 'next']

def show_welcome():
    """ Shows welcome instructions to the user. """

    # formatting helper function
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

    # print instructions line by line
    print(f"\n{' Birthday Calculator ':*^80}")
    for line in help_text:
            print(help_line(line))

    print(f"{'':*^80}")


def check_legit(bday):
    """
    Checks if the person can exist.

    Raises:
        ImpossiblePersonError: if older than oldest person or date is in the future
    """

    # too old (current oldest person is Chiyo Miyako, born on May 2nd, 1901)
    if bday < datetime(1901,5,2):
        raise ImpossiblePersonError("You should call the newspapers as you are older than the current oldest person! (congrats though)")

    # too young
    elif bday > datetime.today():
        raise ImpossiblePersonError("Since you're from the future, can you travel back some more years and buy me some bitcoins? Kthxbye")


def get_bday():
    """
    Lets user enter their birth date and checks for its validity.

    Returns:
        calculator: BirthdayCalc object
    """

    valid = False
    while not valid:
        try:
            # get the data
            year = int(input("Please enter the year in which you were born: "))
            month = int(input("Please enter the month in which you were born (1-12): "))
            day = int(input("Please enter the day on which you were born (1-31): "))

            # try to create BirthdayCalc object
            calculator = birthday_calc.BirthdayCalc(day,month,year)
            # if successful without exceptions, check if the person can even exist
            check_legit(calculator.bday)

            valid = True

        except ValueError:
            print("Invalid input. Enter as numbers and make sure the date exists.")
        except ImpossiblePersonError as err:
            print(err)
        finally:
            # empty line so it's prettier
            print()

    return calculator


def evaluate_action(calculator, unit):
    """
    Executes an action called [unit]_since_birth on an object of BirthdayCalc class.

    Args:
        calculator: BirthdayCalc object
        action: name of the unit
    """

    # just one way of doing it: first checking if user asked for next birthday
    if unit == "next":
        # get days left
        days_left = calculator.next_birthday()

        # function will return 365
        if days_left == 0:
            print("No days left! Your birthday is today! Happy birthday!")
        elif days_left == 1:
            print("Your birthday is tomorrow! Just 1 day left!")
        else:
            print(f"There are {days_left} days left until your next birthday! \n")
        return

    try:
        # getattr will look in the class of calculator if it can find a function
        # with the name given by the string in the second argument
        # this string is composed of the unit name and _since_birth
        # (e.g. "months_since_birth")
        # "func" will now reference the function that is retrieved
        func = getattr(calculator,f"{unit}_since_birth")

        # execute the function [...]_since_birth() and store result
        result = func()

        # print result
        print(f"It has been {result} {unit} since your birth! \n")

    # function could not be found
    except AttributeError:
        print(f"Method called {unit}_since_birth not found.")


def main():
    """ Main birthday test function. """

    # display instructions
    show_welcome()

    # get birthday object
    calculator = get_bday()

    cont = 'y'
    while cont == 'y':
        valid = False
        while not valid:
            try:
                # get unit user wants to see their age in
                unit = input("What do you want to know? The years, months, days,"
                "hours, minutes or seconds since your birth?\nOr type 'next' if "
                " you want to find out how many days there are left until your "
                "next birthday: ")

                # check if unit is available
                if unit not in OPTIONS:
                    raise ValueError

                # input was fine if we make it to this point
                valid = True
            except ValueError:
                print("Please enter 'months', 'days', 'hours', 'minutes' or 'seconds'!")

        # execute respective function
        evaluate_action(calculator, unit)

        # continue asking for units, if wished for by user
        cont = input("You wanna continue? (y/n) ")

# start program
main()
