# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # happy case
        # head = [1,2,3,4,5]
        # output = 3

        # head = [1,2,3,4]
        # output = 3

        # edge case
        # head = [1]
        # output = 1

        # fast slow pointer approach
        # fast, slow = head, head
        # traverse the linked list from the head until the fast pointer becomees none
        #   move slow by 1 node
        #   move fast by 2 nodes
        # return slow
        
        # 1 -> 2 -> 3 -> 4
        fast, slow = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
