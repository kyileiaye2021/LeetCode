# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # travere two lists with 2 pointers
        #   add the nodes and carry and divide by 10 
        #   create a new node with remainder and add it to dummy
        #   add the dividend to the carry
        
        carry = 0
        dummy = ListNode(0)
        temp = dummy

        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            carry = curr_sum // 10
            curr_node = curr_sum % 10
            new_node = ListNode(curr_node)
            temp.next = new_node
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curr_sum = l1.val + carry
            carry = curr_sum // 10
            curr_node = curr_sum % 10
            new_node = ListNode(curr_node)
            temp.next = new_node
            temp = temp.next
            l1 = l1.next

        while l2:
            curr_sum = l2.val + carry
            carry = curr_sum // 10
            curr_node = curr_sum % 10
            new_node = ListNode(curr_node)
            temp.next = new_node
            temp = temp.next
            l2 = l2.next

        if carry > 0:
            new_node = ListNode(carry)
            temp.next = new_node
            temp = temp.next
            
        return dummy.next