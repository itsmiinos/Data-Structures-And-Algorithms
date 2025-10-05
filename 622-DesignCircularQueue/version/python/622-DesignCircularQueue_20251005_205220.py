# Last updated: 10/5/2025, 8:52:20 PM
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.head = Node()
        self.temp = self.head
        self.list_size = 0

    def enQueue(self, value: int) -> bool:
        if self.list_size == self.size : 
            return False
        
        else : 
            self.temp.next = Node(value)
            self.temp = self.temp.next
            self.list_size +=1

            return True

    def deQueue(self) -> bool:
        if self.list_size == 0: 
            return False
        
        else : 
            self.head = self.head.next
            self.list_size -=1
            return True

    def Front(self) -> int:
        if self.list_size == 0 :
            return -1
        
        else : 
            return self.head.next.val

    def Rear(self) -> int:

        if self.list_size == 0 : 
            return -1
        
        else : 
            return self.temp.val
        

    def isEmpty(self) -> bool:

        if self.list_size == 0 : 
            return True
        
        return False
        

    def isFull(self) -> bool:

        if self.list_size == self.size : 
            return True
        
        return False

class Node :
    def __init__(self , val = None , next = None) : 
        self.val = val
        self.next = next
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()