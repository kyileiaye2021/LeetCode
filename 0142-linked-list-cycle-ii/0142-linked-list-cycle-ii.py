# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # happy case
        # input: head = [3,2,0,-4]
        # output: 1

        # input: head = [3,2,1]
        # output: 0

        # edge case
        # input: head = []
        # output: -1

        # input: head = [1]
        # output: -1

        # input: head = [3]
        # output: 0

        # fast, slow pointer approach
        # need to keep track of the slow_index
        # fast, slow to the head of list
        # traverse the list until the fast pointer reaches null or the fast pointer next node reaches null
        #   move fast 2 steps at a time
        #   move slow 1 step at a time
        #   update slow_index by 1
        #   check if fast pointer meets the slow 
        #       return slow pointer index
        # return -1

        # fast and slow can meet at any point in the cycle. How can we find the beginning of the cycle?

        fast, slow = head, head
        
        while fast and fast.next:

            slow = slow.next 
            fast = fast.next.next

            if fast == slow:
                fast = head

                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return fast

        return None
