
def checkLetter(question):
    char = input("Enter a Character : ")[0]
    for i in range(len(question)):
        if question[i] == char:
            word[i] = char  ##abcdef
            flag = True
    return flag

def winnerOrLoser(word):
    s = ""
    for i in word:
        s += i
    if question==s:
        print("You are a Winner!!")
        return 1


question = "elephant"
chances = len(question)
# chances = guesses
# temp="--------"
word=["-","-","-","-","-","-","-","-"]
while chances != 0 :
    flag = False
    print("------------------------------------------------------------------------------------")
    print("----------------------------------Start---------------------------------------------")
    print("Your chances left are :", chances)
    print(word)
    flag = checkLetter(question)
    if winnerOrLoser(word) == 1:
        break
    if flag==False:
        chances -= 1

