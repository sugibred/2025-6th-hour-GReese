#Name:Gregg
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print("Hello World!")
#2. Create an empty list.
emtlist = []
#3. Create a list that contains the names of everyone in the classroom.
studentslist = ["Gregg","Ally","Shane","Devon","Ethan","Conner","tristan"]
#4. Print the list from #3, sort the list, then print the list again.
print(studentslist)
studentslist.sort()
print(studentslist)
#5. Append 5 different integers into the empty list from #2 and print the list.
emtlist.append(1)
emtlist.append(11)
emtlist.append(12)
emtlist.append(1574835268974362598)
emtlist.append(-1)
print(emtlist)
#6. Add together the middle three numbers in the list from #2 and print the result.
add_list = emtlist[1]+emtlist[2]+emtlist[3]
print(add_list)
#7. Remove the very first number in the list from #2. Print the new first number.
emtlist.remove(emtlist[0])
print(emtlist[0])
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
mylife = {
    "name": "Greg",
    "grade" : "12",
     "fav_color" : "Purple"}

#9. Using the update function, add a fourth key and value determining your favorite candy.
mylife.update({"FAv CAndu" : "Andies"})
#10. Print ONLY the values of the dictionary from #8.
print(mylife.values())