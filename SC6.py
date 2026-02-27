#Name:Gregg
#Class: 6th Hour
#Assignment: Scenario 6

import random

#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)
class characters:
    def __init__(self, name, hp, init, ac, atkmod, damage, frt):
        self.name = name
        self.hp = hp
        self.init = init
        self.ac = ac
        self.atkmod = atkmod
        self.damage = damage
        self.frt = frt

laezel = characters('LaeZel', 48, 1, 17, 6, random.randint(1,6) + random.randint(1,6) + 3, 0)
goblin = characters('Goblin', 7, 0, 12, 4, random.randint(1,6) + 2, 0)

'''def damage_roll(self):
        dmg_rll = self.damage'''
def init_roll(self):

    self.frt = random.randint(1,20) + self.init
    print(f"{self.name} rolled a {self.frt}")

    if laezel.frt >= goblin.frt:
        print ("laezel goes first")
        roll_damage(laezel)


def roll_damage(self):
    total = 0
    roll = random.randint(1,20)
    if roll == 1:
        print(f'{self.name} rolled a one. automatic forfeit')
        return

    else:
        hitvalue = roll + self.damage

        '''if roll == 20:
            print(f'{self.name} rolled a nat 20. double damage.')
            dmg_dealt = self.damage * 2
        elif hitvalue >='''
init_roll(laezel)
init_roll(goblin)


