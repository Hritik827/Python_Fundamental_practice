import random
randNumber=random.randint(1,100)
# print(randNumber)
UserGuess=None
guesses=0

while(UserGuess!=randNumber):
    UserGuess=int(input("enter your guess: "))
    guesses+=1
    if(UserGuess==randNumber):
        print("you guesses it right")
    else:
        if(UserGuess>randNumber):
            print("you guesses it wrong! Enter a smaller number")
        else:
            print("you guesses it wrong!Enter a larger number")

print(f"you guessed the number in {guesses} guesses")
with open("hiscore.txt","r") as f:
    # hiscore=int(f.read())       ye f.read ye ek string hogi so integer mein typecast kiya
    hiscore=int(f.read()) 
if(guesses<hiscore):
    print("you have just broken the high score")
    with open("hiscore.txt","w") as f:
        # f.write(str(guesses))     we can't write integer in txt so convert in text
        f.write(str(guesses))