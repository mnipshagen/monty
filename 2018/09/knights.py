import random


MAX_ATTRIBUTE_POINTS = 20
ATTRIBUTES = ['Vitality', 'Strength', 'Luck']


class KnightError(Exception): pass


class Knight:

    def __init__(self, name, vitality, strength, luck):
        used_points = vitality + strength + luck
        if (used_points != MAX_ATTRIBUTE_POINTS):
            raise KnightError(f"{used_points} is not equal to attribute points {MAX_ATTRIBUTE_POINTS}")
        self.name = name
        self.vitality = int(MAX_ATTRIBUTE_POINTS * 1.5) + int(1.4 * vitality)
        self._health = self.vitality
        self.strength = strength
        self.luck = 2*luck
        self.crit_modifier = 3
        self.available_actions = [self.light_attack, self.heavy_hit]

    def alive(self):
        return self.health > 0

    @property
    def health(self):
        return self._health

    def take_damage(self, damage):
        self._health -= damage

    def heal(self, amount):
        self._health = min(self.health + amount, self.vitality)

    def light_attack(self):
        crit = random.randint(0,99) < self.luck*2
        return int((1 + 0.15 * self.strength) * self.crit_modifier ** (int(crit))), crit

    def heavy_hit(self):
        crit = random.randint(0, 99) < self.luck
        return int(((3 + 0.4 * self.strength)) * self.crit_modifier ** (int(crit))), crit

    def all_actions(self):
        return self.available_actions
    
    def __str__(self):
        return self.name

    def description():
        return "This is the basic knight. There are the basic attributes and two attacks."


class BlackKnight(Knight):

    def __init__(self, name, vitality, strength, luck):
        super().__init__(name, vitality, strength, luck)
        self.available_actions += [self.execute]

    def execute(self):
        return 0, False

    def description():
        return ("The black knight is a dangerous foe, who deals 1.8 times "
            "damage, but cannot crit")
