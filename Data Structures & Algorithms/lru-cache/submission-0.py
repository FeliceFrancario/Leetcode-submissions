class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.LR=Node(0,0)
        self.MR=Node(0,0)
        self.LR.next=self.MR
        self.MR.prev=self.LR

    def remove(self, node):
        prev, nxt =node.prev,node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        #nxt=self.MR
        node.next=self.MR
        node.prev=self.MR.prev
        prev=self.MR.prev
        prev.next=node
        self.MR.prev=node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            lru=self.LR.next
            self.remove(lru)
            del self.cache[lru.key]
        
