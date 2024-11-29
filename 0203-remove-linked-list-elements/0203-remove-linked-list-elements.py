# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # check if the head val is equal to the val
        #   head = the next of the head
        # iterate over the nodes in the list
        #   check if the next node value is equal to val
        #       if the next node is last node      
        #           connect the curr node with next node's next
        #           change the curr node to next node

        dummy = ListNode()
        dummy.next = head
        h = dummy

        while head:
            next_node = head.next
            if head.val == val:
                dummy.next = next_node
            else:
                dummy = dummy.next
            head = next_node

        return h.next



        