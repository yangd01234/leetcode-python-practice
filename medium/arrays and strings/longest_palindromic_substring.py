"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),


Things to keep in mind:
How can you use the middle expansion method here?
"""
class Solution:

    def longestPalindrome(self, s: str) -> str:

        def helper(l, r):
            '''helper function checks expanded substring'''
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                # three things happening here.  Check left within bounds, right within bounds, and still palindrome.
                l -= 1
                r += 1
            return s[l+1:r] # return the substring

        res = ""
        for i in range(len(s)):
            # check pattern aba
            test = helper(i,i)
            if len(test) > len(res):
                res = test
            # check pattern aa
            test = helper(i, i+1)
            if len(test) > len(res):
                res = test

        return res

