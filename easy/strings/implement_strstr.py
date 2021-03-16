"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle 
is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question 
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
 This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.

Things to know:
How can you use a runner pointer to keep track of validation?
What needs to be asserted first?
When looping through, what do you need to aware of in term of index boundaries?
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        needle_len = len(needle)
        haystack_len  = len(haystack)
        if needle_len > haystack_len:
            return -1
        # if needle is empty, return 0
        if needle_len == 0:
            return 0

        # need these two so we can have runner pointers
        needle_i = 0
        for i in range(0, haystack_len - needle_len + 1):
            # find the first letter match
            if haystack[i] == needle[0]:
                # iterate through and see if the rest match
                    for j in range(0, needle_len):
                        if needle[j] == haystack[i + j]:
                            needle_i += 1
                    if needle_i == needle_len:
                        return i
                    else: needle_i = 0
        # needle not in haystack
        return -1

sol = Solution()
print(sol.strStr("hello", "ll"))
print(sol.strStr("aaaaaaaaaaa", "bba"))
print(sol.strStr("", ""))
print(sol.strStr("", "a"))
print(sol.strStr("mississippi", "issipi"))
print(sol.strStr("a", "a"))