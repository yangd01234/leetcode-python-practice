"""
Merge two sorted linked lists and return it as a sorted list. The list should be
 made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

Why do you need to keep track of the head?
What does temp keep track of?
How can you iterate through and compare the two?
When iterating through the list, what are the things you need to keep track?
What leftovers do you need to keep track of?
What should you return?
Is it ok to create a new ListNode object?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = temp = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        
        # assign the new tails
        if l1: temp.next = l1
        if l2: temp.next = l2
        
        # return next because res has no value
        return res.next
        