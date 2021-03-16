"""
The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
 which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of 
groups so that each group is a contiguous section all of the same character. 
Then for each group, say the number of characters, then say the character. To 
convert the saying into a digit string, replace the counts with a number and 
concatenate every saying.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.

 

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

Constraints:

1 <= n <= 30

Things to keep in mind:
How does this problem use the last sequence?
How does the last question correlate to 1,2,3,4?
What are the assertions?
What can you assign the starting res variable to make your life easier?
How can you use a helper function?
What do you need to keep in mind when counting the sequence?
Why should you use an index -2?
"""

class Solution:

    def helperConvert(self, s):
        res = ""
        occurance = 1

        if len(s) == 1:
            return s

        # go through each and find the occurance per sequence
        for i in range(0, len(s)-1):
            # if occurs in next sequence, add
            if s[i] == s[i+1]:
                occurance += 1
            else: # otherwise, append and reset occurance
                res += (str(occurance) + s[i])
                occurance = 1

        res += (str(occurance) + s[len(s)-1])
        return res

    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        # the sequence is based off of the n-1 term
        res = "11"

        for i in range(0, n-2):
            res = self.helperConvert(res)

        return res

            

sol = Solution()
print(sol.countAndSay(7))

