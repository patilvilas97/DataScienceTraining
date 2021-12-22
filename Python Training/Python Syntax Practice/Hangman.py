flag = False
def checkLetter(question,flag):                                 ##To check whether the entered character is present in
    char = input("Enter a Character : ")[0]                     ##the question, if present the user's guess is correct
    for i in range(len(question)):
        if question[i] == char:
            word[i] = char  ##abcdef
            flag =  True
    return flag

def winnerOrLoser(word):                                        ##To check whether our guestion is correctly solve or
    s = ""                                                      ##is pending to complete
    for i in word:
        s += i
    if question==s:
        print("You are a Winner!!")
        print(str(word))
        print("------------------------------------------------------------------------------------")
        print("------------------------------------End---------------------------------------------")
        return 1


question = "elephant"                                           ##Word to guess
chances = len(question)
word=["-","-","-","-","-","-","-","-"]
while chances != 0 :
    flag = False
    print("------------------------------------------------------------------------------------")
    print("----------------------------------Start---------------------------------------------")
    print("Your chances left are :", chances)
    print(word)
    flag = checkLetter(question,flag)
    if flag==False:
        chances -= 1
    if winnerOrLoser(word) == 1:
        break
if(chances==0):
    print("                     Sorry, Better Luck Next Time")
    print("------------------------------------------------------------------------------------")
    print("-----------------------------------End----------------------------------------------")
