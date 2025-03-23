from entities import *

class Combat:
    def __init__(self, target1 : LivingEntity, target2 : LivingEntity):
        self.target1 = target1
        self.target2 = target2
    
    def DealDamage(self, amount, target: LivingEntity):
        target.health -= amount
