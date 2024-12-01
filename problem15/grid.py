def binomial_coefficient(n, k):
    numerator = 1
    denominator = 1
    
    # Calculate n! / (n-k)!
    for i in range(k):
        numerator *= n - i
        denominator *= i + 1

    return numerator // denominator

# Calculate 40 choose 20
result = binomial_coefficient(40, 20)
print(result)