# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # happy cases
        # head = [1,2,3]
        # output: [3,2,1]

        # head = ['a', 'b']
        # output: ['b', 'a']

        # head = ['a', 'b', 1, 2]
        # output: []

        # head = [1]
        # output: [1]

        # edge case
        # head = []
        # output: []

        # Three pointers
        # curr pointer, prev pointer, next pointer
        # temp = head
        # traverse the linked list
        #   curr next = prev
        # 1 --> 2 2 --> 1
        # curr = head
        # prev = None
        # temp = curr.next
        # while temp.next
        #   curr.next = prev
        #   prev = curr
        #   curr = temp
        #   temp = temp.next 
        # return temp

        if not head: 
            return head

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev



        