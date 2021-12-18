num = int(input("Enter the Number : "))
limit = int(input("Enter the Limit : "))

for i in range(1,limit+1):                      ##Prinint Multiples of a Given Number
    print(num,"*", i,"=", num*i)