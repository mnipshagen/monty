import random

class Car: #(Object, Vehicle, MoreParents):
    """This class represents a car that can drive from A to B"""

    def _consume_fuel(self, amount):
        """Reduces fuel by amount to a minimum of 0"""
        self.current_fuel -= amount
        self.current_fuel = max(self.current_fuel, 0)

    def __init__(self, 
            brand="santa's sledge", 
            colour="snow white", 
            location="northpole",
            no_of_passenger=1, # elves do not count
            fuel='reindeers',
            fuel_capacity=9):
        self.brand = brand
        self.colour = colour
        self.location = location
        self.no_of_passenger = no_of_passenger
        self.fuel = fuel
        self.fuel_capacity = fuel_capacity
        self.current_fuel = fuel_capacity
        self.driving = False
        self.doors_open = False

    def drive(self, location):
        if (self.fuel_capacity != 0 and not self.doors_open):
            self.driving = True
            self.target_location = location
    
    def arrive(self):
        if self.driving:
            self._consume_fuel(self.current_fuel/2)
            self.driving = False
            self.location = self.target_location

    def doors(self):
        if not self.driving:
            self.doors_open = not self.doors_open
        return self.doors_open

    def fill_tank(self):
        if not self.driving:
            self.current_fuel = self.fuel_capacity

    def __str__(self):
        percentage = self.current_fuel / self.fuel_capacity * 100
        return (f"This is a {self.colour} car by {self.brand} "
               f"in {self.location}, which is currently"
               f"{'' if self.driving else ' not'} driving and "
               f"the tank is filled by {percentage}%")

# constructing a new one
c = Car('Tesla', 'red', 'space', 4, 'electricity', 53)
print(c)


class MyClass:

    def __init__(self):
        _internal_list = list()
        _hidden_prop = 0

    @property
    def the_list(self):
        # returns a shallow copy
        return self._internal_list[:] 
    
    @the_list.deleter
    def the_list(self):
        self._internal_list = list()

    @property
    def prop(self):
        return _hidden_prop
    
    @prop.setter
    def prop(self, value):
        if value < 0:
            raise ValueError("No negative values allowed.")
        self._hidden_prop = value

    @prop.deleter
    def prop(self):
        self._hidden_prop = 0


class Phone:

     def __init__(self, number):
        self.number = number
        self.busy = False
        self.microphone = False
        
     def call(self, recipient_phone):
         if recipient_phone.receive_call(self):
            self.busy = True
            self.microphone = True
             return True
         return False
        
     def receive_call(self):
         if not self.busy:
            self.busy = True
            self.microphone = True
             return True
         return False


class MobilePhone(Phone):
    
     def __init__(self, number, res_x, res_y):
        super().__init__(number)
        # use Screen class we haven't defined here
        self.screen = Screen(res_x, res_y)
      
     def receive_call(self, caller_phone):
         if super().receive_call():
            self.show_number(caller_phone)   # add this functionality
             return True
         return False
    
     def show_number(self, caller_phone):  # this function is new
        self.screen.display(caller_phone.number)

def receive_call(self, caller_phone):
     if super().receive_call():
        self.show_number(caller_phone) # add this functionality
        return True
     return False

def receive_call(self):
    if not self.busy:
       self.busy = True
       self.microphone = True
        return True
    return False






class Circle:
    
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius**2

class Tire(Circle):
    
    def __init__(self, radius, outer_radius):
        super().__init__(outer_radius)
        self._radius = radius
        self._outer_radius = outer_radius
