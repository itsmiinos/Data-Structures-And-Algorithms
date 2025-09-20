# Last updated: 9/20/2025, 10:37:42 PM
from typing import Optional, List
from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        map = defaultdict(list)
        queue = deque()
        queue.append((root, 0, 0))  # (node, vertical_level, depth)

        while queue:
            node, vertical_level, depth = queue.popleft()
            map[vertical_level].append((depth, node.val))

            if node.left:
                queue.append((node.left, vertical_level - 1, depth + 1))
            if node.right:
                queue.append((node.right, vertical_level + 1, depth + 1))

        result = []
        for key in sorted(map.keys()):
            column = sorted(map[key], key=lambda x: (x[0], x[1]))  # sort by depth, then value
            result.append([val for _, val in column])

        return result
