# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head:
            return True

        if not head.next:
            return True

        def find_mid(slow, fast):
            # base case
            if not fast or not fast.next:
                return slow

            # recursive case
            return find_mid(slow.next, fast.next.next)

        def reverse(head, prev):
            # base case
            if not head:
                return prev

            # recursive case
            next_node = head.next
            head.next = prev
            return reverse(next_node, head)

        def isPalindrome(head1, head2):
            # base case
            if not head2:
                return True

            # recursive case
            if head1.val != head2.val:
                return False
            
            return isPalindrome(head1.next, head2.next)

        dummy = ListNode()
        dummy.next = head
        slow = find_mid(dummy, dummy)
        cur = slow.next
        slow.next = None
        prev = None
        head2 = reverse(cur, prev) # reverse the second portion
        return isPalindrome(head, head2)




