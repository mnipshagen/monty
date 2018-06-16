import bike

def test_bikes():
    print("*** Bike Test Class ***\n")

    # *** testing Bike class ***
    print("First, let's create an ordinary Bike: ")
    bob = bike.Bike(1,5) # 1 seat, 5 gears
    print(f"Going on a ride: {bob.start_ride()}")
    print(f"Going on another ride: {bob.start_ride()}")
    print(f"Stopping the current ride: {bob.end_ride()}")
    print(f"Now, going on another ride again: {bob.start_ride()}")
    print(f"What's our current gear? {bob.curr_gear}")
    print(f"Let's change the gear to 3 then: {bob.change_gear(3)}")
    print(f"What's our current gear? {bob.curr_gear}")
    print("Such a nice Bike! \n")


    # *** testing Bicycle subclass ***
    print("So, what can a Bicycle do that a normal bike cannot?: ")
    sam = bike.Bicycle() # Bicycle has defaults for all values
    print("Let's make some noise:")
    sam.ring_bell()
    print("Such a nice Bicycle! \n")


    # *** testing Motorbike subclass ***
    print("Ok, last but not least, the Motorbike: ")
    jim = bike.Motorbike()
    print(f"First we need to check our tank. Is it full?: {jim.tank}")
    print(f"Ok, then. Going on a ride: {jim.start_ride()}")
    print(f"Finishing our ride: {jim.end_ride()}")
    print(f"What about our tank now. Is it full??: {jim.tank}")
    print(f"Getting new fuel... {jim.fill_tank()}")
    print(f"Tank full?: {jim.tank}")

    try:
        print("Let's try to change the gear to 200:")
        jim.change_gear(200)
    # invalid gear throws exception. we don't want the program to crash
    except ValueError as v:
        print(v)
        print("Well that did not work.")
    print("Such a nice Motorbike! \n")
    print("End of bike test!")

test_bikes()
