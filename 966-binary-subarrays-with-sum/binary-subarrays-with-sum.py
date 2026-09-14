class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_map = collections.defaultdict(int)
        sum = 0
        count = 0
        my_map[0] = 1

        for i in range(len(nums)) :
            sum+= nums[i]
            diff = sum - goal
            if diff in my_map :
                count += my_map[diff]
           
            my_map[sum] += 1
        
        return count
