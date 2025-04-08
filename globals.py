class GameBackground:
    def __init__(self):
        self.shop = False
        self.city = False
        self.forest = False

    def set_background(self, target):
        self.shop = False
        self.city = False
        self.forest = False
        
        if target == 'shop':
            self.shop = True
        elif target == 'city':
            self.city = True
        elif target == 'forest':
            self.forest = True