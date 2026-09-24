# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        if not head:
            return None 

        def recur(slow, fast):
            if not fast or not fast.next:
                return slow

            return recur(slow.next, fast.next.next)

        return recur(head,head)

        