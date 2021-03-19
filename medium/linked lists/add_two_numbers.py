"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number
0 itself.


Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

# create a new linked list to return
# design helper function to add and carry over
# iterate through both linked lists and add

Things to keep in mind:
How can you use a helper function?
When iterating through a linked list, what should you keep in mind?
How can you track when you iterate through TWO linked lists simultaniously?
What is the last thing you need to cleanup when iterating through two linked lists?
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_helper(self, n1, n2):
        """ helper function: 0 <= Node.val <= 9 """
        if (n1 + n2) >= 10:
            return 1, (n1 + n2 - 10)
        else:
            return 0, (n1 + n2)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # create a res node head
        res = ListNode()
        res_head = res
        # set index
        walker_l1 = l1
        walker_l2 = l2
        carry_over = 0
        # iterate through both lists
        while walker_l1 != None or walker_l2 != None:

            sum1 = walker_l1.val if walker_l1 != None else 0
            sum2 = walker_l2.val if walker_l2 != None else 0
            # if exists, set to current linked node val

            if walker_l1:
                walker_l1 = walker_l1.next
            else:
                walker_l1 = None

            if walker_l2:
                walker_l2 = walker_l2.next
            else:
                walker_l2 = None

            carry_over, res.val = self.add_helper(sum1 + carry_over, sum2)

            if not walker_l2 and not walker_l1:
                break
            res.next = ListNode()
            res = res.next

        if carry_over != 0:
            res.next = ListNode()
            res = res.next
            res.val += carry_over
        else:
            res = None
        return res_head


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


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

list_1 = ListNode()
list_1.val = l1[0]

list_2 = ListNode()
list_2.val = l2[0]

populate_single_list(list_1, l1)
populate_single_list(list_2, l2)

sol = Solution()
n_result = sol.addTwoNumbers(list_1, list_2)
print_list(n_result)


l1 = [2,4,3]
l2 = [5,6,4]

list_1 = ListNode()
list_1.val = l1[0]

list_2 = ListNode()
list_2.val = l2[0]

populate_single_list(list_1, l1)
populate_single_list(list_2, l2)

sol = Solution()
n_result = sol.addTwoNumbers(list_1, list_2)
print_list(n_result)
