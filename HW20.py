#Name: Gregg
#Class: 6th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class storage:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double(self):
         self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
apple = storage(12, 10, 1)
pear = storage(5, 12, 2)
mangoes = storage(18, 15, 3)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"apple amount {apple.stock}")
print(f"pear amount {pear.stock}")
print(f"pear cost ${pear.cost}")
print(f"mango amount {mangoes.stock}")
#4. Make a def function within the class that doubles the cost of an item, double the cost of the second store item, and print the new cost below the original cost print statement.
pear.double()
print(f"pear cost ${pear.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
mangoes.stock /= 4
mangoes.stock = round(mangoes.stock)
print(mangoes.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del apple
try:
    print(f"weight of the apple {apple.weight}")
except NameError:
    print("no apple😔😔😔😔")