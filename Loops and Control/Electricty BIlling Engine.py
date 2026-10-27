#Electricty BIlling Engine

try:
    units = int(input("Enter total number of units consumed: "))
    month = str(input("Enter month: "))
except ValueError:
    print("Invalid Input! Input can only be integer.")
    exit()

if(units < 0):
    print("Invalid Input! Input cannot be negative.")
    exit()

fixed_charge = 100
bill = 0

if(units > 0 and units <= 100):
    bill = units * 2
elif(units > 100 and units <= 300):
    bill = (200 + (units - 100)*3)
elif(units > 300 and units <=600):
    bill = (800 + (units - 300)*5)
elif(units > 600):
    bill = (2300 + (units - 600)*8)

bill_after_fixed = bill + fixed_charge

if(bill_after_fixed > 3000):
    energy_charge = ((bill_after_fixed * 5)/100)
    final_bill = bill_after_fixed + energy_charge
else:
    energy_charge = 0
    final_bill = bill_after_fixed

print("\n")
print(f"==========={month} Electricity Bill=============\n")
print(f"Energy Charge: \t{bill} Rs.")
print(f"Fixed charges: \t{fixed_charge} Rs.")
print(f"Surcharge: \t{energy_charge} Rs.")
print(f"Final Bill: \t{final_bill} Rs.")




