# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        def merge(head1, head2):
            # base case
            if not head1 and not head2:
                return None

            if not head1:
                return head2

            if not head2:
                return head1

            # recursive case
            if head1.val < head2.val:
                head1.next = merge(head1.next, head2)
                return head1

            else:
                head2.next = merge(head1, head2.next)
                return head2
            
        return merge(list1, list2)


