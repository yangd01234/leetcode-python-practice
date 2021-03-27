"""
Given the head of a singly linked list, reverse the list, and return the 
reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?

Things to keep in mind:
If it is a singly lined list what's the only thing you need to reverse?
Don't think of the values in order, but think of the attributes of the class.


Hint:
Look at the pointers, reverse only the pointers.


Things to keep in mind:
What is a simple solution to this? This about the only thing you need to update.
Now with this simple solution, what are the things you need to keep track of?
What do you need to assert?
What can you use as temporary placeholders (so you don't allocate more variables than needed)?
Why do you need to set current.next to head, and then point head to current?
That seems like a cycle? But why is that advantagous?

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        new_tail = head
        
        while new_tail.next:
            current = new_tail.next
            new_tail.next = current.next

            # at the end of this switch, you essentially set the new head          
            current.next = head
            head = current
        
        return head