"""
This module contains several utility functions.

It is tailored to the usage together with the battle module, and might
not be suited for general use.
"""
import inspect


def get_item_from_user(message, lst):
    """
    Gets a valid index from a user to get an item from lst.

    The user is shown `message` and the range of valid indices, in the form
    of "Valid indices inclusive between 0 and max_index". The user is asked 
    until a valid item was chosen.

    Args:
        message: The message to show the user before asking for index
        lst: the list to choose from
    
    Returns:
        The chosen index
    """
    idx = -1
    while idx == -1:
        try:
            # get an input from the user
            print(message)
            val = input(f"Valid indices inclusive between 0 and {len(lst) - 1}\n")
            # try to parse it as an int
            idx = int(val)
            # try to extract the action, this will throw if out of bounds
            item = lst[idx]
        # if it was no int or is out of bounds, remind the user what is to do
        # and reset idx
        except (ValueError, IndexError):
            idx = -1
            print(
                "Please enter an integer value between inclusive "
                f"0 and {len(lst) - 1}"
            )

    return idx

def class_tester(class_to_check_for):
    def class_check(to_test):
        """
        Checks if the passed object is a (sub)class of class_to_check_for.

        We first check if the object is in fact a class, or else issubclass would
        throw an error, and then checks whether the object is a subclass
        of class_to_check_for. issubclass returns True when both arguments are 
        the same class.

        Args:
            to_test: the object to test if it is a class and a Knight

        Returns:
            True if the passed object is a subclass of Knight or the class Knight.
            False otherwise.
        """
        # important for bonus task. Adapted from:
        # https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python#1796247
        # You can safely ignore this code if you don't want to deal with it,
        # it is somewhat advanced.
        return inspect.isclass(to_test) and issubclass(to_test, class_to_check_for)

    return class_check
