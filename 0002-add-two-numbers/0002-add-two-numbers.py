# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # 2, 4, 3
        # 5, 6, 4
        # 7, 0, 8

        # 9, 9, 9
        # 9, 9, 9, 9
        # 8, 9, 9, 0, 1

        # 1
        # 0, 1
        # 1, 1

        i = l1
        j = l2
        carry = 0
        dummy = ListNode()
        curr = dummy

        while i and j:
            new_node_val = (i.val + j.val + carry) % 10
            carry = (i.val + j.val + carry) // 10
            new_node = ListNode(new_node_val)
            curr.next = new_node
            curr = curr.next
            i = i.next
            j = j.next

        while i:
            new_node_val = (i.val + carry) % 10
            carry = (i.val + carry) // 10
            new_node = ListNode(new_node_val)
            curr.next = new_node
            curr = curr.next
            i = i.next

        while j:
            new_node_val = (j.val + carry) % 10
            carry = (j.val + carry) // 10
            new_node = ListNode(new_node_val)
            curr.next = new_node
            curr = curr.next
            j = j.next

        if carry > 0:
            new_node = ListNode(carry)
            curr.next = new_node


        return dummy.next


