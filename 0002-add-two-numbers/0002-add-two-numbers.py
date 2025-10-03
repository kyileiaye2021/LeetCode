# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node
        # curr is dummy
        # carry over intialized to 0

        # iterate thru the list until one of the lists is exhauste
        #   create a new node
        #   add the vals from lst1 and lst2 + carry over 
        #   if the new val is greater than =  10
        #       divide the new val by 10 and assign it to carry over
        #       remainder stored in the new node
        #   
        #   curr.next = new node
        #   move curr to curr.next
        #   lst 1 and lst2 nodes
        #   
        # go over the lists that are not exhausted yet 
        #   add the carry over to the node val 
        #   if the new val is greater than =  10
        #       divide the new val by 10 and assign it to carry over
        #       remainder stored in the new node
        #   move curr to the next
        #   move the curr list by 1

        # if carry over is > 0
        #   create a new node for that and append it to the curr node

        # return dummy.next

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 and l2:
            new_node = ListNode(0)
            new_node.val = l1.val + l2.val + carry
            carry = 0
            if new_node.val >= 10:
                carry = new_node.val // 10
                new_node.val = new_node.val % 10

            curr.next = new_node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next


        while l1:
            new_node = ListNode(0)
            new_node.val = l1.val + carry
            carry = 0

            if new_node.val >= 10:
                carry = new_node.val // 10
                new_node.val = new_node.val % 10

            curr.next = new_node
            curr = curr.next
            l1 = l1.next

        while l2:
            new_node = ListNode(0)
            new_node.val = l2.val + carry
            carry = 0

            if new_node.val >= 10:
                carry = new_node.val // 10
                new_node.val = new_node.val % 10

            curr.next = new_node
            curr = curr.next
            l2= l2.next

        
        if carry > 0:
            new_node = ListNode(carry)
            curr.next = new_node
        
        return dummy.next

        





        