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

Things to keep in mind:
What data structure should you use?
How can you use strings to your advantage?
"""

class Solution:
    def groupAnagrams(self, strs):
        # create a dict to keep everything
        keys = {}
        res = []

        # iterate through and sort the strings
        for s in strs:
            sorted_str = "".join(sorted(s))

            if sorted_str in keys:
                keys[sorted_str].append(s)
            else:
                keys[sorted_str] = [s]

        # for each key, loop through and append to res
        for key in keys:
            res.append(keys[key])

        return res