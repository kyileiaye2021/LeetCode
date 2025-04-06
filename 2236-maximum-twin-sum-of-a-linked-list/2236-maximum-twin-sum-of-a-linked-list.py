# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # happy cases
        # input: head = [1,2,4,7]
        # output: 8

        # input: head = [-1,4,0,-4]
        # output: 4

        # edge cases
        # input: head = [2,3]
        # output 5

        # Brute force
        # Two pointer
    
        # fast , slow to find middle node
        # prev = None
        # curr = slow.next
        # traverse the list until curr becomes none
        #   tempNext = curr.next
        #   set curr.next = prev
        #   set prev = curr

        # max_sum = 0
        # curr = head
        # traverse the list until prev becomes none
        #   curr_sum = curr.data + prev.data
        #   max_sum = max(curr_sum, max_sum)
        # return max_sum

        # if there are only 2 nodes
        if not head.next.next:
            return head.val + head.next.val

        # find middle node 
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        curr = slow
        prev = None
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        max_sum = 0
        while prev:
            curr_sum = prev.val + head.val
            max_sum = max(max_sum, curr_sum)
            prev = prev.next
            head = head.next

        return max_sum
        