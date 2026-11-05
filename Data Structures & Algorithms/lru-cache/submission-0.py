class Node:
    
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self, node):
        pre=node.prev
        nex=node.next
        pre.next=nex
        nex.prev=pre
      
    def add_to_tail(self, node):
        pre=self.tail.prev
        pre.next=node
        node.prev=pre
        node.next=self.tail
        self.tail.prev=node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
        else:
            node=Node(key, value)
            self.cache[key]=node
        self.add_to_tail(node)
        if len(self.cache)>self.cap:
            h=self.head.next
            self.remove(h)
            del self.cache[h.key]

