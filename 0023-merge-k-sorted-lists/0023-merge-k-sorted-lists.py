# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, curr1, curr2):
        dummy = temp = ListNode(0)
        while curr1 and curr2:
            if curr1.val > curr2.val:
                temp.next = curr2
                curr2 = curr2.next
            else:
                temp.next = curr1
                curr1 = curr1.next
            temp = temp.next

        if curr1:
            temp.next = curr1
        if curr2:
            temp.next = curr2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                curr1 = lists[i]
                curr2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.merge(curr1, curr2))

            lists = mergedList

        return lists[0]


