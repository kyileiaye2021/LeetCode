class ListNode():
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = ListNode()
        self.mru = ListNode()
        self.lru.next = self.mru
        self.mru.prev = self.lru
        self.capacity = capacity
        self.hashmap = {}

    def remove(self, node): # remove from the list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node): # insert the node at the right
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:

        if key in self.hashmap:
            # update the node as mru
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val

        return -1
        
    def put(self, key: int, value: int) -> None:
        # if key is already in hashmap: update teh value in hashmap and remove the node and update the node as mru
        if key in self.hashmap:
            self.remove(self.hashmap[key])
    
        # if key is not in hashmap
        self.hashmap[key] = ListNode(key, value)
        self.insert(self.hashmap[key])

        # if the len exceeds capacity, remove lru 
        if len(self.hashmap) > self.capacity:
            lru_node = self.lru.next
            self.remove(lru_node)
            del self.hashmap[lru_node.key]
        
        



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)