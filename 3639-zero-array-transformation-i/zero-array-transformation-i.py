class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0]*(n+1) #+1 for the dummy value

        for inner_list in queries : 
            i = inner_list[0]
            j = inner_list[1]
            self.difference_increase( diff , i , j , 1)

        for i in range(1, len(diff)) : 
            diff[i] = diff[i] + diff[i-1]
        
        for i in range (len(nums)) :
            if diff[i] < nums[i]:
                return False
        
        return True
        
    
    def difference_increase(self , diff : [int] , i : int , j : int , val) :
        diff[i] += 1
        diff[j+1] -=1
