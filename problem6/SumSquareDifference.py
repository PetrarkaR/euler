numbers=100
sumofsquares=0
squareofsum=0
for i in range(1,101,1):
    sumofsquares+=i*i
for i in range(1,101,1):
    squareofsum+=i
print(squareofsum)
squareofsum=squareofsum*squareofsum
print(squareofsum-sumofsquares)