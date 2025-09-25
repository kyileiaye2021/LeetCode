"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# map the original node to new node
# traverse the orig node
#   extract the copy
#   copy node random should point to the orig node random
#   copy node next should point to the orig node next

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        map = {None:None}
        curr= head

        while curr:
            new_node = Node(curr.val)
            map[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            copy = map[curr]
            copy.random = map[curr.random]
            copy.next = map[curr.next]
            curr = curr.next

        return map[head]        