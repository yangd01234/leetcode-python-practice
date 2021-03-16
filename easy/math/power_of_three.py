"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
Example 4:

Input: n = 45
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

Things to keep in mind:
Brute force is just to loop through and find if i ** 3 == n.  How can we make
this faster?
What can you use to your advantage if you know the max int?
With powers, how can you manipulate it so that it works all the time?
Ex: is 3 x 3 x 3 within 3 x 3 x 3 x 3 x 3?
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (n > 0) and (1162261467 % n == 0)