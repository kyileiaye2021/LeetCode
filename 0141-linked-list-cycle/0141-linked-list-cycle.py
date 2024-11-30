# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using hashset
        # st = set() # Space O(n)

        # while head: # Time O(n)
        #     if head in st:
        #         return True

        #     st.add(head)
        #     head = head.next

        # return False
       
       # Floyd cycle algorithm
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
