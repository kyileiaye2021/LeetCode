# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        # def recur(head, prev)
        # base case
        # if head is None
        #   return prev

        # recursive case
        #   next node = head.next
        #   head.next = prev
        #   return recur(next node, head)

        # return recur(head, None)

        def reverse(head, prev):
            # base case
            if not head:
                return prev

            # recursive case
            next_node = head.next
            head.next = prev
            return reverse(next_node, head)

        return reverse(head, None)
        