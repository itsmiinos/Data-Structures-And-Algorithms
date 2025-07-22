class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashmap = {}
        window_size = 0
        max_sum = 0

        for i in range(len(nums)) : 
            if nums[i] in hashmap : 
                break
            else : 
                hashmap[nums[i]] = i
                window_size+=1
                max_sum += nums[i]
        
        i = window_size
        start = 0
        sum = max_sum

        while i < len(nums) : 
            if nums[i] in hashmap : 
                index = hashmap[nums[i]]
                while start <= index : 
                    del hashmap[nums[start]]
                    sum -= nums[start]
                    start +=1
            
            hashmap[nums[i]] = i
            sum+=nums[i]
            window_size = max(window_size , i - start + 1)
            max_sum = max(sum , max_sum)
            i+=1
        
        return max_sum
