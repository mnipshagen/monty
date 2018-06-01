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
        return 1 + int((.5 + 0.2 * self.strength) * self.crit_modifier ** (int(crit))), crit

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
        self.luck = 0

    def light_attack(self):
        dmg, crit = super().light_attack()
        dmg *= 1.4
        return int(dmg), crit

    def heavy_hit(self):
        dmg, crit = super().heavy_hit()
        dmg *= 1.4
        return int(dmg), crit

    def description():
        return ("The black knight is a dangerous foe, who deals 1.4 times "
            "damage, but cannot crit")


class Priest(Knight):

    def __init__(self, name, vitality, strength, luck):
        super().__init__(name, vitality, strength, luck)
        self.vitality = int(1.5 * MAX_ATTRIBUTE_POINTS) + int(1.1 * vitality)
        self._health = self.vitality
        self._available_heals = 5
        del self.available_actions[self.available_actions.index(self.heavy_hit)]
        self.available_actions += [self.heal]

    def heal(self):
        if self._available_heals > 0:
            self._available_heals -= 1
            crit = random.randint(0, 99) < self.luck
            self._health += int((self.vitality - self._health)/2 + .5) * int((self.crit_modifier/2+1)) ** (int(crit))
            return 0, crit
        else:
             return self.light_attack()

    def description():
        return (
            "Priests scale worse with vitality and cannot use heavy hit, but they can heal "
            "themselves. Healing is more effective the less health the priest has and can "
            "critically strike. Crits  overheal priests going over their max health. A "
            "priest can heal up to 5 times per battle. When a priest cannot heal anymore "
            "their heals turn into light attacks."
        )
