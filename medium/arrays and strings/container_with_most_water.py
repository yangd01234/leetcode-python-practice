"""
11. Container With Most Water
Medium

8936

689

Add to List

Share
Given n non-negative integers a1, a2, ..., an , where each represents a point at 
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the 
line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis 
forms a container, such that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

Things to keep in mind:
What method should you use?
Why do you only need to keep track of l and r heights?
What do you need for the max area?

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # use a two pointer approach
        l, r = 0, len(height) -1

        # keep the area.  We need to keep track of l/r and height (w * h)
        area = 0

        # loop while left pointer is greater than right pointer
        while (l < r):
            # area = max of current area or w*height
            area = max(area, (r-l)*(min(height[l], height[r])))

            # if your height is smaller than right, advance
            if height[l] < height[r]:
                l += 1
            else: # otherwise, advance right
                r -= 1
        return area

