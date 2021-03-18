"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Things to keep in mind:
What should you assert?
What type of data set can you use for fast lookup?
How can you apply the sliding window approach to this?
How can you get the result and how should you add this up?
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        # use a set for fast lookup
        char_set = set()
        left = 0
        res = 0

        # with the sliding window approach, you can go from left to right
        for right in range((len(s))):

            # if s[right] in char_set, remove it and increment left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # add s[right] to the set
            char_set.add(s[right])
            # the result of the loop is the current max or, window + 1
            res = max(res, right - left + 1)
        return res

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring(""))

