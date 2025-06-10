class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        value1 = nums[0]
        count1 = 1
        value2 = nums[0]
        count2 = 0

        for i in range (1, len(nums)):
            if nums[i] == value1 : 
                count1+=1
            elif nums[i] == value2 : 
                count2+=1
            
            elif count1 == 0 :
                count1 = 1
                value1 = nums[i]

            elif count2 == 0 : 
                count2 = 1
                value2 = nums[i]
            
            elif nums[i]!= value1 and nums[i]!=value2 : 
                count1-=1
                count2-=1
            
        cnt1 = 0
        cnt2 = 0
        ans = []
        for i in range(len(nums)) : 
            if nums[i] == value1 : 
                cnt1 +=1
            elif nums[i] == value2 : 
                cnt2 +=1
        
        if cnt1 > len(nums)//3 : 
            ans.append(value1)
        if cnt2 > len(nums)//3 : 
            ans.append(value2)
        
        return ans