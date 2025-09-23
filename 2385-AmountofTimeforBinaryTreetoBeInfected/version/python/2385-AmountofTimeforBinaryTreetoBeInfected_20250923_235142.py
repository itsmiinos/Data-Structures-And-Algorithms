# Last updated: 9/23/2025, 11:51:42 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_map = {}
        queue = []

        queue.append(root)
        total_nodes = 1

        start_node = None

        while len(queue) > 0 : 
            rem = queue.pop(0)
            if rem.val == start : 
                start_node = rem

            if rem.left is not None : 
                queue.append(rem.left)
                parent_map[rem.left] = rem
                total_nodes +=1
            
            if rem.right is not None : 
                queue.append(rem.right)
                parent_map[rem.right] = rem
                total_nodes +=1
        

        
        queue = []
        queue.append(start_node)
        visited = set()
        visited.add(start_node)
        time = -1

        while len(queue) > 0 :

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

            time +=1
        
        return time