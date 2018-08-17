class Player:
    def __init__(self, hp, mana, level):
        self.hp = hp
        self.mana = mana
        self.level = level
        self.inventory = []

    def take_damage(self, damage):
        self.hp -= damage
        
    def heal(self, healing):
        self.hp += healing

    def use_mana(self, mana):
        self.mana -= mana

    def restore_mana(self, mana):
        self.mana += mana

    def level_up(self, level):
        self.level += level

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, index):
        self.inventory.pop(index)

