# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        sec_list = ListNode(0)
        temp = sec_list

        first = head
        second = first.next

        while second and second.next:
            temp.next = second
            temp = temp.next

            first.next = second.next
            second = second.next.next
            first = first.next

        temp.next = second
        if second:
            first.next = None

        curr = head
        while curr.next:
            curr = curr.next

        curr.next = sec_list.next
        return head