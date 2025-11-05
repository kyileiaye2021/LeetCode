class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.capacity = capacity
        self.tail = Node()
        self.head = Node()
        self.tail.prev = self.head
        self.head.next = self.tail
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def push(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        return node
    
    def promote(self, node):
        self.remove(node)
        self.push(node)
    
    def pop(self):
        node = self.head.next
        self.remove(node)
        return node.val
        
    def get(self, key: int) -> int:
        if key in self.data:
            self.promote(self.data[key])
            return self.data[key].val[1]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            self.data[key] = self.push(Node((key, value)))
        else:
            self.data[key].val = (key, value)
            self.promote(self.data[key])
        if len(self.data) > self.capacity:
            key, _ = self.pop()
            del self.data[key]
            
            
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)