# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        res = dummy
        total = 0

        while l1 or l2 or carry:
            total = carry 

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            new_val = total % 10
            carry = total // 10

            new_node = ListNode(new_val)
            dummy.next = new_node
            dummy = dummy.next
        
        return res.next


