# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create a head of the merged linked list
        # create a temp pointer to keep track of the head of the merged lst
        # iterate over the lists until one of the list ends
        #   check if the curr val of which list is smaller
        #       link it to the next of the merged linked list
        # if there are nodes in one of the lists, add them to the merged list
        # retur temp.next
        
        merged_lst = ListNode()
        temp_head = merged_lst
        
        while list1 and list2:
            if list1.val < list2.val:
                merged_lst.next = list1
                list1 = list1.next
            else:
                merged_lst.next = list2
                list2 = list2.next
            merged_lst = merged_lst.next
            
        while list1:
            merged_lst.next = list1
            list1 = list1.next
            merged_lst = merged_lst.next
            
        while list2:
            merged_lst.next = list2
            list2 = list2.next
            merged_lst = merged_lst.next
            
        return temp_head.next