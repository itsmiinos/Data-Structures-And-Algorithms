class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums)) :
            my_set = set()
            for j in range(i,len(nums)) :
                
                my_set.add(nums[j])
            
                total_sum += len(my_set) ** 2
        
        return total_sum