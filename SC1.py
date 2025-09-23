#Name:Gregg
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
enemies={
        'slime' : {
            'health' : 30,
            'armor' : 10,
            'speed' : 10,
            'damage' : 5,
        },
        'skeleton' : {
            'health' : 50,
            'armor' : 20,
            'speed' : 8,
            'damage' : 10,
        },
        'zombie' : {
            'health' : 52,
            'armor' : 18,
            'speed' : 5,
            'damage' : 12,
        },
        'golem' : {
            'health' : 100,
            'armor' : 50,
            'speed' : 7,
            'damage' : 50,
        },
        'Slime_King' : {
            'health' : 1000,
            'armor' : 100,
            'speed' : 15,
            'damage' : 150,
        }
}
userchoice=input('slime, skeleton, zombie, golem, Slime_King: ')
print(enemies[userchoice])
enemies[userchoice].update({'damage' : int(input('choose damage:'))})
print(userchoice,enemies[userchoice])