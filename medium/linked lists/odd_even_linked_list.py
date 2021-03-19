"""
Given the head of a singly linked list, group all the nodes with odd indices 
together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain 
as it was in the input.
 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
 

Follow up: Could you solve it in O(1) space complexity and O(nodes) time complexity?

Things to keep in mind:
Should you set the end of something so it's not a cycle?
How can you keep in mind and skip a couple if you know it's odds and evens?
Why does updating evens and odds hav eto be at different next steps?
How do you account for different next steps for evens and odds?
When updating single linked list pointers, what do you need to keep in mind?
What are the two things you need to update when updating pointers?

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return None

        # keep track of odd, even, and even heads
        odd = head
        even = head.next
        even_head = even

        # iterate through even AND even.next to not miss anything
        while even and even.next:
            odd.next = even.next
            # move odd forward
            odd = odd.next
            even.next = odd.next
            # move even forward
            even = even.next

        odd.next = even_head
        return head


# helper functions to populate and print the lists
def populate_single_list(l1: ListNode, arr):
    walker = l1
    for i in range(1, len(arr)):
        temp = ListNode()
        temp.val = arr[i]
        walker.next = temp
        walker = temp

def print_list(l1: ListNode):
    temp = l1
    while temp.next:
        print(temp.val)
        temp = temp.next
    print(temp.val)

l1 = [2,1,3,5,6,4,7]

list_1 = ListNode()
list_1.val = l1[0]


populate_single_list(list_1, l1)
#print_list(list_1)
sol = Solution()
n_result = sol.oddEvenList(list_1)
print_list(list_1)