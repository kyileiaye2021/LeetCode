# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # traverse the nodes in linked list and get the middle node
        # reverse the second part of the linked list
        # iterate over elements in each part
        #   compare if the values of the curr nodes are not the same
        #       return False
        # return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True


        

        
