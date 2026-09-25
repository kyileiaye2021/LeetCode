class ListNode():
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList():
    def __init__(self):
        self.lru = ListNode()
        self.mru = ListNode()
        self.lru.next = self.mru
        self.mru.prev = self.lru
        self.size = 0

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1

    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
        self.size += 1

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.cache = {} # {key: Node}
        self.countMap = defaultdict(int) # {key: freq}
        self.ddlMap = defaultdict(LinkedList) # {freq: ddl}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # increment freq of key in countMap
        prev_freq = self.countMap[key]
         # update ddl in freq
        self.ddlMap[prev_freq].remove(self.cache[key])
        # update min freq
        if self.min_freq == prev_freq and self.ddlMap[prev_freq].size == 0:
            self.min_freq += 1

        self.countMap[key] += 1
        curr_freq = self.countMap[key]
        self.ddlMap[curr_freq].insert(self.cache[key])
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        # update the key value in the hashmap
        # update the freq of key
        # update the ddl (remove from the prev count dll and insert in the list of new count)
        if key in self.cache:
            prev_freq = self.countMap[key]
            self.ddlMap[prev_freq].remove(self.cache[key])
            # update min freq
            if self.min_freq == prev_freq and self.ddlMap[prev_freq].size == 0:
                self.min_freq += 1

            self.countMap[key] += 1
            curr_freq = self.countMap[key]
            node = self.cache[key]
            node.val = value
            self.ddlMap[curr_freq].insert(node)
            return


        # else
        # if len(ele) exceeds capacity, remove the ele that is least freq 
        # if there are multiple least freq ele, remove the most recent ones
        if len(self.cache) == self.cap:
            ll_to_remove = self.ddlMap[self.min_freq]
            lru_node = ll_to_remove.lru.next
            ll_to_remove.remove(lru_node)
            del self.cache[lru_node.key]
            del self.countMap[lru_node.key]
            
        # add the new key val in hashmap
        # update the freq of key
        # update the ddl (just insert in the list)
        self.countMap[key] = 1
        self.cache[key] = ListNode(key, value)
        self.ddlMap[1].insert(self.cache[key])
        self.min_freq = 1
            

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)