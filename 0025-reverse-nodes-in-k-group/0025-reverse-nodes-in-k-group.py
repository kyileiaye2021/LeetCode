# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # happy cases
        # 1, 2, 3, 4, 5, k = 2
        # 2, 1, 4, 3, 5

        # 1, 2, ,3, 4, 5, 6, k = 2
        # 2,1,4,3,6,5

        # 1,2,3,4,5, k = 3
        # 3,2,1,4,5
        
        # 1, k = 1
        # 1

        # 1,2,k=1
        # 1,2

        # if k = 1, return head
        # dummy node and add the head to it
        # prevL = dummy
        # curr = head
        # k_ele = false

        # future right = curr
        # while curr and curr.next:

        #   check if there are k ele
        #       if there are k ele, k_ele = true
        #
        #   if k_ele
            #   # reverse the list for k times
            #   prev = none
            #   traverese the list for k times
            #       next node = curr.next
            #       curr.next = prev
            #       prev = curr
            #       curr = next
            #else
            #   break
        #
        #   prevL.next = prev

        #   future_right.next = curr
        # return dummy.next

        if k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prevL = dummy
        curr = head
        k_ele = True

        while curr and curr.next:
            print("curr: ", curr.val )
            future_right = curr

            temp = curr
            for _ in range(k):
                if temp == None:
                    k_ele = False
                    break
                temp = temp.next
            if temp:
                print('temp: ', temp.val)
            prev = None
            if k_ele:
                # reverse the sublist
                for _ in range(k):
                    next_node = curr.next 
                    curr.next = prev
                    prev = curr
                    curr = next_node

            else:
                break

            prevL.next = prev
            future_right.next = curr
            prevL = future_right
            if curr:
                print('After reversing, curr: ', curr.val)
        
        return dummy.next


