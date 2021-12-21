question = "elephant"
chances = len(question)
# chances = guesses
# temp="--------"
word=["-","-","-","-","-","-","-","-"]
while chances != 0 :
    print("------------------------------------------------------------------------------------")
    print("----------------------------------Start---------------------------------------------")
    print("Your chances left are :", chances)
    print(word)
    char = list(input("Enter a Character : ")[0])
    for i in range(len(question)):
        if question[i]==char:
            print(word[i])
            word[i] == char         ##abcdef
            print(word[i])

    if question==word:
        print("You are a Winner!!")
        break
    else:
        chances = chances-1
