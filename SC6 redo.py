#Name:Gregg
#Class: 6th Hour
#Assignment: Scenario 6

import random
from ctypes import GetLastError


#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)
class characters:
    def __init__(self, name, hp, init, ac, atkmod, damage):
        self.name = name
        self.hp = hp
        self.init = init
        self.ac = ac
        self.atkmod = atkmod
        self.damage = damage

    def laezel_dmg_roll(self):
        laezel_dmg = random.randint(1,6) + random.randint(1,6) + 3
        self.dmg = laezel_dmg

    def goblin_dmg_roll(self):
        goblin_dmg = random.randint(1,6) + random.randint(1,6) + 3
        self.dmg = goblin_dmg
laezel = characters('LaeZel', 48, 1, 17, 6, 0)
shadowheart = characters('Shadowheart', 40, 1, 18, 4, 0)
gale = characters('Gale', 32, 1, 14, 6, 0)
astarion =  characters('Astarion', 40, 3, 14, 5, 0)

goblin = characters('Goblin', 7, 0, 12, 4, 0)
orc = characters('Orc', 15, 1, 13, 5, 0)
troll = characters('Troll', 84, 1, 15, 7, 0)
mindflayer = characters('Mindflayer', 71, 1, 15, 7, 0)
dragon = characters('Dragon', 127, 2, 18, 7, 0)


def hero_attack():
    while laezel.hp >= 0 or goblin.hp >= 0:
        roll=random.randint(1,20)
        laezel.laezel_dmg_roll()
        if roll == 1:
            print (f"{laezel.name} missed")
        elif roll == 20:
            goblin.hp -= laezel.dmg * 2
            print("laezel rolled a nat 20")
        elif roll + laezel.atkmod >=goblin.ac:
            goblin.hp -= laezel.dmg
            print(f"{laezel.name} did {laezel.dmg} damage")
        else:
            print(f"{laezel.name} missed")

        if goblin.hp <= 0:
            print(f"{goblin.name} is dead")
            exit()
        else:
            print(f"Goblin has {goblin.hp} hp")
            enemy_attack()

def enemy_attack():
    while laezel.hp >= 0 or goblin.hp >= 0:
        roll = random.randint(1, 20)
        goblin.goblin_dmg_roll()
        if roll == 1:
            print(f"{goblin.name} missed")
        elif roll == 20:
            laezel.hp -= goblin.dmg * 2
            print("Goblin rolled a nat 20")
        elif roll + goblin.atkmod >= laezel.ac:
            laezel.hp -= goblin.dmg
            print(f"{goblin.name} did {goblin.dmg} damage")
        else:
            print(f"{goblin.name} missed")

        if laezel.hp <= 0:
            print(f"{laezel.name} is dead")
            exit()
        else:
            print(f"Laezel has {laezel.hp} hp")
            hero_attack()

def initiative():
    laezel_init= random.randint(1,20) + laezel.init
    goblin_init = random.randint(1, 20) + goblin.init

    if laezel_init >= goblin_init:
        print("Laezel goes first")
        hero_attack()
    else:
        print("Goblin goes first")
        enemy_attack()
initiative()