# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        n = 1
        dum_odd = ListNode()
        dum_even = ListNode()
        curr_odd = dum_odd
        curr_even = dum_even
        curr = head

        while curr:
            if n % 2 == 0:
                curr_even.next = curr
                curr_even = curr_even.next
            else:
                curr_odd.next = curr
                curr_odd = curr_odd.next

            curr = curr.next
            n += 1
        curr_even.next = None
        curr_odd.next = dum_even.next 
        return dum_odd.next
                