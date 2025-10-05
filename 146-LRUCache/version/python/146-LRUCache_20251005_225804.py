# Last updated: 10/5/2025, 10:58:04 PM
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashmap = {}

        self.max_cap = capacity
        self.size = 0

    def get(self, key: int) -> int:
        
        if key in self.hashmap : 
            node = self.hashmap[key]

            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            second_last_node = self.tail.prev
            second_last_node.next = node
            node.prev = second_last_node

            node.next = self.tail
            self.tail.prev = node

            return node.val

        else : 
            return -1        

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap : 
            node = self.hashmap[key]
            node.val = value

            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            second_last_node = self.tail.prev
            second_last_node.next = node
            node.prev = second_last_node

            node.next = self.tail
            self.tail.prev = node

            self.hashmap[key] = node
        
        else : 

            if self.size == self.max_cap : 
                front_node = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

                key_to_del = front_node.key
                del self.hashmap[key_to_del]

                new_node = Node(key , value)

                second_last_node = self.tail.prev
                second_last_node.next = new_node
                new_node.prev = second_last_node

                new_node.next = self.tail
                self.tail.prev = new_node

                self.hashmap[key] = new_node
            
            else : 

                new_node = Node(key , value)

                second_last_node = self.tail.prev
                second_last_node.next = new_node
                new_node.prev = second_last_node

                new_node.next = self.tail
                self.tail.prev = new_node

                self.hashmap[key] = new_node

                self.size +=1

class Node:
    def __init__(self , key = None , val = None , next = None , prev = None) -> None :
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)