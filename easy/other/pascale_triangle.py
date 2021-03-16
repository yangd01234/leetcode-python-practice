"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above 
it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

Things to keep in mind:
Should you use a temp array?
What should you assert overall?
What should you assert per row?
How can you use the sub array to your advantage?
What are some thigns to keep in mind when tracking the index position?
"""

class Solution:
    def generate(self, numRows: int):
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1,1])
            else:
                sub_array = []
                p = res[i-1]
                sub_array.append(1)
                for j in range(len(p) - 1):
                    sub_array.append(p[j] + p[j+1])
                sub_array.append(1)
                res.append(sub_array)
        return res
sol = Solution()
print(sol.generate(3))