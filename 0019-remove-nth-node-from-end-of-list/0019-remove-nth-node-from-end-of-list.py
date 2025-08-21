# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # go thru every single node and get the len of the list
        # go thru for len - k - 1 times
        # curr = curr.next

        # 2 pointers
        # x, y 
        # move x by k times ahead
        # move x and y until we reach y to the end
        
        
        x, y = head, head
        for i in range (n):
            y = y.next

        if not y: # if there is only one ele in the list or if y reaches None
            head = head.next
            return head

        while y.next:
            x = x.next
            y = y.next
        
        x.next = x.next.next
        return head
