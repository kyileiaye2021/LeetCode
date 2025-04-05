# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Happy case
        # input: head = [1,2,3,4,5], left = 2, right = 4
        # output: [1,4,3,2,5]

        # input: head = [1,5,7,4], left = 1, right = 3
        # output: [7,5,1,4]

        # Edge case
        # input: head = [1,4,2,-1], left = 1, right = 4
        # output: [-1,2,4,1]

        # input: head = [4], left = 1, right = 1
        # output: [4]

        # input: head = [3,5,2,9], left = 2, right = 2
        # output: [3,5,2,9]

        # Two pointer approach 
        # dummy node
        # dummy node.next = head
        # pre - to maintain the node before the left
        # moving curr and pre until curr reaches the left pointer
        # traverse the list until curr reaches the right pointer
        #   move curr and reverse the list
        # prev.next.next to curr
        # connect the pre.next to prev

        diff = right - left
        if diff < 1:
            return head

        dummy = ListNode(0, head)
        preLeft = dummy # to maintain the node before the sublist
        curr = head

        # moving both pointers until curr reaches the left node
        for _ in range(left - 1):
            curr = curr.next
            preLeft = preLeft.next

        # reverse the sub list
        prev = None
        for _ in range(diff + 1):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
 
        # connect the first node of the sublist to the curr node
        preLeft.next.next = curr

        # connect the node before the sublist to last node of sublist
        preLeft.next = prev
        
        return dummy.next
