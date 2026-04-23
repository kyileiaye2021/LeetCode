# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(m *n) if we combine 1 list at a time
        # if we combine 2 list at a time until there is only 1 list left --> (O(nlogm))

        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_lst = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lst.append(self.merge(l1, l2))

            lists = merged_lst
        
        return lists[0]

    def merge(self, l1, l2):
        
        dummy = ListNode(0)
        res = dummy
        p1 = l1
        p2 = l2

        while p1 and p2:
            if p1.val > p2.val:
                res.next = p2
                p2 = p2.next
            
            else:
                res.next = p1
                p1 = p1.next
            res = res.next

        if p1:
            res.next = p1

        if p2:
            res.next = p2

        return dummy.next
            
                