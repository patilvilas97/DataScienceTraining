Fruits = ["Orange", "Banana", "Apple", "Kiwi"]
print(Fruits[1])
Fruits.append("Grapes")                         ##Inserting Element at the End
print(Fruits)
Fruits.insert(1,"Watermelon")                   ##Inserting the element at any index
print(Fruits)
Vegetables = ["Potato", "Corriander", "Onion"]
toBuy = Fruits
toBuy.insert(1, Vegetables)                     ##Inserting list into list
print(toBuy)
print(toBuy[0])
print(toBuy[1][2])
