"""
On the first row, we write a 0. Now in every subsequent row, we look at the 
previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of 
K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].

Things to keep in mind:
Why do you need to track length?
How do you track lenght?
Why do you need to subtract from N every time
How can you make this faster without using strings or arrays?
"""

class Solution:

    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            if K == 1:
                return 0
            else:
                return 1

        l = 2 ** (N - 1)

        if K <= l:
            return self.kthGrammar(N - 1, K)
        else:
            res = self.kthGrammar(N - 1, K - l)
            return 0 if res == 1 else 1

n = 10001
n &= n - 1
print(n)    

sol = Solution()
print(sol.kthGrammar(4, 5))