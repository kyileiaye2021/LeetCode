# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        
        # split the list into 2 lists a and b until there are no nodes in the list

        # def merge(list1, list2):
        # h1 = list1, h2 = list2
        # dummy = ListNode()
        # curr = dummy
        # while h1 and h2:
        #   if h1.val < h2.val:
        #       curr.next = h1
        #       curr = curr.next
        #       h1 = h1.next
        #   else:
        #       curr.next = h2
        #       curr = curr.next
        #       h2 = h2.next
        # return dummy.next 


        # recur(head)
        # base case
        #   if not head and head.next:
        #       return head
        #   slow = head
        #   fast = head.next
        #   while fast and fast.next:
        #       slow = slow.next
        #       fast = fast.next.next
        #   head2 = slow.next
        #   slow.next = None
        #   list1 = recur(head)
        #   list2 = recur(head2)
        #   return merge(list1, list2)

        def merge(list1, list2):
            dummy = ListNode()
            curr = dummy
            h1 = list1
            h2 = list2

            while h1 and h2:
                if h1.val < h2.val:
                    curr.next = h1
                    h1 = h1.next
                else:
                    curr.next = h2
                    h2 = h2.next
                curr = curr.next

            if h1:
                curr.next = h1

            if h2:
                curr.next = h2

            return dummy.next

        def recur_split(head):
            # base case
            if not head or not head.next:
                return head

            # recursive case
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            head2 = slow.next
            slow.next = None

            list1 = recur_split(head)
            list2 = recur_split(head2)
            return merge(list1, list2)

        return recur_split(head)

