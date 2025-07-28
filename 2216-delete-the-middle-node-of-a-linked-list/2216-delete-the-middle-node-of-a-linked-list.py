# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [1, 2, 3, 4, 5] 
        #  psf
        #     ps  f
        #        s     f       
        
        # [1, 2, 3, 4]
        # p.  s  f
        #     p  s     f
        
        # s = 1
        # f = 2
        # s = 2
        # f = 4 
        # s = 3
        # f = null
        
        # slow and fast pointer
        # [1,3,4,7,1,2,6]
        #psf
        #  p s f
        #    p s f
        #      p s   f 
        #                f=None  
        
        
        # [1, 2, 3, 4]
        # p.  s. f
        #      p  s    f=None 
        slow, fast = head, head
        prev = None
        
        while(fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if(prev):
            prev.next = slow.next
            return head
        else:
            return None
