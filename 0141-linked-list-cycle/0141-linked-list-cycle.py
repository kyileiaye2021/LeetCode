# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # happy case
        # input: head = [3,2,0,-4], pos = 1
        # output: true

        # input: head = [2,3], pos = 0
        # output: True

        # edge case

        # input: head = [], pos = 0
        # output: False

        # input: head = [1], pos = 0
        # output: True
         
        # input: head = [2], pos = -1
        # output: False

        # input: head = [2,4,3], post = 4
        # output: False

        # brute force - array: cannot work because we don't know when to break
        # fast slow pointer approach 
        # fast, slow both pointing to head
        # traverse the list from the head until the fast pointer reaches none
        #   move the slow pointer by 1 node
        #   move the fast pointer by 2 nodes
        #   check if the fast and slow pointer meets at some point:
        #       return true
        # return false

        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

