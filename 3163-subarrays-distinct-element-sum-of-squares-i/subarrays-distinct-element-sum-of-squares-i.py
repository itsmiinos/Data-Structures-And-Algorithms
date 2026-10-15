class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums)) :
            for j in range(i,len(nums)) :
                my_set = set()
                for k in range(i , j+1) :
                    my_set.add(nums[k])
            
                total_sum += len(my_set) ** 2
        
        return total_sum