from time import sleep

class Quest:
    def __init__(self, name, description, reward):
        self.name = name
        self.description = description
        self.reward = reward
        self.status = "Available"

    def start_quest(self):
        self.status = "In Progress"

    def complete_quest(self):
        self.status = "Completed"

    def questing(self):
        while True:
            print('Questing...')
            sleep(1)