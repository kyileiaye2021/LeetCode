# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        
        l = head
        r = head
        def recur_palindrome(r):
            nonlocal l
            # base case
            if not r:
                return True

            if not recur_palindrome(r.next):
                return False

            if l.val != r.val:
                return False
            l = l.next
            return True

        return recur_palindrome(r)