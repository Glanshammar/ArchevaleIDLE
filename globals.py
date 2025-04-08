class GameBackground:
    def __init__(self):
        self.shop = False
        self.city = False
        self.forrest = False

    def set_background(self, target):
        self.shop = False
        self.city = False
        self.forrest = False
        
        if target == 'shop':
            self.shop = True
        elif target == 'city':
            self.city = True
        elif target == 'forrest':
            self.forrest = True

gamebg = GameBackground()