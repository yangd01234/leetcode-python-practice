"""
Say you have an array prices for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock multiple
 times).

Note: You may not engage in multiple transactions at the same time (i.e., you
must sell the stock before you buy again).

HINT: Runner pointer
"""



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # find the total profit
        profit_total = 0

        # loop through list O(1) with +1 runner pointer
        for i in range(1,len(prices)):
        	difference = prices[i] - prices[i-1]
        	# check if next day has profit
        	if (difference) > 0:
        		profit_total += difference

        return profit_total
        

# ex_1 = 7; ex_2 = 4; ex_3 = 0
ex_1 = [7,1,5,3,6,4]
ex_2 = [1,2,3,4,5]
ex_3 = [7,6,4,3,1]

profit_1 = Solution()
print(profit_1.maxProfit(ex_3))