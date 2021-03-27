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
What do you need to check both runner and runner.next?

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
        
        # find the halfway point.  You won't need the runner after this. 
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            
        # reverse the second half of list
        prev = None
        while walker:
            # keep walker.next in temp (node)
            temp = walker.next
            # set walker.next to our previous value (pointer)
            walker.next = prev
            # set prev to walker (node)
            prev = walker
            #re-assign walker to temp essentially move walker forward by 1 (node)
            walker = temp
            
        # check if palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True



