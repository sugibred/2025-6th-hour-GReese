#Name:
#Class: 5th Hour
#Assignment: HW2

#int = number
#str = word
#bool = true or false
#1. Print "Hello World!"
print('Hello World')
#2. Create three different variables with distinct names and values: one with an integer, one with a string, one with a boolean.
chicken = 5
turkey = 'food'
blue_jay = True
#3. Print all three variables on the same print function (at the same time).
print(chicken,turkey,blue_jay)
#4. Create a variable that asks the user to input an integer.
number_for_thing = int(input("Enter a number: "))
#5. Add the integer variable from #2 with the integer from #4 and print the result.
number_5_res = (chicken + number_for_thing)
print(number_5_res)
#6. Take the result from #5 and divide it by 2. Print the result.
division_res = (number_5_res / 2)
print(division_res)
#7. Change the value of the boolean variable to the opposite value (if true then make false, or vice versa).
blue_jay = False
#8. Print the value of the boolean variable.
print(blue_jay)
#9. Create a variable with a number that contains decimals.
decimal_number = 6.65
#10. Round the number from #9 up or down using the round function.
print(round(decimal_number))