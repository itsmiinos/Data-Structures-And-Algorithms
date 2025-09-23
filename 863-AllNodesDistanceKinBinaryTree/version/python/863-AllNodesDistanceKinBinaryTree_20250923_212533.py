# Last updated: 9/23/2025, 9:25:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}
        queue = []

        queue.append(root)

        while len(queue) > 0 : 
            rem = queue.pop(0)

            if rem.left is not None : 
                queue.append(rem.left)
                parent_map[rem.left] = rem
            
            if rem.right is not None : 
                queue.append(rem.right)
                parent_map[rem.right] = rem
        

        level = 0
        queue = []
        queue.append(target)
        visited = set()
        visited.add(target)

        while len(queue) > 0 and level < k:

            n = len(queue)

            while n > 0 : 

                temp = queue.pop(0)

                if temp.left is not None and temp.left not in visited : 
                    queue.append(temp.left)
                    visited.add(temp.left)
                
                if temp.right is not None and temp.right not in visited : 
                    queue.append(temp.right)
                    visited.add(temp.right)
                
                if temp in parent_map and parent_map[temp] not in visited : 
                    queue.append(parent_map[temp])
                    visited.add(parent_map[temp])
            
                n-=1

            level +=1
        
        return [node.val for node in queue]
        
            

        