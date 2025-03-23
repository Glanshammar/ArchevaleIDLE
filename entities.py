class Entity:
    def __init__(self):
        self.health = 1000
        self.destroyed = False
    
    def Destroyed(self):
        if self.health == 0:
            self.destroyed = True


class LivingEntity(Entity):
    def __init__(self, levels=[0,0,0]):
        super().__init__()
        self.strength_level = levels[0]
        self.archery_level = levels[1]
        self.magic_level = levels[2]
    
    def TakeDamage(self, amount):
        self.health -= amount
    
    def DealDamage(self, amount, target: Entity):
        target.TakeDamage(amount)


class Player(LivingEntity):
    def __init__(self):
        super().__init__()
        self.woodcutting_level = 0
        self.woodcutting_xp = 0

class Goblin(LivingEntity):
    pass
