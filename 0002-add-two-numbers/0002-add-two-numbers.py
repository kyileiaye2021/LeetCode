# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1 = [2,3,4]
        # l2 = [4,3,1]
        # output: [6,6,5]

        # l1 = [5,6,7]
        # l2 = [5,6,7]
        # output: [0,3,5,1]

        # l1 = [0]
        # l2 = [0]
        # output: [0]

        # l1 = [9,9,9]
        # l2 = [9,9]
        # output: [8, 9, 0, 1]

        # l1 = [0]
        # l2 = [1]
        # output: [1]

        # 5 + 5 = 10 % 10 = 0
        # carry = 10// 10 = 1

        # traverse l1 and l2 together
        
        dummy = ListNode(0)
        res = dummy

        p1 = l1
        p2 = l2
        cur_sum = 0
        carry = 0

        while p1 and p2:
            cur_sum = p1.val + p2.val + carry
            carry = 0
            if cur_sum > 9:
                carry = cur_sum // 10
                cur_sum = cur_sum % 10
            
            new_node = ListNode(cur_sum)
            res.next = new_node
            res = res.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            cur_sum = p1.val + carry
            carry = 0
            if cur_sum > 0:
                carry = cur_sum // 10
                cur_sum = cur_sum % 10
            new_node = ListNode(cur_sum)
            res.next = new_node
            res = res.next
            p1 = p1.next

        while p2:
            cur_sum = p2.val + carry
            carry = 0
            if cur_sum > 0:
                carry = cur_sum // 10
                cur_sum = cur_sum % 10
            new_node = ListNode(cur_sum)
            res.next = new_node
            res = res.next
            p2 = p2.next

        if carry > 0:
            new_node = ListNode(carry)
            res.next = new_node

        return dummy.next