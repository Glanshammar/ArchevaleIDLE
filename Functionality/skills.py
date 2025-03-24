class Skill:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.level : int = 0
        self.xp : int = 0

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.get_xp_to_next_level():
            self.level_up()

    def level_up(self):
        self.level += 1

    def get_xp_to_next_level(self):
        return 100 * self.level

class Woodcutting(Skill):
    def __init__(self):
        super().__init__("Woodcutting", "A skill for cutting trees.")
        self.level : int = 120
        self.xp : int = 200000000

class Fishing(Skill):
    def __init__(self):
        super().__init__("Fishing", "A skill for catching fish.")
        self.level : int = 99
        self.xp : int = 13034431

class Strength(Skill):
    def __init__(self):
        super().__init__("Strength", "Determines your ability to lift heavy object and dealing physical damage.")

class Magic(Skill):
    def __init__(self):
        super().__init__("Fishing", "Create magical items and make enchantments, and cast magical spells both offensive and defensive.")

class Archery(Skill):
    def __init__(self):
        super().__init__("Fishing", "A combat skill for bows, crossbows and other projectile weaponry.")