#Reverse and Extract

try:
    string = str(input("Enter string: "))
except ValueError:
    print("Invalid Input! Only Accepts Strings!")
    exit()

rev = string[::-1]

first_three_char = string[:3]
last_three_char = string[-3:]

print(f"\nThe first three characters: {first_three_char}\nThe Last three characters: {last_three_char}")

length = len(string)

print("\nCharacters at even index")
for i in range(0, length):
    if(i%2 == 0):
        print(string[i])

print("\nCharacters at odd index")
for i in range(0, length):
    if(i%2 != 0):
        print(string[i])