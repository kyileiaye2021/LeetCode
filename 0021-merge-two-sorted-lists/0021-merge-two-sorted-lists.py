# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Happy cases
        # input: list1=[1,2,4], list2 = [1,3,4]
        # output: [1,1,2,3,4,4]

        # input: list1 = [3,5], list2 = [1]
        # output: [1, 3,5]

        # Edge case
        # input: list1 = [], list2 = [1,6]
        # output: [1,6]
        
        # input: list1 = [7,9,11], list2 = []
        # output: [7,9,11]

        # input: list1=[], list2=[]
        # output : []

        # Two pointer approach 
        # if head of list1 is empty, return head of list2
        # if head of list2 is empty, return the head of list1
        # if both heads are empty, return empty list
        # p, q pointers
        # create a dummy node
        # temp = dummy
        # traverse until p reaches end of list1 and q reaches the end of list2
        #   check if the p ele is less than q ele
        #       set the dummy.next to p 
        #   else
        #       set the dummy.next to q
        #   dummy = dummy.next
        # traverse until p reaches the end of list1
        #   set the dummy.next to p
        #   dummy = dummy.next
        # traverse until q reaches the end of list2
        #   set the dummy.next to q
        #   dummy = dummy.next
        # return temp.next

        if not list1:
            return list2

        if not list2:
            return list1

        p, q = list1, list2
        dummy = ListNode(0)
        temp = dummy
        while p and q:
            if p.val < q.val:
                dummy.next = p
                p = p.next

            else:
                dummy.next = q
                q = q.next

            dummy = dummy.next

        while p:
            dummy.next = p
            p = p.next
            dummy = dummy.next

        while q:
            dummy.next = q
            q = q.next
            dummy = dummy.next

        return temp.next
