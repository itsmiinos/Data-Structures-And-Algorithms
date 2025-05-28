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

        while temp is not None : 
            copy_node = Node(temp.val)
            copy_node.next = temp.next
            temp.next = copy_node
            temp = temp.next.next
        
        temp = head
        
        while temp is not None : 
            copy_node = temp.next
            if temp.random is None : 
                copy_node.random = None
            else :
                copy_node.random = temp.random.next
            temp = temp.next.next
        
        dummyNode = Node(-1)
        temp = head
        copy_temp = dummyNode

        while temp is not None : 
            copy_temp.next = temp.next
            temp.next = temp.next.next
            copy_temp = copy_temp.next
            temp = temp.next

        return dummyNode.next
            