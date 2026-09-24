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
        curr = head
        total = 0
        while curr:
            total += 1
            curr = curr.next

        i = total - n

        print(i)

        dummy = ListNode()
        dummy.next = head

        curr = dummy

        for j in range(1, i + 1):
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next



