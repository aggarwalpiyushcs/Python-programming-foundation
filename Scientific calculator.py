#Scientific calculator

print("\n==========Scientific Calculator============\n")
print("\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Power\n7.Absolute value\n8. Floor Division\n0. Exit")

def get_two_numbers():
    try:
        a = float(input("Enter number one: "))
        b = float(input("Enter number two: "))
    except ValueError:
        print("Invalid Values!")
        exit()

def get_one_numbers():
    try:
        a = float(input("Enter number one: "))
    except ValueError:
        print("Invalid Values!")
        exit()
     

def addition(a, b):
    sum = a + b
    return sum

def substraction(a, b):
    sub = a - b
    return sub

def multiplication(a, b):
    mul = a * b
    return mul

def division(a, b):
    if(b == 0):
        print("Invalid Values!")
        exit()


