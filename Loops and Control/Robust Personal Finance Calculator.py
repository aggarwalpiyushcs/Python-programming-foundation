#Robust Personal Finacne Calculator

print("\n==========Robus Finance Calculator==========\n")
print("Give all inputs in Indian Currency i.e, Rupees\n")
try: 
    income = float(input("Enter monthly income in rupees: "))
    rent = float(input("Enter rent: "))
    food = float(input("Enter food expenses: "))
    transportation = float(input("Enter transportation expenses: "))
    other = float(input("Enter other expenses: "))
    saving_target_percentage = float(input("Enter saving target percentage: "))
except ValueError:
    print("Invalid values! Please enter the inputs correctly!")
    exit()



if(income <= 0 ):
    print("\nIncome cannot be Zero or Negative!")
    exit()

total_expenses = rent + food + transportation + other
remaining_amount = income - total_expenses

if(remaining_amount < 0):
    print("\nTotal expneses is greater than the income! You should manage your fund efficiently.")
    exit()

if(saving_target_percentage >=100 or saving_target_percentage < 0):
    print("\nSaving target percentage cannot be one hundred or greater than it or less than 0..")
    exit()

required_saving = ((saving_target_percentage * income)/100)

if(required_saving <= remaining_amount):
    print("Congratualtions! Saving Target achieved!")
else:
    print("Work hard! Saving Target not acheived")

percentage_income_spent = ((total_expenses/income)*100)

print("\n\n\n")
print("\n==========Robus Finance Calculator==========\n")
print(f"\nMonthly Income:\t{income}")
print(f"\nHouse rent:\t{rent}")
print(f"\nFood Expenses:\t{food}")
print(f"\nTransportation expenses:\t{transportation}")
print(f"\nOther Expenses:\t{other}")
print(f"\nSaving Target %:\t{saving_target_percentage}")
print(f"\nTotal Expenses:\t{total_expenses}")
print(f"\nRemaining amount:\t{remaining_amount}")
print(f"\n% Income Spent:\t{percentage_income_spent}")




