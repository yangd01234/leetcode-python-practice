"""
Given a string, find the first non-repeating character in it and return its
index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.
Things to keep in mind:
What data structure can you use for easy lookup?
What can you increment?
If you want to complete in O(n) time, is it ok to use multiple for loops?

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracker_dict = {}
        for i in s:
            if i not in tracker_dict:
                tracker_dict[i] = 1
            else:
                tracker_dict[i] += 1

        for i in range(len(s)):
            if tracker_dict[s[i]] == 1:
                return i
        return -1

first_unique = "loveleetcode"
sol = Solution()
print(sol.firstUniqChar(first_unique))