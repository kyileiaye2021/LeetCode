# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right):
        l1 = left
        l2 = right
        res = ListNode(0)
        temp = res

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        if l1:
            temp.next = l1
        
        if l2:
            temp.next = l2
        return res.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        right = slow.next
        slow.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

        

        