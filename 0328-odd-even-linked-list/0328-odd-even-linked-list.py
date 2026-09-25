# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        # dum odd = ListNode()
        # curr odd
        # dum even = ListNode()
        # curr even

        # recur(curr, n)
        # non local curr odd
        # non local cur even
        # base cases
        #   if curr is none
        #       return
        #   if n % 2 == 0:
        #       curr even.next = curr
        #       curr even = curr even.next
        #   else:
        #       curr odd.next = curr
        #       curr odd = curr odd.next
        #   recur(curr.next, n + 1)
        # 
        # recur(curr, 1)

        # curr = dum odd
        # while curr.next:
        #   curr = curr.next
        # curr.next = dum even.next
        # return dum odd.next

        dum_odd = ListNode()
        dum_even = ListNode()
        curr_odd = dum_odd
        curr_even = dum_even

        def recur_even_odd(curr, n):
            nonlocal curr_odd
            nonlocal curr_even

            # base case
            if not curr:
                return None

            # recursive step
            if n % 2 == 0:
                curr_even.next = curr
                curr_even = curr_even.next

            else:
                curr_odd.next = curr
                curr_odd = curr_odd.next

            recur_even_odd(curr.next, n + 1)


        # n = 1
        # dum_odd = ListNode()
        # dum_even = ListNode()
        # curr_odd = dum_odd
        # curr_even = dum_even
        # curr = head

        # while curr:
        #     if n % 2 == 0:
        #         curr_even.next = curr
        #         curr_even = curr_even.next
        #     else:
        #         curr_odd.next = curr
        #         curr_odd = curr_odd.next

        #     curr = curr.next
        #     n += 1

        recur_even_odd(head, 1)
        curr_even.next = None
        curr_odd.next = dum_even.next 
        return dum_odd.next
                