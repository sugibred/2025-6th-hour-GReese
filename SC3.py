#Name:
#Class: 6th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

players = int(input("Enter number of players: "))

total = 0

for i in range(1,players+1):
    rate = int(input("Enter rating: "))
    while rate < 1 or rate > 5:
        print('rating must be between 1 and 5')
        rate = int(input("rate this beauty: "))
    else:
        total += rate
average = total / players

print(average)