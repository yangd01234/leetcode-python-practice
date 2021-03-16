"""
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

Things to keep in mind:
How can you traverse and get half of the singly linked list with while?
How can you reverse the second half?
What questions should you ask about manipulation of the linked list?
How can you finally check if it is a palindrome?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # find the length of the node

        runner = head
        walker = head

        # reach the middle
        while runner and runner.next:
            # you set two next for runner to get half
            runner = runner.next.next
            walker = walker.next

        # reverse second half
        previous = None

        while walker:
            temp = walker.next
            walker.next = previous
            previous = walker
            walker = temp

        # check if palindrome
        left, right = head, previous
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True



