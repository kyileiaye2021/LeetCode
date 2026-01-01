# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = [1,2,3,4]
        # [2,1,4,3]

        # head = [1,2]
        # [2,1]

        # head = [1]
        # [1]

        # head = []
        # []

        # head = [1,2,3]
        # [2,1,3]

        # if only one node or no node, return node
        # curr -> head
        # flag = flase

        # dummy = node(0)
        # dummy = head
        # temp = dummy
        # slow = fast = dummy

        # while fast and fast.next
        #   if val != -1
        #       temp.next = fast
        #       temp = temp.next
        #       slow.next = fast.next
        #       
        #  slow = slow.next
        #  fast = move by 2 nodes

        # if fast:
        #   slow.next = fast.next
        # else
        #   slow.next = None

        # temp.next = fast

        # traverse the two list
        #   add l2 node
        #   add l1 node
        #   move the nodes by 1
        
        # add l1 nodes if l1

        # add l2 nodes if l2
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        sec_lst = ListNode(0)
        temp = sec_lst

        slow = fast = dummy
        while fast and fast.next:
            if fast.val != -1:
                temp.next = fast
                temp = temp.next
                slow.next = fast.next
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow.next = fast.next
        else:
            slow.next = None

        temp.next = fast

        res = ListNode(0)
        curr = res
        l1 = head
        l2 = sec_lst.next

        while l1 and l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

            curr.next = l1
            l1 = l1.next
            curr = curr.next
        
        if l1:
            curr.next = l1

        if l2:
            curr.next = l2

        return res.next
            
        

        