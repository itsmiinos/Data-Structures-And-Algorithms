# Last updated: 9/20/2025, 9:11:10 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None : 
            return []

        queue = []
        queue.append(root)
        result = []
        level = 1

        while len(queue) > 0 : 
            
            n = len(queue)
            temp = []

            while n > 0 : 

                node = queue.pop(0)
                temp.append(node.val)

                if node.left is not None : 
                    queue.append(node.left)
                if node.right is not None : 
                    queue.append(node.right)
                
                n-=1
            
            if level % 2 == 0 : 
                temp = self.reverseArray(temp)
            
            result.append(temp)
            level+=1
        
        return result


    def reverseArray(self , arr : list[int]) -> list[int] :

        i = 0
        j=len(arr)-1

        while i<=j : 
            [arr[i] , arr[j]] = [arr[j] , arr[i]]
            i+=1
            j-=1
        
        return arr
                
