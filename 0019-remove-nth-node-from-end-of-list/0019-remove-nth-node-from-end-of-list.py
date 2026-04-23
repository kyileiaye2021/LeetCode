# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # head = 1,2,3,4,5, n = 2
        # output: [1,2,3,5]

        # head = [1,2,3], n = 3
        # output: [2,3]

        # head = [1,2,3], n = 1
        # output: [1,2]

        # head = [1],  n = 1
        # output: []

        # fast and slower pointer
        # 1, 2, 3, 4, n = 2
        # 
        # dummy node
        # d -> 1 -> 2 -> 3

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next





        
