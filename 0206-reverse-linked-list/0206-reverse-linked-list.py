# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Happy case
        # input - [1,2,3,4]
        # output - [4,3,2,1]
        
        # input - [1,2]
        # output - [2,1]
        
        # Edge case
        # input - []
        # output - []
        
        # input - [2]
        # output - [2]
        
        # Traversal approach
        # create a prev pointer initialized to null
        # traverse the linked list
        #   track the next node of the curr node
        #   assign the prev node pointer to the next of curr node
        #   move prev pointer to curr node
        #   move curr pointer to the next of the curr node
        # return prev pointer
        
        if not head:
            return None
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev 
        