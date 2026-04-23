# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 2 separate linked list
        # reverse the second linked list
        # add them alternatively
        # find the middle with fast and slow pointer
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the list
        cur = slow.next
        prev = None
        while cur:
            new_node = cur.next
            cur.next = prev
            prev = cur
            cur = new_node

        # end of the first linked list
        slow.next = None

        dummy = ListNode(0)
        res = dummy

        temp = head
        while temp and prev:
            res.next = temp
            res = res.next
            temp = temp.next

            res.next = prev
            res = res.next
            prev = prev.next

        if temp:
            res.next = temp

        if prev:
            res.next = prev

        return dummy.next
