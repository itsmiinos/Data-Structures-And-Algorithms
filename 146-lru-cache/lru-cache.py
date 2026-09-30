class Node :
    
    def __init__(self , val = 0 , key = 0 , next = None , prev = None) -> None :
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.records = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.records :
            node = self.records[key]
            prevNode = node.prev
            nextNode = node.next

            nextNode.prev = prevNode
            prevNode.next = nextNode

            prevTailNode = self.tail.prev
            prevTailNode.next = node
            node.prev = prevTailNode
            node.next = self.tail
            self.tail.prev = node

            self.records[key] = node

            return node.val
        else :
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.records :
            node = self.records[key]
            prevNode = node.prev
            nextNode = node.next

            nextNode.prev = prevNode
            prevNode.next = nextNode

            prevTailNode = self.tail.prev
            prevTailNode.next = node
            node.prev = prevTailNode
            node.next = self.tail
            self.tail.prev = node
            node.val = value

            self.records[key] = node


        elif len(self.records) == self.cap :
            lastUsedNode = self.head.next
            del self.records[lastUsedNode.key]

            nextNode = lastUsedNode.next
            self.head.next = nextNode
            nextNode.prev = self.head

            node = Node(value , key)
            prevTailNode = self.tail.prev
            prevTailNode.next = node
            node.prev = prevTailNode
            node.next = self.tail
            self.tail.prev = node
            self.records[key] = node

        else :
            node = Node(value , key)
            prevTailNode = self.tail.prev
            prevTailNode.next = node
            node.prev = prevTailNode
            node.next = self.tail
            self.tail.prev = node
            self.records[key] = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)