# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        prev_l = dummy

        for _ in range(left - 1):
            prev_l = prev_l.next

        prev = None
        curr = prev_l.next
        
        for _ in range((right - left + 1)):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        tail = prev_l.next
        prev_l.next = prev
        tail.next = curr

        return dummy.next