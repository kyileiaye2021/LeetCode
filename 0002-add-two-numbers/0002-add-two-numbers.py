# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        # happy cases
        # 2, 4, 3
        # 5, 6, 4
        # 7, 0  8

        # edge cases
        # 0
        # 0
        # 0

        # 9, 9
        # 9
        # 8 0 1

        # recur(l1, l2, carry)
        # base case
        # if not l1 and not l2 
        #   return None

        # recursive case
        # l1 val = 0, l2 val = 0
        # if l1:
        #   l1 val = l1.val
        # if l2:
        #   l2 val = l2.val
        # new val = l1 val + l2 val + carry
        # carry = new val % 10
        # create a new node with new val
        # if not l2:
        #   new val.next = recur(l1.next, None, carry)
        # if not l1:
        #   new val.next = recur(None, l2.next, carry)
        # return new val

        # return recur(l1, l2, 0)

        def recur(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None

            l1_val = 0
            l2_val = 0

            if l1:
                l1_val = l1.val

            if l2:
                l2_val = l2.val

            new_val = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10

            new_node = ListNode(new_val)
            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None

            new_node.next = recur(l1_next, l2_next, carry)
            return new_node

        return recur(l1, l2, 0)


