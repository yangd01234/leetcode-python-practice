"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

HINT: 

Things to keep in mind:
Assertion?
What is most important to keep track of?
Is there a way to complete in O(n) time?
What are the two things you should keep track of to get the max profit?
How does max difference impact getting the current max value?
Why do you need to get the difference of p - min_stock?
How does min difference impact getting the current max value?

"""

class Solution:
    def maxProfit(self, prices) -> int:
    	n = len(prices)

    	# check if there are no buys/sells
    	if n < 2:
    		return 0

    	# set placeholder for maximum profit
    	max_profit = 0
    	# set placeholder for lowest stock value
    	min_stock = prices[0]

    	for p in prices:
    		# max between current recorded max profit vs current p - min stock value
    		max_profit = max(max_profit, p - min_stock)
    		# grab the lowest stock value
    		min_stock = min(min_stock, p)
    	return max_profit

profit = Solution()

profit_1 = profit.maxProfit([7,1,5,3,6,4])
profit_2 = profit.maxProfit([7,6,4,3,1])

print(profit_1)
print(profit_2)

