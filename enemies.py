import random

class Monster:
    def __init__(self, hp, strength):
        self.hp = hp
        self.strength = strength

    def take_damage(self, damage):
        self.hp -= damage

    def deal_damage(self, opponent):
        opponent.take_damage(random.randint(0, self.strength))

class Boss(Monster):
    def __init__(self, hp, strength):
        super().__init__(hp, strength)
        
