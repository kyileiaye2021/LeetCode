# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # if the list is just one node return that node
        # separate the list into two lists
        # add the nodes alternatively from the two lists
        # return dummy.next

        # separate the list into two
        if not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy 
        fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        l2_head = slow.next
        slow.next = None

        # reverse the second list
        prev = None
        curr = l2_head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        

        # recombining the two lists
        l1 = head
        l2 = prev

        res = ListNode(0)
        while l1 and l2:
            res.next = l1
            res = res.next
            l1 = l1.next

            res.next = l2
            res = res.next
            l2 = l2.next

        if l1:
            res.next = l1

        if l2:
            res.next = l2

        return res.next


