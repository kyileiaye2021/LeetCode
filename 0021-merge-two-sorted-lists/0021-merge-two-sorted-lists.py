# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # happy case
        # input: list1 = [1], list2 = [1,2]
        # output: [1,1,2]

        # input: list1 = [2,3], list2 = [2]
        # output: [2,2,3]

        # edge case
        # input: list1 = [], list2 = [2]
        # output: [2]

        # input; list1 = [1], list2 = []
        # output: [1]

        # first, create a empty node
        # create two pointers
        # iterate until one pointer reaches to the end of the linked list
        #   check if the which pointer has smaller value
        #       append the smaller node to the empty node
        #       move the corresponding pointer to the next node
        # return the next of the empty node

        new_node = ListNode()
        merged = new_node

        i, j = list1, list2

        while i and j:
            if i.val > j.val:
                new_node.next = j
                j = j.next
            else:
                new_node.next = i
                i = i.next
            new_node = new_node.next

        while i:
            new_node.next = i
            new_node = new_node.next
            i = i.next

        while j:
            new_node.next = j
            new_node = new_node.next
            j = j.next

        return merged.next
