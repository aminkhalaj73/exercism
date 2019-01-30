import random
import math

class Character:
    def __init__(self):
        self.strength = self.roll_dice()
        self.dexterity = self.roll_dice()
        self.constitution = self.roll_dice()    
        self.intelligence = self.roll_dice()
        self.wisdom = self.roll_dice()
        self.charisma = self.roll_dice()
        self.hitpoints = 10 + modifier(self.constitution)
    

    def roll_dice(self):
        self.dice = []
        i = 0
        while i < 4 :
            self.dice.append(random.randint(1,6))
            i += 1    
        self.dice.remove(min(self.dice))
        return sum(self.dice)
    
def modifier(value):
    return math.floor((value-10)/2)