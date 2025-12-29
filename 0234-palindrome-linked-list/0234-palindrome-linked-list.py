# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # 1 -> 2 -> 1 -> 2 -> 1
        # 1 -> 2 -> 1
        # 1 -> 2
        
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None

        prev = None
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
        