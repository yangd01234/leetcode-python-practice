"""
Given an array of strings strs, group the anagrams together. You can return the 
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

Things to keep in mind:
What data type can you use?
How can you figure out duplicates?
How can you sort and join a string?
"""
class Solution:

    def groupAnagrams(self, strs):

        idx = 0
        res = []

        keys = {}
        # use a dict and keep all the lists.  Sort everything first
        
        for i in range(0, len(strs)):
            # if key exists, append.  Else create
            sorted_string = "".join(sorted(strs[i]))
            if sorted_string in keys:
                keys[sorted_string].append(strs[i])
            else:
                keys[sorted_string] = [strs[i]]

        for key in keys:
            res.append(keys[key])

        return res

sol = Solution()


strs_1 = ["eat","tea","tan","ate","nat","bat"]

strs_2 = [""]

strs_3 = ["a"]

sol = Solution()
print(sol.groupAnagrams(strs_1))
print(sol.groupAnagrams(strs_2))
print(sol.groupAnagrams(strs_3))