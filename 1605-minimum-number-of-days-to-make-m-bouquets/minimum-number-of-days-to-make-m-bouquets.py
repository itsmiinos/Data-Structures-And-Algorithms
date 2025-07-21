class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay) < m*k : # case where all the flowers cant make m * k
            return -1
        
        min_bloom_day = float('inf') # where we get only the first bloomed flower
        max_bloom_day = -float('inf') # where we get all the flowers

        for i in range(len(bloomDay)) : 
            min_bloom_day = min(min_bloom_day , bloomDay[i])
            max_bloom_day = max(max_bloom_day , bloomDay[i])

        result = self.doBinarySearch(min_bloom_day , max_bloom_day , m , k , bloomDay)
        return result
    
    def doBinarySearch(self , low : int , high : int , m : int, k : int, bloomDay : list[int]) -> int : 
        ans = 0

        while low <= high : 
            mid = low + (high - low)//2

            if self.calculateNumberOfFlowers(mid ,bloomDay , k) >= m : #we need to check whether the flowers in that day sums up to m*K
                ans = mid # that number of days can make M*K flowers but we need the minnimum
                high = mid - 1
            else : 
                low = mid + 1
        
        return ans
    
    def calculateNumberOfFlowers(self , day : int, bloomDay : list[int] , k : int) -> int : 
        running_sum = 0 
        count = 0
        for i in range(len(bloomDay)) : 
            if bloomDay[i] <= day : 
                running_sum+=1
                if running_sum == k : 
                    count+=1
                    running_sum = 0
            else : 
                running_sum = 0
        
        return count
