# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Happy cases
        # input: head = [1,2,3], n = 1
        # output: [1,2]

        # input: head = [1,-1,5,9], n = 2
        # output: [1,-1,9]

        # input: head = [2,3], n = 1
        # output: [2]

        # edge cases
        # input: head = [2], n = 1
        # output: []

        # Brute Force - Array: O(n) time and O(n) space
        # Two pointers 
        # check if there is only one node
        #   return empty list
        # x, y pointer both pointing to the head first
        # move y pointer ahead n times
        # if y pointer points to the last node
        #   connect x.next to None
        # traverse the list until y pointer reaches the second to last node in the list
        #   move x, y at a time
        # remove x.next node and connect x node to x.next.next
        # temp = x.next
        # x.next = x.next.next
        # return head

        # for the empty list
        if not head or not head.next:
            return None

        x, y = head, head
        for i in range(n):
            y = y.next

        # for the list with 2 nodes
        if not y:
            head = head.next
            return head

        # if not y.next:
        #     x.next = None
        #     return head

        while y.next:
            x = x.next
            y = y.next

        # remove the node at nth position from the end
        x.next = x.next.next

        return head



        