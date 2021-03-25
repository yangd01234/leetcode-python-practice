"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

Things to keep in mind:
What happens when you reach the base case?
How should you design the base case around this?
How can you make this so it's bottom up approach?
What is the subproblem?
What are some things to keep in mind as you're building the row?
How is it that only the single row is returned and now the entire triangle?
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]

        # recurse and remove -1 row index
        pre = self.getRow(rowIndex-1)
        
        # start subproblem of constructing a new row
        new = [1] # start and end of rows always have 1
        # subproblem
        for i in range(0, len(pre) - 1):
            new.append(pre[i] + pre[i+1])
        new.append(1)

        # new returned value is only used once base case is reached
        return new