class GameBackground:
    def __init__(self):
        self.show_shop = False
        self.show_city = False
        self.show_forest = False

    def set_show(self, target):
        self.show_shop = False
        self.show_city = False
        self.show_forest = False
        
        if target == 'shop':
            self.show_shop = True
        elif target == 'city':
            self.show_city = True
        elif target == 'forest':
            self.show_forest = True