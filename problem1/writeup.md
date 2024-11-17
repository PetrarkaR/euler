# Problem 1

<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>

To solve this problem, I first count how many times a number divisible by 3 or 5 appears below the limit. Then, I calculate the total sum of these numbers by multiplying each divisor (3 or 5) by the sum of all the numbers it divides evenly into.

However, there’s an overlap where some numbers are counted twice—specifically, numbers that are divisible by both 3 and 5, like 15 and its multiples. To account for this, I calculate the sum of numbers divisible by 15 separately and subtract it from the total sum. This ensures each number is counted exactly once.