# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # happy cases
        # input: [1,1,3,5]
        # output: [1,3,5]

        # input: [1,3,3,6,7]
        # output: [1,3,6,7]

        # input: [1,3,3,4,8,8,9]
        # output: [1,3,4,8,9]

        # edge cases
        # input: []
        # output: []

        # input: [2]
        # output: [2]

        # input: [1,1,1,1]
        # output: [1]
        
        # input: [4,5,6,9]
        # output: [4,5,6,9]

        # Set and traversal approach
        # if the list is none,
        #   return none
        # create a hashset
        # temp pointer pointing to the head node
        # traverse the list until the next of temp is none
        #   check if the temp.next is already visited
        #       set the temp.next = temp.next.next
        #   else: add the next node data in the set
        #   set the temp to temp.next
        # return head

        if not head:
            return None

        temp = head
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head

            