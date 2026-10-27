try:
    l = int(input("Enter lower range: "))
    r = int(input("Enter Higher range: "))
except ValueError:
    print("Invalid Input! Only accepts Integer values!")
    exit()

if(l>r):
    raise ValueError("Lower range cannot be greater than higher range!")

if(l < 0 or r < 0):
    raise ValueError("Lower range and higher range cannot be negative!")

prime_numbers = []




for i in range(max(2, l), r+1):
    is_prime = True
    for j in range(2, int(r**0.5)+1):
        if(i%j == 0):
            is_prime = False
        else:
            is_prime = True
    if(is_prime == True):
        prime_numbers.append(i)

print(f"Prime numbers between the range of {l} and {r}: {prime_numbers}")

prime_numbers.sort
total = len(prime_numbers)
smallest = min(prime_numbers)
largest = max(prime_numbers)
sum_prime = sum(prime_numbers)


print(f"Smallest Prime number: {smallest}")
print(f"Largest Prime number: {largest}")
print(f"Total number of primes: {total}")
print(f"Sum of all prime numbers between the range: {sum_prime}")