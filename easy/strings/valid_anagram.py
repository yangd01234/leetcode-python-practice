"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your
solution to such case?

Things to keep in mind:
What is the first assertion?
How can you use sorting to your advantage?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if unequal length
        if len(s) != len(t):
            return False

        temp_s = sorted(s)
        temp_t = sorted(t)

        for i in range(0, len(s)):
            if temp_s[i] != temp_t[i]:
                return False
        return True


s_1 = "anagram"
t_1 = "nagaram"
s_2 = "rat"
t_2 = "car"

sol = Solution()
print(sol.isAnagram(s_1, t_1))
print(sol.isAnagram(s_2, t_2))
