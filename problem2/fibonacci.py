fibonacci = [1,2]
fibonacciNew= []
sum=0
for i in range (40):
    
    temp=fibonacci[i]+fibonacci[i+1]
    fibonacci.append(temp)
    if(temp>4000000):
        break
    if(fibonacci[i+2] % 2 ==0):
        print(fibonacci[i+2])

print(fibonacci)
length=len(fibonacci);
for i in range (length):
    if(fibonacci[i]%2==0):
        sum=sum+fibonacci[i]
print(sum);