from skills import *

class Entity:
    def __init__(self):
        self.destroyed = False


class LivingEntity(Entity):
    def __init__(self, hp=1000):
        super().__init__()
        self.health = hp
        self.strength = Strength()
        self.archery = Archery()
        self.magic = Magic()


class Player(LivingEntity):
    def __init__(self):
        super().__init__()
        self.woodcutting = Woodcutting()
        self.fishing = Fishing()

class Goblin(LivingEntity):
    def __init__(self, hp=800):
        super().__init__(hp)
