def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))


from math import sqrt
sum=0
maxNum=2000000

for i in range(1,maxNum):
    if(is_prime(i)==True):
        sum+=i
        print(sum)