"""
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

Things to keep in mind:
How would you sort by the first value and why?
Why do you need to add the first interval value?

How would you check the last interval position?
Why do you need only the max of the last interval and current?
What should you append if you don't find this?
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by intervals by the start interval
        intervals.sort(key = lambda i : i[0])

        # add the first interval
        res = [intervals[0]]

        # start at pos 1 since we added the first interval (smallest)
        for start, end in intervals[1:]:
            # last ending interval - check for overlap
            last_end = res[-1][1]

            if start <= last_end:
                # get the biggest of the last interval
                res[-1][1] = max(last_end, end)
            else: # it doesn't overlap, we need to add it to our res
                res.append([start, end])
        return res
