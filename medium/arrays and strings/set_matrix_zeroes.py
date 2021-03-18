"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

Things to keep in mind:
How would you keep track of what is a column vs row?
How does this position look like when assigning values to the matrix?
What should you assert?
Is it ok to go n^3?
What can you assign to indicate the row or col needs to be zeroed out?
Do you need to only indicate it at the beginning [row][0]? or is it ok to replace
all values immediatley?
"""

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])

        if len(matrix) == 0: return

        for row in range(h):
            for col in range(w):
                if matrix[row][col] == 0:
                    for i in range(h):
                        if matrix[i][col] != 0:
                            matrix[i][col] = '#'

                    for j in range(w):
                        if matrix[row][j] != 0:
                            matrix[row][j] = '#'
        # go through and set all # values to 0
        for row in range(h):
            for col in range(w):
                if matrix[row][col] == '#':
                    matrix[row][col] = 0



m1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol = Solution()
print(m1)
sol.setZeroes(m1)
print(m1)