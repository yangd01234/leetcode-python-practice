"""
205. Isomorphic Strings
Easy

1942

461

Add to List

Share
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same 
character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

Things to keep in mind:
Why do you not need to keep track of number of values? 
Why should you only keep track of the occurance once for each letter (as you go)?
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # make a dict with the count
        d = {}

        for i in range (len(s)):
            if s[i] in d.keys():
                if d[s[i]] != t[i]:
                    return False

            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
        return True