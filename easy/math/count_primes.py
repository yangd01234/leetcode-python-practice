"""
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

Things to keep in mind:
What is the sieve of eratosthenes?
"""
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0

        a = [True] * n

        a[0], a[1] = False, False
        res = 0

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            for j in range (i*i, n, i):
                a[j] = False

        for i in range(0, len(a)):
            if a[i]:
                res += 1
        return res

sol = Solution()
print(sol.countPrimes(10))