##write a python program to find the maximum between 3 numbers.

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
if n1>n2 and n1>n3:
    print(n1,'is maximum')
elif n2>n1 and n2>n3:
    print(n2,'is maximum')
else:
    print(n3,'is maximum')



##enter first number: 35
##enter second number:78
##enter third number:10
##78 is maximum
