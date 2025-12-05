# Last updated: 12/5/2025, 9:51:14 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        self.result = []
4        self.helper(candidates , 0 , target , [])
5        return self.result
6    
7    def helper(self , candidates : list , index : int , target : int , temp : list) -> None  :
8        if target == 0 : 
9            self.result.append(temp.copy())
10            return
11        
12        if index > len(candidates)-1 : 
13            return
14        
15        if candidates[index] <= target :
16            temp.append(candidates[index])
17            self.helper(candidates , index , target - candidates[index] , temp)
18            temp.pop(-1)
19            self.helper(candidates , index + 1 , target , temp) 
20
21        else : 
22            self.helper(candidates , index + 1 , target , temp)
23        