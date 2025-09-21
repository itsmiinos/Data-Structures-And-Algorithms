# Node Class:
class Node:
    def __init__(self, val):  # ✅ Fixed constructor
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isSumProperty(self, root):
        if root is None:
            return True
        
        if root.left is None and root.right is None:
            return True
        
        left_data = root.left.data if root.left is not None else 0
        right_data = root.right.data if root.right is not None else 0
        
        if root.data == left_data + right_data:
            return self.isSumProperty(root.left) and self.isSumProperty(root.right)
        
        return False
