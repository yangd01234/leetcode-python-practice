"""
Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most significant digit is at the head of the
 list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.

 

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

HINT: You can use datatype manipulation to get around **

Things to keep in mind:
What can you convert the digits to?
How can you then iterate throught his and find the answer?
Do you need to convert it back to an int?

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = ""
        # create a str and convert it back to int
        for i in digits:
            temp += str(i)

        temp = int(temp)
        temp += 1

        a = []

        for c in str(temp) :
            a.append(int(c))

        return a


digits1 = [1,2,3]
digits2 = [4,3,2,1]
digits3 = [0]

obj = Solution()
print(obj.plusOne(digits1))