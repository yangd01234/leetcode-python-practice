"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without
 repetition.


Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

HINT:
Use hash or dict since we're dealing with unique values. 

One method: Use strings to keep track of unique values

Things to keep in mind:
What data structure should you use to keep track of things?
How can you loop through and use strings to your advantage?
What math operator should you use to keep track of the sub-grid (3x3) location?
How would you store these strings?
How can you then check for the three conditions using the data structure to lookup?
why do you need to keep track of if something has been visited?
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        tracker = {}
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if (curr != "."):
                    # store current cell value and locations
                    curr = board[i][j]
                    curr_row = "row-" + str(i) + str(curr)
                    curr_col = "col-" + str(j) + str(curr)
                    curr_mini =  "mini" + str(i//3) + "-" + str(j//3) + "-" + str(curr)
                    
                    # three conditions: unique in col, row, and 3x3
                    if ((curr_row in tracker)
                        or (curr_col in tracker)
                        or (curr_mini in tracker)):
                        return False
                    else:
                        tracker[curr_row] = 1
                        tracker[curr_col] = 1
                        tracker[curr_mini] = 1
        return True
                

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","7",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


board2 = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

obj = Solution()
print(obj.isValidSudoku(board))
print(obj.isValidSudoku(board2))



