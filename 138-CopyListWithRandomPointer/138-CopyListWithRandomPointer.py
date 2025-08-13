# Last updated: 8/13/2025, 8:22:19 PM
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

        while temp is not None : 

            next_node = temp.next
            copy_node = Node(temp.val)
            temp.next = copy_node
            copy_node.next = next_node
            temp = temp.next.next
        
        temp = head

        while temp is not None : 

            random_node = temp.random
            copy_node = temp.next
            if random_node : copy_node.random = random_node.next
            temp = temp.next.next
        
        temp = head
        copy_head = head.next
        copy_temp = copy_head

        while temp is not None and copy_temp is not None : 
            next_original_node = copy_temp.next
            temp.next = next_original_node
            next_copy_node = next_original_node.next if next_original_node else None
            copy_temp.next = next_copy_node
            temp = temp.next
            copy_temp = copy_temp.next
        
        return copy_head
