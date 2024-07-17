# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # find the length of the two nodes
        # if list A len is greater, traverse the list A ahead by the difference  between list A and B
        # if list B len is greater, traverse the list B ahead
        # traverse both A and B to find the intersection node
        
        
        # find the length of the two nodes
        intersectVal = ListNode(0)
        listA = headA
        listB = headB
        
        listA_length = 0
        while listA:
            listA_length += 1
            listA = listA.next
        
        listB_length = 0
        while listB:
            listB_length += 1
            listB = listB.next
        
        skipA = 0
        skipB = 0
        listA = headA
        listB = headB
        
# if list A len is greater, traverse the list A ahead by the difference  between list A and B
        if listA_length > listB_length:
            for _ in range(listA_length - listB_length):
                listA = listA.next
                skipA += 1
              
    # if list B len is greater, traverse the list B ahead
        else:
            for _ in range(listB_length - listA_length):
                listB = listB.next
                skipB += 1
        
        # traverse both A and B to find the intersection node
        while listA and listB:
            if listA == listB:
                return listA
            listA = listA.next
            listB = listB.next
        
        return None # if no intersection is found
                