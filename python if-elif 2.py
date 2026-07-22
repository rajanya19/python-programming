##write a python program to check a whether a year is leap year or not.

n=int(input("enter a year:"))
if n%4==0 and n%100!=0 and n%400==0:
    print(n,"is a leap year.")
else:
    print(n,"is not a leap year.")


##enter a year:2007
## 2007 is not a leap year.
