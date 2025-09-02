#Name:Gregg
#Class: 6th Hour
#Assignment: HW4


#1. Print Hello World!
print('hello world')
#1. Create a list with 5 strings containing 5 different names in it.
five_names=['Kash', 'Gregg', 'Shanuel', 'Ben', 'Hubert Cumberdale']
#2. Append a new name onto the Name List.
five_names.append('john door')
#3. Print out the 4th name on the list.
print(five_names[3])
#4. Create a list with 4 different integers in it.
number_list=[5,8,6,7]
#5. Insert a new integer into the 2nd spot and print the new list.
number_list.insert(1, 3)
#6. Sort the list from lowest to highest and print the sorted list.
number_list.sort()
#7. Add the 1st three numbers on the sorted list together and print the sum.
print(number_list[0] + number_list[1] + number_list[2])
print(sum(number_list))
#8. Create a list with two strings, two variables, and too boolean values.
rando_list=['Kash','Shane', 6, 7, True, False]
print(rando_list)
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(rando_list[int(input('choose 0-5:'))])