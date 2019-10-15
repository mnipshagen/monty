"""
A small script to interact with the bunnyfriend.

It loops over a "daily routine" where you can interact with the bunnyfriend,
until it has grown up or ran away. Each daily routine consists of three
interactions with the bunnyfriend.
"""
from bunnyfriend import Bunnyfriend

# print a small introduction for the user
print (
    "A BunnyFriend is a creature that is born small and fluffy and has",
    "  the dream of becoming a big, full-grown bunny!",
    "We want to help its dream come true by feeding and playing with it,",
    "  but be careful... if you don't play enough, it might grow to resent you...",
    sep="\n",
    end="\n\n"
)
# name the pet and create the bunnyfriend instance
bunny = Bunnyfriend(input("Give your bunnyfriend a name: "))

# the main loop. we keep track of days to print them as a header
days = 0
while bunny.interactable:

    for _ in range(3): # interact three times!
        print(f"Day {days}:")
        print(bunny)
        bunny.interact()
    
    bunny.pass_day()
    days += 1
