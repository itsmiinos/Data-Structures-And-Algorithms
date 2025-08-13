# Last updated: 8/13/2025, 8:22:02 PM
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.hashmap = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap : 
            return -1
        
        else : 
            node = self.hashmap[key]
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail
            self.tail.prev = node

            value = node.val
            return value
        

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap : 

            node = self.hashmap[key]
            node.val = value

            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail
            self.tail.prev = node
            

            self.hashmap[key] = node
        
        else : 

            if len(self.hashmap) == self.size : 

                overflow_node = self.head.next
                overflow_node_next = overflow_node.next
                overflow_node_next.prev = self.head
                self.head.next = overflow_node_next

                #clean up : 
                overflow_node.next = None
                overflow_node.prev = None
                
                new_node = Node(key , value)
                last_node = self.tail.prev
                last_node.next = new_node
                new_node.prev = last_node
                self.tail.prev = new_node
                new_node.next = self.tail


                del self.hashmap[overflow_node.key]
                self.hashmap[key] = new_node
            
            else : 
                
                new_node = Node(key , value)
                
                last_node = self.tail.prev
                last_node.next = new_node
                new_node.prev = last_node
                self.tail.prev = new_node
                new_node.next = self.tail


                self.hashmap[key] = new_node
                


class Node : 
    def __init__(self , key  : int = None , value : int = None , prev = None, next = None) -> None : 
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)