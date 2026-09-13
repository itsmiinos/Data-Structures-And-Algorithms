class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dequeue = collections.deque()
        ans = []
        for i in range(len(nums)) : 
            if len(dequeue) > 0 and dequeue[0] < i - k + 1 :
                dequeue.popleft()
            
            while len(dequeue) > 0 and nums[dequeue[-1]] < nums[i] :
                dequeue.pop()
            
            dequeue.append(i)

            if i >= k-1 :
                ans.append(nums[dequeue[0]])
            
        return ans