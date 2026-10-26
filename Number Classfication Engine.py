#Number Classfication Engine

import math

try:
    n = int(input("Enter number: "))
except ValueError:
    print("Invalid Value! Enter Integer.")
    exit()

#Check positive, negative or Zero.
if(n == 0):
    print(f"{n} is Zero.")
elif(n<0):
    print(f"{n} is negative integer.")
elif(n>0):
    print(f"{n} is Positive integer.")


#Check Even and odd

if(n%2==0):
    print(f"{n} is Even Number.")
else:
    print(f"{n} is odd number.")

#Divisible by 3, 5 or both
if(n == 0):
    print(f"{n} is divisible by 3 and 5.")
else:
    if(n%3 == 0):
        print(f"{n} is divisible by 3.")
    else:
        print(f"{n} is not divisible by 3.")

    if(n%5 == 0):
        print(f"{n} is divisible by 5.")
    else:
        print(f"{n} is not divisible by 5.")

    if(n%5 == 0 and n%3==0):
        print(f"{n} is divisible by 3 and 5 both.")
    else:
        print(f"{n} is not divisible by 3 and 5 both.")


#Perfect square
root = math.sqrt(n)

if(n < 0):
    print(f"{n} is not a perfect square root.")
    exit();

if(root * root == n):
    print(f"{n} is perfect square root.")
else:
    print(f"{n} is not a perfect square root.")
 