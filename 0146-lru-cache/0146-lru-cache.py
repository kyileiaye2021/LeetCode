class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to nodes
        self.left = ListNode(0,0) #lru
        self.right = ListNode(0,0) #mru
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node): # removing node from the list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node): # inserting the node at right
        prev, nxt = self.right.prev, self.right
        prev.next, node.prev = node, prev
        nxt.prev, node.next = node, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # update the lru
            # remove from the list
            # add it at the right
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = ListNode(key, value)
        self.insert(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)