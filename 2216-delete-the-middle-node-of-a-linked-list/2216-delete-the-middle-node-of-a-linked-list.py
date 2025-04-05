# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Happy cases
        # input: [1,2,3]
        # output: [1,3]

        # input: [1,2,6,5]
        # output: [1,2,5]

        # Edge cases
        # input: [1]
        # output: []

        # input: [3,-1]
        # output: [3]

        # Two Pass - first find of the len of the list and find the middle by doing len/2
        #          - in the second pass, go thru list until the middle position and remove the middle node

        # Slow/fast pointer 
        # set curr to head
        # prev node = None
        # go thru the list with f/s pointers until curr becomes none or curr.next becomes none
        #   update prev to s
        #   move s by 1 node
        #   move f by 2 nodes 
        # remove the s pointer node -> set prev.next to s.neext
        # return head

        if not head or not head.next:
            return None

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head