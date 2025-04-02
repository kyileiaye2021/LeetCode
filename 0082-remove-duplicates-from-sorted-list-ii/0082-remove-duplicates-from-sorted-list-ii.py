# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Happy cases
        # input: head = [1,2,3,3,4,5]
        # output: [1,2,4,5]

        # input: head = [1,1,2,3]
        # output: [2,3]

        # input: head = [1,2,4,5,5]
        # output: [1,2,4]

        # edge cases
        # input: []
        # output: []

        # input: [2]
        # output: [2]

        # input: [1,1,1,1,1]
        # output: []

        # input: [1,2,3,4]
        # output: [1,2,3,4]

        # Two pointer Traversal Approach
        # prev = listNode(0)
        # temp = prev
        # curr = head
        # traverse the list until curr next is none
        #   check if the curr next data is equal to the curr data
        #       set the curr next to curr next next
        #       set prev next to curr next     
        #   else:
        #       set prev to curr
        #       set curr to curr.next
        # return temp.next

        if not head:
            return None

        prev = ListNode(0)
        temp = prev
        curr = head
        prev.next = curr
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.next.val == curr.val:
                    curr.next = curr.next.next
                prev.next = curr.next
                curr = curr.next

            else:
                prev = prev.next
                curr = curr.next

        return temp.next