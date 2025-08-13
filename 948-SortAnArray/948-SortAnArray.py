# Last updated: 8/13/2025, 8:18:19 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)

        #selection sort
        # for i in range(n-1) : 
        #     minele = nums[i]
        #     minindex = i
        #     for j in range(i+1 , n) : 
        #         if nums[j] < minele : 
        #             minindex = j
        #             minele = nums[j]
            
        #     temp = nums[i]
        #     nums[i] = nums[minindex]
        #     nums[minindex] = temp
        
        # return nums

        start = 0 
        end = n-1
        self.mergeHelper(nums , start , end)
        return nums
    
    def mergeHelper(self , nums : [int] , start : int , end : int) -> [int] :
        if start >= end : 
            return
        
        mid = start + (end - start)//2
        self.mergeHelper(nums , start , mid)
        self.mergeHelper(nums , mid+1 , end)
        self.merge(nums , start , mid , end)


    def merge(self , nums:[int] , start : int , mid : int , end:int) :
        p1 = start
        p2 = mid+1

        res = []*(end-start+1)
        p3=0
        while p1<mid+1 and p2<end+1: 
            if nums[p1] < nums[p2] : 
                res.append(nums[p1])
                p1+=1
            else : 
                res.append(nums[p2]) 
                p2+=1
                
        while p1<mid+1 : 
            res.append(nums[p1])
            p1+=1
        
        while p2<end+1 : 
            res.append(nums[p2])
            p2+=1
        
        for i in range(len(res)):
            nums[start + i] = res[i]

