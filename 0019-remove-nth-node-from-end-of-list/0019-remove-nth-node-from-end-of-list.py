# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        # head = [1,2,3,4,5], n = 2
        # [1,2,3,5]

        # head = [1], n = 1
        # []

        # head = [1,2], n = 1
        # [1]

        # head = [1,2,3], n = 3
        # [2,3]
    
        dummy = ListNode()
        dummy.next = head

        s = f = dummy

        for i in range(n):
            f = f.next

        while f.next:
            s = s.next
            f = f.next
        
        s.next = s.next.next

        return dummy.next


        

