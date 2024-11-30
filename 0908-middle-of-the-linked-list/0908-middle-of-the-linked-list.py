# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # happy cases
        # input: head = [1,2,3,4,5]
        # output: [3,4,5]

        # input: head = [1,2,3,4,5,6]
        # output: [4,5,6]

        # edge cases
        # input: head = [1]
        # output: [1]

        # input: head = [1,2]
        # output: [2]

        # slow and fast pointer
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow