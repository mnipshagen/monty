class Dinosaur:
    """
    Class defining a dinosaur that can sleep, wake up and eat.

    Attributes:
        height: dino height in meters
        weight: dino weight in kilograms
        legs: on how many legs the dino is walking
        food: food preferences (diet)
        asleep: True if dino is currently sleeping
        hungry: True if dino is currently hungry
    """

    def __init__(self, height, weight, legs, food):
        """
        Creates a new dino object

        Args:
            height: dino height in meters
            weight: dino weight in kilograms
            legs: on how many legs the dino is walking
            food: food preferences (diet)
        """

        self.height = height
        self.weight = weight
        self.legs = legs
        self.food = food
        self.asleep = False
        self.hungry = True

    def sleep(self):
        """
        Makes the dino go to sleep by setting asleep to True

        Returns:
            True if dino successfully went to sleep
            False if dino is already asleep
        """

        if self.asleep:
            return False
        self.asleep = True
        return True

    def wake_up(self):
        """
        Makes the dino wake up by setting asleep to False.
        Makes the dino hungry.

        Returns:
            True if dino successfully woke up
            False if dino is already awake
        """

        if not self.asleep:
                return False
        self.asleep = False
        self.hungry = True
        return True

    def eat(self):
        """
        Makes the dino eat and sets hungry to False

        Returns:
            True if dino successfully ate
            False if dino is not hungry
        """

        if not self.hungry:
            return False
        self.hungry = False
        return True



class Sauropod(Dinosaur):
    """
    Class defining a sauropod that can sleep, wake up, eat and headbang

    Attributes:
        height: dino height in meters
        weight: dino weight in kilograms
        legs: on how many legs the dino is walking, automatically set to 4
        food: food preferences (diet), automatically set to herbivore
        asleep: True if dino is currently sleeping
        hungry: True if dino is currently hungry
        head_position: 'up' or 'down'
    """

    def __init__(self, height, weight):
        """
        Creates a new dino object of type sauropod

        Args:
            height: dino height in meters
            weight: dino weight in kilograms
        """
        super().__init__(height, weight, legs=4, food='herbivore')
        self.head_position = 'up'

    def headbang(self,n):
        """
        Makes dino go into party mode

        Args:
            n: Number of times the head goes down and up
        """

        print('Party!')

        for i in range(n):
            self.head_position = 'down'
            self.head_position = 'up'



class Theropod(Dinosaur):
    """
    Class defining a theropod that can sleep, wake up, eat and hunt

    Attributes:
        height: dino height in meters
        weight: dino weight in kilograms
        legs: on how many legs the dino is walking, automatically set to 2
        food: food preferences (diet), automatically set to carnivore
        asleep: True if dino is currently sleeping
        hungry: True if dino is currently hungry
    """

    def __init__(self, height, weight):
        """
        Creates a new dino object of type theropod

        Args:
            height: dino height in meters
            weight: dino weight in kilograms
        """
        super().__init__(height, weight, legs=2, food='carnivore')

    def hunt(self):
        """Makes the dino go look for food saying 'Chomp Chomp'"""

        print("Chomp Chomp")



class Brachiosaurus(Sauropod):
    """
    Class defining a Brachiosaurus that can sleep, wake up, eat and headbang

    Attributes:
        height: dino height in meters, automatically set to 12
        weight: dino weight in kilograms, automatically set to 42000
        legs: on how many legs the dino is walking, automatically set to 4
        food: food preferences (diet), automatically set to herbivore
        asleep: True if dino is currently sleeping
        hungry: True if dino is currently hungry
        head_position: 'up' or 'down'
    """

    def __init__(self):
        """Creates a new dino object of type Brachiosaurus"""

        super().__init__(height=12, weight=42000)

    def headbang(self):
        """Makes dino go into party mode by headbanging exactly 10 times"""

        super().headbang(10)
