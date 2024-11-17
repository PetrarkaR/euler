import time

start_time = time.time()

maxInteger = 999
firstMultiplicant = 3
secondMultiplicant = 5
edgeCaseNumber = firstMultiplicant * secondMultiplicant

numberOfFirst = maxInteger // firstMultiplicant
numberofSecond = maxInteger // secondMultiplicant
numberofEdge = maxInteger // edgeCaseNumber

sumOfFirst = (((numberOfFirst * numberOfFirst + numberOfFirst)) // 2) * firstMultiplicant
sumOfSecond = (((numberofSecond * numberofSecond + numberofSecond)) // 2) * secondMultiplicant
sumOfEdge = (((numberofEdge * numberofEdge + numberofEdge)) // 2) * edgeCaseNumber

result = sumOfFirst + sumOfSecond - sumOfEdge
print(result)

end_time = time.time()

print("Time taken to execute the code:", end_time - start_time, "seconds")
