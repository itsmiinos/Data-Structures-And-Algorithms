# Last updated: 8/13/2025, 8:22:50 PM
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = self.second = self.prev = None

        def inorder(node: TreeNode):
            if not node:
                return

            inorder(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                    self.second = node
                else:
                    self.second = node

            self.prev = node
            inorder(node.right)

        inorder(root)
        # Swap the values of the two nodes
        self.first.val, self.second.val = self.second.val, self.first.val
