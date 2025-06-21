#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,nums, n):
        #Your code here
        prefixCountZero = [0]*(len(nums))
        prefixCountOne = [0]*(len(nums))

        currentCount = 0
        for i in range(len(nums)) : 
            if nums[i] == 0 : 
                prefixCountZero[i] = currentCount + 1
                currentCount +=1
            else : 
                prefixCountZero[i] = currentCount
        currentCount = 0
        for i in range(len(nums)) : 
            if nums[i] == 1 :
                prefixCountOne[i] = currentCount+1
                currentCount +=1
            else : 
                prefixCountOne[i] = currentCount
        count = 0
        map = {}
        map[0] = 1
        for i in range(len(nums)) :
            diff = prefixCountZero[i] - prefixCountOne[i]
            count += map.get(diff , 0)
            map[diff] = map.get(diff , 0 )+1
        return count