import random
secrect= random.randint(1,10)

while True:
    n=int(input("enter a number :"))
    if (n!=secrect):
        print("try again")
    else:
        print("well guessed!")
        break

print("exit")
        

