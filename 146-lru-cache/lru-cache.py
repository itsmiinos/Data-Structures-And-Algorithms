class ListNode : 

    def __init__ (self , key : int , value : int) : 
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.my_map = {}
        self.cap = 0
        self.total_cap = capacity
    
        self.head = ListNode(-1 , -1)
        self.tail = ListNode(-1 , -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.my_map : 
            remove_node = self.my_map.get(key)
            self.removeAnyNode(self.head, remove_node)
            self.addNode(self.tail , remove_node)
            return remove_node.value
        else :
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.my_map : 
            remove_node = self.my_map.get(key)
            self.removeAnyNode(self.head , remove_node)
            new_node = ListNode(key , value)
            self.addNode(self.tail , new_node)
            self.my_map[key] = new_node
        else :
            if self.cap == self.total_cap :
                oldest_node = self.head.next
                self.my_map.pop(oldest_node.key) 
                self.removeAnyNode(self.head , oldest_node)
                new_node = ListNode(key , value)
                self.addNode(self.tail , new_node)
                self.my_map[key] = new_node
            else :
                new_node = ListNode(key , value)
                self.addNode(self.tail , new_node)
                self.my_map[key] = new_node
                self.cap +=1

    def addNode(self , tail : Optional[ListNode] , new_node : Optional[ListNode]) -> None : 
        prev_node = tail.prev

        #addition of node : 
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = tail
        tail.prev = new_node

    def removeAnyNode(self , head : Optional[ListNode] , old_node : Optional[ListNode]) -> Optional[ListNode] :

        prev_node = old_node.prev
        next_node = old_node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        old_node.prev = None
        old_node.next = None

        return old_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)