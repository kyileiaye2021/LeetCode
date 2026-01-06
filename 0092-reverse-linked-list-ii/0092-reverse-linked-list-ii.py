# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # happy cases
        # 1, 2, 3, 4, 5, left =  2, right = 4
        # 1, 4, 3, 2, 5
        # 
        # 1, 2, 3, 4, 5, 6, 7, l = 2, r = 7
        # 1, 7, 6, 5, 4, 3, 2
        # 
        # 1, 2, 3, 4, 5, left =  1, right = 4
        # 4, 3, 2, 1, 5

        # edge cases
        # 1, l = 1, r= 1
        # 1

        # 1, 2, l = 1, r = 2
        # 2, 1

        # dummy node
        # add the head to the dummy.next

        # prev left = dummy
        # curr = head
        # traverse the list 
        #   stop when the curr reaches the left pointer
        # mark the prev left and future right node
        # prev = None
        # reverse the nodes until the curr is right node
        # traverse one time to make prev at the right node
        # connect the prev to the prev left .next
        # connect the future right node.next to the curr
        # return dummy.next

        if not head.next:
            return head

        diff = right - left

        if diff < 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev_l = dummy
        curr = head

        # get to the left node
        for _ in range(left - 1):
            prev_l = curr
            curr = curr.next

        future_r = curr

        # reverse the list upto right node
        prev = None
        for _ in range(diff + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # connecting the new left to the list
        prev_l.next = prev

        # connecting the new right to the list
        future_r.next = curr

        return dummy.next



            




