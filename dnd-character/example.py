import random
import math

class dnd :
    def __init__(self):
        self.strength = self.roll_dice()
        self.dexterity = self.roll_dice()
        self.constitution = self.roll_dice()    
        self.intelligence = self.roll_dice()
        self.wisdom = self.roll_dice()
        self.charisma = self.roll_dice()
        self.hitpoints = 10 + self.constitution_modifier()
    

    def roll_dice(self):
        self.dice = []
        i = 0
        while i < 4 :
            self.dice.append(random.randint(1,6))
            i += 1    
        self.dice.remove(min(self.dice))
        return sum(self.dice)
    
    def constitution_modifier(self):
        return math.floor((self.constitution - 10)/2)

amin = dnd()
print(amin.strength)
print(amin.charisma)
print(amin.dexterity)
print(amin.charisma)
print(amin.hitpoints)
print(dnd().roll_dice())



        

# dice = []
# i = 0
# while i < 4 :
#     dice.append(random.randint(1,6))
#     i += 1

# print(dice)
# print(min(dice))
# dice.remove(min(dice))
# print(dice)
# print(sum(dice))