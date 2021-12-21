phonebook={"bob" : 123456789, "buddy" : 789456123, "vilas" : 8554074424}
print(phonebook["bob"])

for i in phonebook:             ##printing Dictionary
    print("key :",i,",","Value :", phonebook[i], end=", ")


print("samir" in phonebook)     ##Checking is present or not
print(phonebook["vilas"])


phonebook["harshal"] = 48656331  ##Adding element in Dictionary
print(phonebook)

phonebook.pop("bob")            ##Removing Element from Dictionary
print(phonebook)