#Digital Intelligence System

try:
    n = int(input("Enter Integer: "))
except ValueError:
    print("Invalid Input! Enter Integer!")
    exit()

temp = n
temp1 = n
temp2 = n

if(n == 0):
    count = 1
    sum = 0
    product = 0
    sum_even = sum_odd = largest_digit = smallest_digit = 0
    exit()

temp1 = abs(temp1)
temp = abs(temp)
count = 0
digits = []
product = 1
sum = 0
sum_even = sum_odd = 0
reverse = 0
armstrong_sum = 0

largest_digit = 0
smallest_digit = 0

count_odd = count_even = 0


while(temp > 0):
    digit = temp % 10
    sum = sum + digit
    count = count + 1
    if(digit % 2 == 0):
        count_even = count_even + 1
        sum_even = sum_even + digit
    else:
        count_odd = count_odd + 1
        sum_odd = sum_odd + digit

    digits.append(digit)

    largest_digit = max(digits)
    smallest_digit = min(digits)

    if(digit != 0):
        product = product * digit
    temp = temp // 10

while(temp2 > 0):
    digit = temp2 % 10
    reverse = (reverse*10) + digit
    armstrong_sum = armstrong_sum + (digit ** count)
    temp1 = temp2//10

print(f"\nTotal number of digits: {count}")
print(f"Sum of Digits: {sum}")
print(f"Products of non zero: {product}")
print(f"Largest Digit: {largest_digit}")
print(f"Smallest Digit: {smallest_digit}")
print(f"Sum of Even digits: {sum_even}")
print(f"Sum of Odd Events: {sum_odd}")
print(f"Number of Even digits: {count_even}")
print(f"Number of Odd Events: {count_odd}")

if(reverse == n):
    print(f"{n} is palindrome number.")
else:
    print(f"{n} is not palindrome number.")

if(armstrong_sum == n):
    print(f"{n} is armstrong number.")
else:
    print(f"{n} is not armstrong number.")