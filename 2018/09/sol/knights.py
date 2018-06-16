"""
This module provides several knight classes that are able to deal and take damage.

It also provides the two constants MAX_ATTRIBUTE_POINTS and ATTRIBUTES.
The former holds how many attribute points each knight has to (!) use. The latter
holds a list or available attributes. They are in the order in which they have
to be supplied to the knight constructor.
"""

import random


MAX_ATTRIBUTE_POINTS = 20
ATTRIBUTES = ['Vitality', 'Strength', 'Luck']


class KnightError(Exception):
    """Custom Error to be raised for wrong handling of a knight."""
    pass


class Knight:
    """
    A super sweet basic knight to be your champion!
    
    Attributes:
        - name: The name of the knight
        - vitality: 
            The maximum health of the knight (Influenced by the knights vitality points)
        - health: the current health of the knight
        - strength: the strength of the knight (influences damage)
        - luck: the luck of the knight (influences critical strike)
    """

    def __init__(self, name, vitality, strength, luck):
        """
        Initialises the knight with the attributes.

        The final attributes are calculated with the spread of the 
        corresponding attribute points.

        Vitality:
            1.5 * MAX_ATTRIBUTE POINTS, so that the knight has health even
            if the knight has 0 vitality points + 1.4 * the vitality of the
            knight.
        Luck: 2 * the luck attribute points
        

        Args:
            name: The name of the knight
            vitality: The vitality points of the knight
            strength: The strength points of the knight
            luck: The luck points of the knight

        Raises:
            KnightError: If the attribute spread is wrong.
        """
        used_points = vitality + strength + luck
        if (used_points != MAX_ATTRIBUTE_POINTS):
            raise KnightError(f"{used_points} is not equal to attribute points {MAX_ATTRIBUTE_POINTS}")
        self.name = name
        self.vitality = int(MAX_ATTRIBUTE_POINTS * 1.5) + int(1.4 * vitality)
        self._health = self.vitality
        self.strength = strength
        self.luck = 2*luck
        self._crit_modifier = 3
        self._available_actions = [self.light_attack, self.heavy_hit]

    def alive(self):
        """Returns True if the knight is alive, False otherwise."""
        return self.health > 0

    @property
    def health(self):
        """
        Wrapper for private property.

        Allows read access to the private property _health in the form of
        property health.
        """
        return self._health

    def take_damage(self, damage):
        """
        Reduces the health of the knight by damage.

        Args:
            damage: the damage to take
        """
        self._health -= damage

    def light_attack(self):
        """
        A light attack with less damage but higher crit chance.

        The crit is calculated in a single roll. A random int is drawn and 
        compared to the luck of the knight * 2. If it is below that value, the 
        attack strikes critical.

        Returns:
            Tuple of damage the attack does and whether it was a critical strike
        """
        crit = random.randint(0,99) < self.luck*2
        # to the power of int(crit) is used, since crit is a bool. If crit is True,
        # this cast will result in 1, and in 0 otherwise. If the exponent is 0, the
        # crit modifier will be 1, and have no influence on the calculation. If the
        # cast results in 1, the attack will be multiplied by the crit modifier.
        return 1 + int((.5 + 0.2 * self.strength) * self._crit_modifier ** (int(crit))), crit

    def heavy_hit(self):
        """
        A heavier attack with higher damage but less critical chance.

        The crit is calculated in a single roll. A random int is drawn and 
        compared to the luck of the knight. If it is below that value, the 
        attack strikes critical.

        Returns:
            Tuple of damage the attack does and whether it was a critical strike
        """
        crit = random.randint(0, 99) < self.luck
        return int(((3 + 0.4 * self.strength)) * self._crit_modifier ** (int(crit))), crit

    def all_actions(self):
        """Returns a list of available actions the knight can take."""
        return self._available_actions
    
    def __str__(self):
        """Returns the name of the knight as identifier."""
        return self.name

    def description():
        """
        Returns a short description of the knight.

        A method only available to the class and not to the instance.
        """
        return "This is the basic knight. There are the basic attributes and two attacks."


