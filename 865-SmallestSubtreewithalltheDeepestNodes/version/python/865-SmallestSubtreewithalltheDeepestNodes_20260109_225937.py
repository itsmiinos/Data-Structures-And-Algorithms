# Last updated: 1/9/2026, 10:59:37 PM
1class Solution:
2    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
3
4        def dfs(node):
5            if not node:
6                return (0, None)
7
8            left_depth, left_node = dfs(node.left)
9            right_depth, right_node = dfs(node.right)
10
11            if left_depth > right_depth:
12                return (left_depth + 1, left_node)
13            if right_depth > left_depth:
14                return (right_depth + 1, right_node)
15
16            # depths equal → this node is LCA
17            return (left_depth + 1, node)
18
19        return dfs(root)[1]