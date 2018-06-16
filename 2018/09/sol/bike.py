"""
This module contains the definitions for Bike and its subclasses Bicycle and
Motorbike.
"""


class Bike:
    """
    Class defining a bike that can be ridden and have its gear changed.

    Attributes:
        seats: number of seats the bike has
        gears: number of gears the bike has
    """

    def __init__(self, seats, gears):
        """
        Creates a new Bike object.

        Args:
            seats: number of seats the bike has
            gears: number of gears the bike has
        """

        self.seats = seats
        self.gears = gears
        self._curr_gear = 1 # current gear, private
        self._riding = False # bike is per default not ridden

    @property
    def curr_gear(self):
        """
        Purpose of this function is to enable the user to check the gear
        status, but is only able to change it with a specific method.
        (was not necessary to implement it this way)
        """
        return self._curr_gear

    def start_ride(self):
        """
        Starts a bike ride.

        Returns:
            True if successful.
            False if bike is already on a ride.
        """

        # can't ride a bike if already ridden
        if self._riding:
            return False

        self._riding = True
        return True

    def end_ride(self):
        """
        Ends a bike ride.

        Returns:
            True if successful.
            False if bike is not currently ridden.
        """

        # can't stop a bike ride if the bike is already standing
        if not self._riding:
            return False

        self._riding = False
        return True

    def change_gear(self, new_gear):
        """
        Changes bike gear to a new gear.

        Args:
            new_gear: gear to be changed to

        Returns:
            True if gear was successfully changed.

        Raises:
            ValueError if current gear is same as new gear or new gear is <= 0
            or not in range of available gears.
        """

        if self._curr_gear == new_gear or not 0 < new_gear <= self.gears:
            raise ValueError("Already in this gear or invalid gear number.")

        self._curr_gear = new_gear
        return True


class Bicycle(Bike):
    """
    Class defining a Bicycle (extending Bike) that can be ridden, have its
    gear changed and has a bell that can be rung.

    Attributes:
        seats: number of seats the bike has
        gears: number of gears the bike has
        bell_sound: sound the bell makes when rung
    """

    def __init__(self, seats=1, gears=7, bell_sound="ring ring"):
        """
        Creates a new Bike object.

        Args:
            seats: number of seats the bicycle has, defaults to 1
            gears: number of gears the bicycle has, defaults to 7
            bell_sound: sound the bell makes when rung
        """

        super().__init__(seats, gears)
        self.bell_sound = bell_sound

    def ring_bell(self):
        """ Rings bicycle bell."""

        print(self.bell_sound)


class Motorbike(Bike):
    """
    Class defining a Motorbike (extending Bike) that can be ridden, have its
    gear changed and has a tank that can be filled.

    Attributes:
        seats: number of seats the bike has
        gears: number of gears the bike has
    """


    def __init__(self, seats=2, gears=5):
        """
        Creates a new Motorbike object.

        Args:
            seats: number of seats the motorbike has, defaults to 2
            gears: number of gears the motorbike has, defaults to 5
        """

        super().__init__(seats, gears)
        # True means full tank. Private so it can only be changed in
        # a controlled manner
        self._tank = True

    @property
    def tank(self):
        """
        Purpose of this function is to enable the user to check the tank
        status, but is only able to fill/empty the tank with specific methods.
        This was not necessary to implement.
        """
        return self._tank

    def start_ride(self):
        """
        Starts a motorbike ride.

        Returns:
            True if successful.
            False if motorbike is already on a ride or tank is empty
        """

        # can't ride a motorbike if tank is empty or it is already ridden
        if not self._tank or not super().start_ride():
            return False

        return True


    def end_ride(self):
        """
        Ends a motorbike ride and empties tank.

        Returns:
            True if successful.
            False if motorbike is not currently ridden.
        """

        if not super().end_ride():
            return False

        self._tank = False # tank is empty after riding
        return True


    # the following method was not necessary to implement, but we want to be
    # able to ride more than once.

    def fill_tank(self):
        """
        Fills motorbike tank with fuel.

        Returns:
            True if successful.
            False if tank already full.
        """

        # can't fill tank if already full
        if self._tank:
            return False

        self._tank = True
        return True
