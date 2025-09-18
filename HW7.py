#Name:
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print('Hello World')
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
kashscardict = {
    'brand' : 'Chevrolet',
    'model' : 'Silverado',
    'year' : [2004, 2018, 2022]
}
#3. Print the keys of the dictionary from #2.
print(kashscardict.keys())
#4. Print the values of the dictionary from #2
print(kashscardict.values())
#5. Print one of the three numbers from the list by itself
print(kashscardict['year'][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
kashscardict.update({'cost':[10000]})

#7. Print the entire dictionary from #2 with the updated key and value.
print(kashscardict)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
my_class = {
    "student_1" : {
        "Name" : "Shane",
        "Grade" : 12,
        "Sports" : False,
    },
    "student_2" : {
        "Name" : "Kash",
        "Grade" : 12,
        "Sports" : False,
    },
    "student_3" : {
        "Name" : "Brody",
        "Grade" : 11,
        "Sports" : True,
    },
}
#9. Print the names of all three classmates on the same line.
print(my_class['student_1']['Name'],my_class['student_2']['Name'],my_class['student_3']['Name'])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.