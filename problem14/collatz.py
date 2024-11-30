i=13
maxChain=0
collatz=0
for i in range(999999,0,-1):
    iteration=1
    temp=i
    print(i)
    while(i!=1):
        if (i%2==0):
            i=i/2
            iteration += 1
        else:
            i=3*i+1
            iteration += 1
    if(maxChain<iteration):
        maxChain=iteration
        collatz=temp
    

print(collatz)
