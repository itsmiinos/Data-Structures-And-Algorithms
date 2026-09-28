"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        if head is None : 
            return None
        # making a copy node
        while temp is not None :
            copyNode = Node(temp.val)
            nextNode = temp.next
            temp.next = copyNode
            copyNode.next = nextNode
            temp = temp.next.next
        
        temp = head
        # making copy of random pointer
        while temp is not None :
            randomNode = temp.random
            copyNode = temp.next
            if randomNode is not None : 
                copyNode.random = randomNode.next
            temp = temp.next.next
        
        dummyNode = Node(0)
        dummyNode.next = head.next
        temp = head
        
        while temp is not None:
            copyNode = temp.next
            nextNode = copyNode.next
            temp.next = nextNode
            if nextNode is not None:
                copyNode.next = nextNode.next
            else:
                copyNode.next = None
            temp = nextNode
        
        return dummyNode.next