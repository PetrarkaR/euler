from math import sqrt

divisors_limit = 500
triangle_sum = 0

for i in range(1, 100000):  # Incrementally calculate triangle numbers
    triangle_sum += i
    divisor_count = 0  # Reset divisor count for each triangle number

    for j in range(1, int(sqrt(triangle_sum)) + 1):
        if triangle_sum % j == 0:
            divisor_count += 2  # Count both j and (triangle_sum / j)
            if j * j == triangle_sum:  # If it's a perfect square
                divisor_count -= 1  # Avoid double-counting the square root

        if divisor_count > divisors_limit:
            print(triangle_sum)
            break

    if divisor_count > divisors_limit:
        break
