"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # new_node hashmap 
        # original node -> new node
        # 7 -> 7_new
        # 13 -> 13_new

        # dummy node

        # hashmap 
        # index -> original node
        # 0 -> 7
        # 1 -> 13

        # traverse the orig ll
        # check if the node is not in new_node hashmap
        #   create a new node with original val
        #   add the new node to new_node hashmap
        # else
        #   res.next = new node from new_node hashmap
        #   res = res.next
        # check if the random node is not in new_node hashmap
        #   create a new node and add it to new_node hashmap
        # else
        #   append the created new node from new_node hashmap
        #   res.random = new_node
        # cur = cur.next
        # return dummy.next

        new_node_map = {None : None}
        curr = head
        copied = ListNode(0)
        res = copied

        while curr:
            if curr not in new_node_map:
                new_node = ListNode(curr.val)
                new_node_map[curr] = new_node
            
            res.next = new_node_map[curr]
            res = res.next

            if curr.random not in new_node_map:
                new_node = ListNode(curr.random.val)
                new_node_map[curr.random] = new_node
            
            res.random = new_node_map[curr.random]
            curr = curr.next
        
        return copied.next
                

        