class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []

        for i in range(k) :
            while len(queue) > 0 and queue[-1] < nums[i] :
                queue.pop(-1)
            
            
            queue.append(nums[i])

        ans = []
        ans.append(queue[0])
        i = 0
        j = k

        
        while j < len(nums) :
            while len(queue) > 0 and nums[j] > queue[-1] :
                queue.pop(-1)
            
            queue.append(nums[j])
            

            if queue[0] == nums[i] :
                queue.pop(0)
            ans.append(queue[0])
            i+=1
            j+=1
        
        return ans
            

        