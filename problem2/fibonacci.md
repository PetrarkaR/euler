# Fibonacci 

`
<p>Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with $1$ and $2$, the first $10$ terms will be:
$$1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$$</p>
<p>By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.</p>

`

So to solve this we can basically adhere to the property of there being a sequence that goes like -> Odd Odd Even, after the number 8 this pattern repeats up until infinity. 
We have that in the end we have an array of numbers [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]

and the solution when we add the numbers up is 4613732