#snake,water,gun game
import random

def game(comp,you):
    # if two valuesn  are equal,declare a tie!
    if comp == you:
        return None
    
# check for all possibitlitues
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True


print("computer turn: Snake(s) water(w) and Gun(g)?")
randno =random.randint(1,3)
if randno==1:
    comp='s'
if randno==2:
    comp='w'
if randno==3:
    comp='g'
    
    

you=input("you turn: Snake(s) water(w) and Gun(g)?")

a=game(comp,you)

print(f"comp chose {comp}")
print(f"you chose {you}")

if a==(None):
    print("the game is a tie!")
elif a:
    print("you win")
else:
    print("you lose")
