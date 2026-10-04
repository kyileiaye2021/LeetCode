# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # recur(head1, head2)
        # base case
        # if not head1 and not head2:
        #   return None
        # if not head1
        #   return head2
        # if not head2
        #   return head1

        # recursive case
        # head1_next = head1.next
        # head1.next = head2
        # head2_next = head2.next
        # head2.next = recur(head1_next, head2_next)
        # return head1

        def find_middle(slow, fast):
            # base case
            if not fast or not fast.next:
                return slow

            # recursive case
            return find_middle(slow.next, fast.next.next)

        def reverse(head, prev):
            # base case
            if not head:
                return prev
            #recursive case

            next_node = head.next
            head.next = prev
            return reverse(next_node, head)
            

        def merge(head1, head2):
            # base case
            if not head1 and not head2:
                return None

            if not head1:
                return head2

            if not head2:
                return head1

            # recursive case
            head1_next = head1.next
            head1.next = head2
            head2_next = head2.next
            head2.next = merge(head1_next, head2_next)
            return head1

        slow = head
        fast = head

        slow = find_middle(slow, fast)
        start = slow.next
        slow.next = None
    
        head2 = reverse(start, None)
        merge(head, head2)
        

    