try:
    height = float(input("Enter height of person (centimeters): "))
    weight = float(input("Enter weight of person (kilograms): "))
except ValueError:
    print("Invalid value!")

height = height/100

if(height == 0 or height < 0):
    print("Invalid Input!\nEnter valud positive height.")
    exit()
    
if(weight == 0 or weight < 0):
    print("Invalid Input!\nEnter valid positive weight.")
    exit()

bmi = (weight/(height**2))

if(bmi < 18.5):
    print("Underweight")
elif(bmi >= 18.5 and bmi < 25):
    print("Normal")
elif(bmi >=25 and bmi < 30):
    print("Overweight")
else:
    print("Obese")