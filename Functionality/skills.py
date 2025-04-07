import os
import json

xp_reqs = [100, 210, 331, 464, 610, 770, 946, 1139, 1351, 1584, 1840, 2121, 2430, 2769, 3141, 3550, 3999, 4492, 5034, 5630, 6285, 7005, 7797, 8668, 9626, 10679, 11837, 13110, 14510, 16050, 17744, 19607, 21656, 23909, 26387, 29112, 32109, 35405, 39030, 43017, 47402, 52225, 57530, 63365, 69783, 76842, 84606, 93146, 102540, 112873, 124239, 136741, 150493, 165620, 182259, 200561, 220693, 242838, 267197, 293991, 323464, 355884, 391546, 430774, 473924, 521389, 573600, 631032, 694207, 763699, 840140, 924225, 1016718, 1118460, 1230376, 1353483, 1488900, 1637858, 1801711, 1981949, 2180210, 2398297, 2638192, 2902076, 3192348, 3511647, 3862875, 4249225, 4674210, 5141693, 5655924, 6221578, 6843797, 7528237, 8281121, 9109293, 10020282, 11022369, 12124664, 13337188, 14670964, 16138117, 17751985, 19527239, 21480018, 23628074, 25990935, 28590082, 31449143, 34594110, 38053573, 41858982, 46044931, 50649474, 55714471, 61285967, 67414612, 74156121, 81571780, 89729004, 98701950, 108572190, 119429454, 131372444, 144509733, 158960750, 174856868, 192342597, 211576898, 232734629, 256008133, 281608987, 309769926, 340746958, 374821693, 412303901, 453534329, 498887799, 548776616, 603654314, 664019781, 730421794, 803464008, 883810443, 972191521, 1069410706, 1176351809, 1293987022, 1423385756, 1565724363]


class Skill:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.level : int = 0
        self.xp : int = 0

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= xp_reqs[self.level]:
            self.level += 1
            print(f"Congrats, level up! You're not level {self.level} {self.name}!")


class Woodcutting(Skill):
    def __init__(self):
        super().__init__("Woodcutting", "A skill for cutting trees.")
        self.level : int = 0
        self.xp : int = 0


class Fishing(Skill):
    def __init__(self):
        super().__init__("Fishing", "A skill for catching fish.")
        self.level : int = 0
        self.xp : int = 0

class Strength(Skill):
    def __init__(self):
        super().__init__("Strength", "Determines your ability to lift heavy object and dealing physical damage.")

class Magic(Skill):
    def __init__(self):
        super().__init__("Fishing", "Create magical items and make enchantments, and cast magical spells both offensive and defensive.")

class Archery(Skill):
    def __init__(self):
        super().__init__("Fishing", "A combat skill for bows, crossbows and other projectile weaponry.")

