"""

Given a linked list, swap every two adjacent nodes and return its head.

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
 

Follow up: Can you solve the problem without modifying the values in the list's
nodes? (i.e., Only nodes themselves may be changed.)

Things to keep in mind:
What is the base case?
Why is this the base case?
How would you start the recursion?
Why do you need to set new_head.next to head and head.next to recursion(new_head.next)?
How can you work on subproblems, backwards?
"""


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case stop if no head.next
        if (head is None) or (head.next is None): return head
        
        # set new head to next node
        new_head = head.next

        # set next next node to head, and nextnextnext node to swap
        new_head.next, head.next = head, self.swapPairs(new_head.next)
        return new_head
