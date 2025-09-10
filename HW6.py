#Name:Gregg Reese
#Class: 6th Hour
#Assignment: HW6


#1. Import the "random" library
import random
#2. print "Hello World!"
print('Hello World')
#3. Create three different variables that each randomly generate an integer between 1 and 10
rando_one = random.randint(1,10)
rando_two = random.randint(1,10)
rando_three = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(rando_one, rando_two, rando_three)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
add_var = rando_one + 2
sub_var = rando_two - 4
mul_var = rando_three * 1.5

#6. Print each result from #5 on the same line.
print(add_var, sub_var, mul_var)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
var_one = random.randint(1,6)
var_two = random.randint(1,6)
var_three = random.randint(1,6)
var_four = random.randint(1,6)
randy_list = [var_one, var_two, var_three, var_four]
#8. Sort the list in #7 and print it.
randy_list.sort()
print(randy_list)
#9. Add together the highest three numbers in the list from #7 and print the result.
high_three = randy_list[1]+randy_list[2]+randy_list[3]
print(high_three)
#10. Create a list with 5 names of other students in this class and print the list.
name_list = ['Kash', 'Shane','Ally', 'Ethan', 'Brody']
#11. Shuffle the list in #10 and print the list again.
random.shuffle(name_list)
print(name_list)
#12. Print a random choice from the list of names from #10.
print(random.choice(name_list))