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

        if not head : 
            return None

        while temp is not None : 
            copy_node_val = temp.val
            copy_node = Node(copy_node_val)

            next_node = temp.next
            temp.next = copy_node
            copy_node.next = next_node
            temp = temp.next.next

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        copy_head = head.next
        temp1 = head
        temp2 = copy_head

        while temp1:
            temp1.next = temp2.next
            temp1 = temp1.next
            if temp1:
                temp2.next = temp1.next
            temp2 = temp2.next
        
        return copy_head