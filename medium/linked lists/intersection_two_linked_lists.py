"""
Given the heads of two singly linked-lists headA and headB, return the node at 
which the two lists intersect. If the two linked lists have no intersection at 
all, return null.

For example, the following two linked lists begin to intersect at node c1:


It is guaranteed that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the 
function returns.


Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, 
skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if 
the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as 
[5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 
nodes before the intersected node in B.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 
if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as 
[3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node 
before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it 
reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, 
while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB intersect.
 

Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?


Things to keep in mind:
How can you break this down into subproblems?
What measure can you use to your advantage?
How can you condense your while loop to make it keep going if not equal?
When one linked list is longer than the other, what should you do to the longer one?
Why should you start at this location instead?
How would you swap which head is longer than the other and why should you do this?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def length(L):
            length = 0
            while L:
                length += 1
                L = L.next
            return length

        l0_len, l1_len = length(headA), length(headB)

        if l0_len > l1_len:
            headA, headB = headB, headA

        for _ in range(abs(l0_len - l1_len)):
            headB = headB.next

        while headA and headB and headA is not headB:
            headA, headB = headA.next, headB.next

        return headA





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