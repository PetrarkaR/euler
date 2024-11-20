import math
import time
# Define the function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True
start_time = time.time()

magicNumber = 600851475143

# Calculate the square root
sqrt_as_integer = round(math.sqrt(magicNumber))
print(f"Square root of {magicNumber} is approximately {sqrt_as_integer}.\n")

print("Divisors and primality:")
for i in range(1, sqrt_as_integer + 1): 
    if magicNumber % i == 0:  
        is_prime_flag = is_prime(i)  
        print(f"{i} is a divisor. Prime: {is_prime_flag}")
end_time = time.time()

print("Time taken to execute the code:", end_time - start_time, "seconds")
