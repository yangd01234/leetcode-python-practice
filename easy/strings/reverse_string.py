"""
Write a function that reverses a string. The input string is given
as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Things to keep in mind:
What can you do to get half of the array?
instead of using a tracker variable, how can you use the i to keep position?
"""

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

string_1 = ["h","e","l","l","o"]
string_2 = ["H","a","n","n","a","h"]
reveresed = Solution()
reveresed.reverseString(string_1)
reveresed.reverseString(string_2)
print(string_1)
print(string_2)