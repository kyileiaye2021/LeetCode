# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Happy cases
        # input: head = [1,2,3,5,8]
        # output: [1,3,8,2,5]

        # input: head = [3,5,4,7]
        # output: [3,4,5,7]

        # edge cases
        # input: head = []
        # output: []

        # input: head = [3]
        # output: [3]

        # input: head = [5,8]
        # output: [5,8]

        # Brute force - 2 pass solution
        # Two pointers 
        # if there is no ele in the list or only one ele in the list:
        #   return head
        # curr pointer to head
        # i = 1
        # 2 dummy nodes
        # odd dummy node
        # even dummy node
        # odd_dummy.next = head
        # even_dummy.next = head.next
        # prev_odd = odd_dummy
        # prev_even = even_dummy
        # traverse the list until curr is none 
        #   check if i is odd:
        #       set the next of prev_odd to curr
        #       set prev_odd to curr
    
        #   else:
        #       set the next of prev_even to curr
        #       set prev_even to curr
        #   set curr to curr.next
        #   increment i by 1
        # set the prev_odd.next to even_dummy.next
        # return odd_dummy.next

        if not head or not head.next:
            return head

        curr = head
        i = 1
        odd_dummy = ListNode(0,head)
        even_dummy = ListNode(0, head.next)
        prev_odd = odd_dummy
        prev_even = even_dummy

        while curr:
            if i % 2 != 0:
                prev_odd.next = curr
                prev_odd = curr
            
            else:
                prev_even.next = curr
                prev_even = curr
            
            curr = curr.next
            i += 1
        prev_even.next = None
        prev_odd.next = even_dummy.next
        return odd_dummy.next


