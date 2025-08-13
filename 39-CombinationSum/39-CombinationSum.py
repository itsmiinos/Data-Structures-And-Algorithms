# Last updated: 8/13/2025, 8:23:54 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.helper(0 , 0 , candidates , target , [])
        return self.result
    
    def helper(self , index : int , sum : int , a : list[int] , target : int , res : list[int]) -> None : 
        if index >= len(a) : 
            if sum == target : 
                self.result.append(res[:])
            return
        if sum > target : 
            return
        res.append(a[index])
        self.helper(index , sum + a[index] ,a , target , res) #take the value but dont increment index
        res.pop()
        self.helper(index + 1 , sum , a , target , res) #dont take the value

        return None