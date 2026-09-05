class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

def trace(node):
    while node:
        print(node.key, node.val, node.prev, node.next)
        node = node.next

class LRUCache:

    def __init__(self, capacity: int):
        self.in_cache = dict()
        self.capacity = capacity
        self.head = None
        self.tail = None

    def pull_and_make_head(self, node):
        print("===", node.key, node.val, node.next, node.prev)
        if self.head == node:
            print("is head")
            pass
        elif self.tail == node:
            print("is tail")
            old_head, old_tail = self.head, self.tail
            new_tail = old_tail.prev
            new_tail.next = None
            self.tail = new_tail
            node.next = old_head
            node.prev = None
            old_head.prev = node
            self.head = node
        else:
            print("is middle")
            node.prev.next = node.next
            node.next.prev = node.prev
            old_head = self.head
            node.next = old_head
            node.prev = None
            old_head.prev = node
            self.head = node

    def pop_tail(self):
        old_tail, new_tail = self.tail, self.tail.prev
        self.tail = new_tail
        new_tail.next = None
        self.in_cache.pop(old_tail.key)

    def push_head(self, node):
        self.in_cache[node.key] = node
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def get(self, key: int) -> int:
        print("Get")
        if key not in self.in_cache:
            return -1

        # Find the node
        node = self.in_cache[key]
        self.pull_and_make_head(node)

        trace(self.head)
        print(self.head)
        print(self.tail)

        return node.val

    def put(self, key: int, value: int) -> None:
        print("Put")
        if key in self.in_cache:
            node = self.in_cache[key]
            node.val = value
            self.pull_and_make_head(node)
        else: # key not in in_cache
            size = len(self.in_cache)
            new_node = ListNode(key, value, None, None)
            self.push_head(new_node)
            if size == self.capacity:
                self.pop_tail()
        trace(self.head)
        print(self.head)
        print(self.tail)
