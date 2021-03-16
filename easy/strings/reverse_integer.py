"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers 
(signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1

Things to keep in mind:
What can you do to convert the integer first?
What built in functions in python can you use?
When asserting signed 32 bit integer, how can you  make it simple?
Why do you start at moving 31 instead of 32?
Why should you assert at the end instead of the beginning for signed 32 int?
"""

class Solution:
    def reverse(self, x: int) -> int:

        r_str_int = str(abs(x))
        r_str_int = ''.join(reversed(r_str_int))
        r_str_int = int(r_str_int)

        # check if signed 32 bit integer.  Since it's signed, we reserve 1 bit hence 31
        if (abs(r_str_int) > (1 << 31)):
            return 0
        elif x < 0:
            return r_str_int * -1
        else:
            return r_str_int

reveresed_integer = Solution()

x = 1534236469
print(reveresed_integer.reverse(x))
print(x)