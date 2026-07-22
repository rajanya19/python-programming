##write a python program to make a menu driven calculator application that will perform arithmetic operation on 2 numbers.

n1=float(input("enter a number:"))
n2=float(input("enter a number:"))
while True:
    print("1.addition 2.subtraction 3.multiplication 4.division 5.exit")
    choice=int(input("enter a choice:"))
    if choice==1:
        print(f'{n1}+{n2}={n1+n2}')
    elif choice==2:
        print(f'{n1}-{n2}={n1-n2}')
    elif choice==3:
        print(f'{n1}*{n2}={n1*n2}')
    elif choice==4:
        print(f'{n1}/{n2}={n1/n2}')
    elif choice==5:
        print("exit")
        break
    else:
        print("invalid choice")




##enter a number:10
##enter a number:4
##1.addition 2.subtraction 3.multiplication 4.division 5.exit
##enter a choice:1
##10.0+4.0=6.0
##1.addition 2.subtraction 3.multiplication 4.division 5.exit
##enter a choice: 3
##10.0*4.0=40.0
##1.addition 2.subtraction 3.multiplication 4.division 5.exit
##enter a choice:5
##exit

