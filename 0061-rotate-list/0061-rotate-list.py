# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # happy cases
        # head = [1,2,3,4,5], k = 2
        # output: [4,5,1,2,3]

        # head = [0,1,2], k = 4
        # Output: [2,0,1]

        # edge cases
        # head = [], k = 3
        # output: []

        # head = [5], k = 4
        # output: [5]

        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head

        # find the len of the list
        cur = head
        length = 0
        while cur:
            length +=1
            cur = cur.next

        # get the modified k
        k = k % length
        if k == 0: # no rotation needed
            return dummy.next

        # slow fast pointer
        # for k times, we move fast pointer first 
        # after that, move slow and fast the same time
        # new head = slow.next
        # slow.next = None
        # fast.next = dummy.next

        slow = fast = dummy
        for i in range(k):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = dummy.next

        return new_head
