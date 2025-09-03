#Name:Gregg
#Class: 6th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
Num_list=[1,2,3,4,5,6,7,8,9]
#2. Sort the list from highest to lowest.
Num_list.sort(reverse=True)
#3. Create an empty list.
empty_list=[]
#4. Remove the median number from the first list and add it to the second list.
Whatever=Num_list[4]
Num_list.pop(4)
empty_list.append(Whatever)
#5. Remove the first number from the first list and add it to the second list.
Whatever2=Num_list[0]
Num_list.pop(0)
empty_list.append(Whatever2)
#6. Print both lists.
print(Num_list)
print(empty_list)
#7. Add the two numbers in the second list together and print the result.
Whateveroutcome=empty_list[0]+empty_list[1]
print(Whateveroutcome)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
empty_list.pop(0)
empty_list.pop(0)
Num_list.append(Whateveroutcome)
#9. Sort the first list from lowest to highest and print it.
Num_list.sort()
print(Num_list)