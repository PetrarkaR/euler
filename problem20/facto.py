from math import factorial

number=factorial(100)
sum=0
while(number>0):
    sum=sum+number%10
    number=number//10
print(sum)