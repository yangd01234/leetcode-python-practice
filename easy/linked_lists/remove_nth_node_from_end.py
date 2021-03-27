"""
Given the head of a linked list, remove the nth node from the end of the list 
and return its head.

Follow up: Could you do this in one pass?

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Things to keep in mind:
What are you given?
How can you assign all to head and why should you?
What should you assert?
How can you use runners and walkers?
What do you need to assert as well when lookinig at linked list heads? Base cases?
Instead of checking for future items like in arrays, what does the runner do here?
How can you assign walker to delete?
Why should you return head?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # assign runner and walker to head
        runner = walker = head

        # find the runner location
        for _ in range(n):
            runner = runner.next

        # assert if runner is head
        if runner == None:
            return head.next

        # runner becomes the bumpstop for walker.  Once walker reaches n, delete
        while runner.next:
            runner = runner.next
            walker = walker.next
        walker.next = walker.next.next

        return head

