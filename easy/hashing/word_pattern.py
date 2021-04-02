"""
290. Word Pattern
Easy

1792

215

Add to List

Share
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter 
in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

Things to keep in mind:
What data structure?
How many should you use?
How split strings in python?
Why do you need to nest the else statements?
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # use a dict to keep track of what each key is supposed to be
        
        hashmap_pattern = {}

        hashmap_string = {}


        # split the list of strings
        string_list = s.split(' ')

        # assert same length
        if len(string_list) != len(pattern):
            return False

        for i in range(len(pattern)):
            # check if its in hashmap pattern
            if pattern[i] in hashmap_pattern:
                if hashmap_pattern[pattern[i]] != string_list[i]:
                    return False
            else:
                hashmap_pattern[pattern[i]] = string_list[i]
            # cross check if in hashmap string
            if string_list[i] in hashmap_string:
                if hashmap_string[string_list[i]] != pattern[i]:
                    return False
            else:
                hashmap_string[string_list[i]] = pattern[i]

        return True

sol = Solution()
sol.wordPattern("abc", "dog cat dog")