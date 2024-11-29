import math

i = 1
brojPrime = 1  # Start with 2 as the first prime
currentPrime = 2  # First prime number

while brojPrime < 10001:
    i += 2  # Only test odd numbers (skip even numbers)
    is_prime = True

    # Check divisors up to sqrt(i)
    for j in range(3, int(math.sqrt(i)) + 1, 2):  # Skip even divisors
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        currentPrime = i
        brojPrime += 1

print(f"The 10001st prime is: {currentPrime}")
