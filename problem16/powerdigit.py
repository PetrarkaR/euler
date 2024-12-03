
number = (pow(2,1000))
sum=0;
while(number>0):
    sum=sum+number%10;
    number=number//10
print(sum)
