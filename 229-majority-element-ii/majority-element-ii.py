class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        val1 = nums[0]
        count1=1
        val2 = nums[0]
        count2=0

        for i in range(1,n) : 
            if nums[i] == val1 : 
                count1+=1
            
            elif nums[i] == val2 : 
                count2+=1
            elif count1==0:
                val1 = nums[i]
                count1=1
            elif count2==0 : 
                val2 = nums[i]
                count2 = 1

            elif nums[i]!=val1 and nums[i]!=val2 : 
                count1-=1
                count2-=1
        
        
        result = []
        c1=0
        c2=0
        if nums.count(val1) > n//3 : 
            result.append(val1)
        if val1!=val2 and nums.count(val2) > n//3 : 
            result.append(val2)

        return result