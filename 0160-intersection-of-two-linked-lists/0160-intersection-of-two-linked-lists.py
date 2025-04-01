# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Happy cases
        # input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
        # output: 8

        # input: listA = [1,4,3,2], listB = [5,3,2]
        # output: 3

        # input: listA = [5,6,2,1], listB = [1,4,1]
        # output: 1

        # Edge cases
        # input: listA = [7,5,1], listB = [4,2,6]
        # output: None

        # input: listA = [1], listB = [1]
        # output: 1

        # input: listA = [3,5,6], listB = [3,5,6]
        # output: 3

        # Brute force - traverse the list and in each iteration, traverse the second list and check if the curr node is equal to the outer curr node - O(n*m) time, O(1) space

        # Hashset - traverse 1 list and store the nodes in hashset. Then, traverse another list and check if there are the same nodes - O(n) time, O(n) space

        # Find length and first traverse the longer list and traverse both lists simultaneously later - O(n + m) time, and O(1) space - Two pass

        # Two pointer
        # p and q pointers pointing to heads of listA and listB
        # traverse the list until p reaches the end
        # if p reaches the end, point it to the head of listB
        # traverse the list until q reaches the end
        # if p reaches the end, point it to the head of listB
        # do the above until 

        curr1 = headA
        curr2 = headB
        len1 = 0
        len2 = 0
        while curr1:
            len1 += 1
            curr1 = curr1.next

        while curr2:
            len2 += 1
            curr2 = curr2.next

        curr1 = headA
        curr2 = headB
        diff = 0
        if len1 > len2:
            diff = len1 - len2
            for _ in range(diff):
                curr1 = curr1.next
        else:
            diff = len2 - len1
            for _ in range(diff):
                curr2 = curr2.next

        while curr1 and curr2:
            if curr1 == curr2:
                return curr1

            curr1 = curr1.next
            curr2 = curr2.next

        return None

        # move the longer list diff node ahead
       