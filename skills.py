class Skill:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.level = 0
        self.xp = 0

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
