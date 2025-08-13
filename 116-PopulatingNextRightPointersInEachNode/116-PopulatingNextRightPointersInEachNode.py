# Last updated: 8/13/2025, 8:22:36 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None : 
            return root
        
        leftmost = root

        while leftmost.left is not None : 
            head = leftmost

            while head : 
                head.left.next = head.right

                if head.next is not None : 
                    head.right.next = head.next.left
                
                head = head.next
            
            leftmost = leftmost.left
        
        return root

