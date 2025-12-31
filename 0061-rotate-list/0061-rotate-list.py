# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # create a circular linked list while keeping track of the len
        if not head:
            return head
            
        list_len = 1
        curr = head

        while curr.next:
            list_len += 1
            curr = curr.next

        curr.next = head

        # len to iterate  = list len - (k % list len) 
        len_to_iterate = list_len - (k % list_len)

        # iterate the list 
        for i in range(len_to_iterate):
            curr = curr.next

        # keep track of the next node of the last node
        res_head = curr.next

        # we have to connect the last node to null
        curr.next = None

        return res_head

        