# Last updated: 9/27/2025, 10:55:23 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root is not None : 
            self.stack.append(root)
            root = root.left
        

    def next(self) -> int:
        popped = self.stack.pop(-1)
        ans = popped.val
        if popped.right is not None : 
            popped = popped.right
            while popped is not None : 
                self.stack.append(popped)
                popped = popped.left
        
        return ans

    def hasNext(self) -> bool:
        if len(self.stack) > 0 : 
            return True
        
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()