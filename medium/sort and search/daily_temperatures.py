
"""
Given a list of daily temperatures T, return a list such that, for each day in 
the input, tells you how many days you would have to wait until a warmer 
temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature
 will be an integer in the range [30, 100].

 Things to know:
 How would you initiate the array and what value should you set?
 What data structure type should you use?
 Is it ok to use two loops?
 How can you use this data structure to your advantage?
 What is the while loop condition you need to lookout for?
"""



class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # create empty array of 0's
        res = [0] * len(T)
        
        stack = []
        
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                temp = stack.pop()
                res[temp] = i - temp
            stack.append(i)
        return res
        