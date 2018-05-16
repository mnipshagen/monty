number = None
while (not number) or not (number > 0):
    try_number = input("Please enter a number > 0: ")
    try:
        number = float(try_number)
        print("Got it!")
    except ValueError as err:
        print("Error: ", err)

try:
    file_handle = open("my_file")
except IOError as err:
    print("Could not open file! Error: ", err)
else:
    content = file_handle.read()
    result = analyse(content)
finally:
    file_handle.close()


key_list = ["key", "my_key", "bike_key", "transponder"]
key_to_lock = {
    "my_key": "Finally I can go home again!",
    "bike_key": "This unlocks my Bike!", 
    "transponder": "Back to work it is."
    }

try:
    idx = int(input(f"A number bewteen 0 and {len(key_list)-1} please: "))
    key = key_list[idx]
    print(key_to_lock[key])
except (IndexError, KeyError, ValueError) as err:
    print("Well this didn't work:", err)

key_list = ["key", "my_key", "bike_key", "transponder"]
key_to_lock = {
    "my_key": "Finally I can go home again!",
    "bike_key": "This unlocks my Bike!",
    "transponder": "Back to work it is."
}

try:
    idx = int(input(f"A number bewteen 0 and {len(key_list)-1} please: "))
    key = key_list[idx]
    print(key_to_lock[key])
except IndexError as err:
    print("No, no. This index doesn't work.")
except KeyError as err:
    print("Seems like that key has no lock. How strange.")
except ValueError as err:
    print("That's not a number...")

key_list = ["key", "my_key", "bike_key", "transponder"]
key_to_lock = {
    "my_key": "Finally I can go home again!",
    "bike_key": "This unlocks my Bike!",
    "transponder": "Back to work it is."
}

try:
    idx = int(input(f"A number bewteen 0 and {len(key_list)-1} please: "))
    key = key_list[idx]
    print(key_to_lock[key])
except (IndexError, ValueError) as err:
    print("That was not a valid index:", err)
except KeyError:
    print("Oh no! That key has no lock!")


def sub(a, b):
    return a + b

assert sub(5, 4) == 1, '5 - 4 != 1'
assert sub(7, 3) == 4, '7 - 3 != 4'


def diff(a, b):
    """Returns the absolute difference of a and b"""
    sub = a - b
    return sub if sub >= 0 else -sub

##########
help(diff)


import turtle

help(turtle.up)


def get_number(message):
    number = None
    while number is None:
        try:
            value = input(message)
            number = float(value)
        except ValueError:
            print("That was no number.")
    
    return number

def get_idx():
    number = get_number("A positive integer please: ")
    if number < 0 or not (int(number) == number):
        raise ValueError(f"{number} is no positive integer")
    return number