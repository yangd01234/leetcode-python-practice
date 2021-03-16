"""
The Hamming distance between two integers is the number of positions at which 
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

How can you use exclusive or?
Review all comparisons if you don't know this answer.
How can you sum the zeroes and ones?
Ex: How would you convert the binary equivalent to a string?
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        xor = "{:b}".format(xor)
        res = 0

        for b in xor:
            res += int(b)

        return res