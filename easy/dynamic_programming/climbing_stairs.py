"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45

HINT: Try the sliding window approach

Things to keep in mind:
What's the assertion?
What's the subproblem?
What can you use the array to keep track of?
Why do you need two integer variables within the loop (s and e)?
Since it's only 1 or 2 steps and not n steps, how can you simplify and keep track of the steps?
How can you build the dp table using the subproblem?
Why should you use i - 2 - 1 for s?
What is the sliding window approach?
why do we set m = 2?
Instead of running an inner loop, what do we do instead?
How are the elements of the prior window removed and the new one added with each iteration?

"""


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        m = 2

        temp = 0
        res = [1]
        for i in range(1, n+1):
            # number of stairs per iter
            s = i - m - 1
            e = i - 1

            # subtract from s as our base
            if (s >=0):
                temp -= res[s]
            temp += res[e]
            res.append(temp)

        return (res[n])


sol = Solution()
print(sol.climbStairs(3))