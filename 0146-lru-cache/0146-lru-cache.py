class ListNode:
    def __init__(self, key=0, val = 0, prev =None, next =None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.lru = ListNode()
        self.mru = ListNode()
        self.lru.next = self.mru
        self.mru.prev = self.lru
        
    def insert(self, node):
        prev_node = self.mru.prev
        node.next = self.mru
        self.mru.prev = node
        node.prev = prev_node
        prev_node.next = node

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # calling get with the key, we need to make that key recent
            self.remove(self.hashmap[key]) # remove from linked list
            self.insert(self.hashmap[key]) # add to linked list 
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])

        self.hashmap[key] = ListNode(key, value)
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.capacity:
                lru_node = self.lru.next
                self.remove(lru_node) # remove the lru cache
                del self.hashmap[lru_node.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)