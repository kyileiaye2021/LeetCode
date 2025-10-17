# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, head):
        if not head or not head.next:
            return head
        revHead = self.helper(head.next)
        head.next.next = head
        head.next = None
        return revHead

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)
        