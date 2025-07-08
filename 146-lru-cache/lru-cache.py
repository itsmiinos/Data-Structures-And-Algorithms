class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.head = ListNode(0 , 0)
        self.tail = ListNode(0 , 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.my_map = {} # {key : ListNode}

    def get(self, key: int) -> int:
        if key in self.my_map : 
            node = self.my_map[key]
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            node.prev = None
            node.next = None

            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail
            self.tail.prev = node

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.my_map : 
            node = self.my_map[key]
            prev_node = node.prev
            next_node = node.next
            node.val = value

            prev_node.next = next_node
            next_node.prev = prev_node

            node.prev = None
            node.next = None

            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail
            self.tail.prev = node

            self.my_map[key] = node

            return


        if len(self.my_map) < self.size : 
            node = ListNode(value , key)
            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail
            self.tail.prev = node
    
            self.my_map[key] = node
        
        else : 
            node_to_remove = self.head.next
            next_node_to_remove = node_to_remove.next
            next_node_to_remove.prev = self.head
            self.head.next = next_node_to_remove

            node_to_remove.next = None
            node_to_remove.prev = None
            key_to_remove = node_to_remove.key

            del self.my_map[key_to_remove]

            node = ListNode(value , key)
            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail
            self.tail.prev = node
    
            self.my_map[key] = node



class ListNode :
    def __init__(self , value : int , key : int , next = None , prev = None ) :
        self.val = value
        self.next = next
        self.prev = prev
        self.key = key


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)