class BlackKnight(Knight):
    """
    A mysterious black knight!

    Attributes:
        - name: The name of the black knight
        - vitality:
            The maximum health of the knight (Influenced by the knights vitality points)
        - health: the current health of the knight
        - strength: the strength of the knight (influences damage)
        - luck: the luck of the knight (influences critical strike)
    """

    def __init__(self, name, vitality, strength, luck):
        """
        Initialises the knight with the attributes.

        The final attributes are calculated with the spread of the 
        corresponding attribute points.

        Vitality:
            1.5 * MAX_ATTRIBUTE POINTS, so that the knight has health even
            if the knight has 0 vitality points + 1.4 * the vitality of the
            knight.
        Luck: Set to 0. The black knight cannot crit.
        

        Args:
            name: The name of the knight
            vitality: The vitality points of the knight
            strength: The strength points of the knight
            luck: The luck points of the knight

        Raises:
            KnightError: If the attribute spread is wrong.
        """
        super().__init__(name, vitality, strength, luck)
        self.luck = 0

    def light_attack(self):
        """
        A light attack with less damage.

        The damage calculation is the same as in the super class, but then
        multiplied by 1.4.

        Returns:
            Tuple of damage the attack does and whether it was a critical strike
        """
        dmg, crit = super().light_attack()
        dmg *= 1.4
        return int(dmg), crit

    def heavy_hit(self):
        """
        A heavier attack with more damage.

        The damage calculation is the same as in the super class, but then
        multiplied by 1.4.

        Returns:
            Tuple of damage the attack does and whether it was a critical strike
        """
        dmg, crit = super().heavy_hit()
        dmg *= 1.4
        return int(dmg), crit

    def description():
        """
        Returns a short description of the black knight.

        A method only available to the class and not to the instance.
        """
        return ("The black knight is a dangerous foe, who deals 1.4 times "
            "damage, but cannot crit")


class Paladin(Knight):
    """
    As a zealot of the gods, the paladin fights as your champion!
    
    Attributes:
        - name: The name of the knight
        - vitality: 
            The maximum health of the knight (Influenced by the knights vitality points)
        - health: the current health of the knight
        - strength: the strength of the knight (influences damage)
        - luck: the luck of the knight (influences critical strike)
    """

    def __init__(self, name, vitality, strength, luck):
        """
        Initialises the knight with the attributes.

        The final attributes are calculated with the spread of the 
        corresponding attribute points.

        Vitality:
            1.5 * MAX_ATTRIBUTE POINTS, so that the knight has health even
            if the knight has 0 vitality points + 1.1 * the vitality of the
            knight. It is less than the base class.
        
        It deletes the heavy hit from the available actions and adds the heal
        instead, since the paladin cannot hit heavily.

        Args:
            name: The name of the knight
            vitality: The vitality points of the knight
            strength: The strength points of the knight
            luck: The luck points of the knight

        Raises:
            KnightError: If the attribute spread is wrong.
        """
        super().__init__(name, vitality, strength, luck)
        self.vitality = int(1.5 * MAX_ATTRIBUTE_POINTS) + int(1.1 * vitality)
        self._health = self.vitality
        self._available_heals = 5
        del self._available_actions[self._available_actions.index(self.heavy_hit)]
        self._available_actions += [self.heal]

    def heal(self):
        """
        Heals the paladin and can overheal. Available a limited time.

        If heals are available, the Paladin heals himself for 20% of his
        max health + half of his missing health. The heal can critically
        strike and overheal the paladin beyond the max health.

        It defaults to the light attack if no heals are available.

        Returns:
            0 and whether it was a critical strike, if the paladin healed.
            Otherwise, returns what light attack will return.
        """
        if self._available_heals > 0:
            self._available_heals -= 1
            crit = random.randint(0, 99) < self.luck
            self._health += int(
                self.vitality * .2 +
                (self.vitality - self._health)/2 *
                (self._crit_modifier/2+1)) ** (int(crit)
            )
            return 0, crit
        else:
             return self.light_attack()

    def description():
        """
        Returns a short description of the paladin.

        A method only available to the class and not to the instance.
        """
        return (
            "Paladins scale worse with vitality and cannot use heavy hit, but they can heal "
            "themselves. Healing is more effective the less health the paladin has and can "
            "critically strike. Crits  overheal paladins going over their max health. A "
            "paladin can heal up to 5 times per battle. When a paladin cannot heal anymore "
            "their heals turn into light attacks."
        )
