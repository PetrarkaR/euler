maxNum=999*999
minNum=500*500
for i in range(minNum,maxNum,1):
    str_number = str(i)
    if(str_number == str_number[::-1]):
        for num1 in range(999, 99, -1):
        # Check if num1 divides the palindrome evenly
            if i % num1 == 0:
                num2 = i // num1  # Calculate the second factor
                if(num2<1000):
                    print(num1,num2)