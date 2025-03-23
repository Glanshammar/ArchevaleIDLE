from entities import *

class Monster:
    def __init__(self, name, health, reward):
        self.name = name
        self.health = health
        self.reward = reward

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return self.reward
        return 0

    def deal_damage(self, amount, target : LivingEntity):
        target.TakeDamage(amount)