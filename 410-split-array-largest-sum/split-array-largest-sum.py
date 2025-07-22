class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        minimum_sum = -float('inf')
        maximum_sum = 0

        for i in range(len(nums)) : 
            minimum_sum = max(minimum_sum , nums[i])
            maximum_sum += nums[i]
        
        result = self.doBinarySearch(minimum_sum , maximum_sum , nums , k)
        return result
    
    def doBinarySearch(self , low : int , high : int , nums : list[int] , k: int) -> int : 
        ans = 0

        while low<=high : 
            mid = low + (high - low) // 2

            if self.calculatePartitionsForGivenSum(mid , nums) <= k : 
                ans = mid
                high = mid - 1
            
            else : 
                low = mid + 1
        
        return ans
    
    def calculatePartitionsForGivenSum(self , n : int , nums : list[int]) -> int : 
        count = 0
        running_sum = 0
        for i in range(len(nums)) : 
            if running_sum + nums[i] > n : 
                count+=1
                running_sum = 0
            running_sum += nums[i]

        return count+1
