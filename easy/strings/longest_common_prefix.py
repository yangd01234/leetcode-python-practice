"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

Things to keep in mind:

How can you offset loops (run the outer faster than the inner)?
How can you add strings?
What sort of boundaries do you need to lookout for with minimum characters?
Why do you need to lookout for these?
How should you set the range limits on your iterations?
Why should you set these limits?
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) < 1:
            return ""
        # boundary check the shortest len of str
        boundary = min(len(s) for s in strs)
        counter = 0
        res = ""

        while counter < boundary:
            for i in range(0, len(strs)-1):
                if strs[i][counter] != strs[i+1][counter]:
                    return res
            res += strs[0][counter]
            counter += 1
        return res

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))