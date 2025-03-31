# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # happy cases
        # input: head = [1,2,3,4]
        # output: [4,3,2,1]

        # input: head = [6,-1,3]
        # output: [3,-1,6]

        # edge cases:
        # input: head = [3]
        # output: [3]

        # input: head = []
        # output: []

        # Brute force - O(n) space using two arrays
        # use an array to store the data of every node by traversing the linked list
        # create an another array to store the elements in reverse order

        # Bruter force - using one array and two pointers - O(n) space
        # use an array to store the data of every node by traversing the linked list
        # create two pointers at the edges of the array and swap the two pointer elements and shrink the size between two pointers

        # Two pointer
        # create a prev pointer to None
        # initialize the curr pointer to head
        # traverse the list until curr pointer reaches None
        #   next node = curr.next
        #   curr.next = prev
        #   prev = curr
        #   curr = next node
        # return prev

        if not head:
            return None
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev