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
Where should you start iteration?
Think of sliding windows, can you set expanding windows?
How would you account for edge cases like odd vs even palindromes?
"""
class Solution:

    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            left, right = i, i
            # odd length palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # we know palindrome
                if (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                # expand pointers
                left -= 1
                right += 1

            # even length palindrome
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # we know palindrome
                if (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                # epand pointers
                left -= 1
                right += 1
        return res