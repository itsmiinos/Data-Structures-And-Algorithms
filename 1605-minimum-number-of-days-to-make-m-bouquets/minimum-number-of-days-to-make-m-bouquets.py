class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = float('inf')
        high = float('-inf')

        if len(bloomDay) < m*k : 
            return -1

        for i in range(len(bloomDay)) : 
            low = min(low , bloomDay[i])
            high = max(high , bloomDay[i])
        
        result = self.doBinarySearch(low , high , bloomDay , m , k)
        return result
    
    def doBinarySearch(self , low : int , high : int , bloomDay : list[int], m : int, k : int) -> int : 
        ans = 0

        while low <= high : 

            mid = low + ((high - low) // 2)

            if self.calculateNumberOfFlowers(mid , bloomDay , k) >= m : 
                ans = mid
                high = mid - 1

            else : 
                low = mid + 1
        
        return ans
    
    def calculateNumberOfFlowers(self , day : int, bloomDay : list[int], k : int) -> int : 
        
        count = 0
        b_count = 0

        for i in range(len(bloomDay)) : 
            if day >= bloomDay[i] : 
                count+=1
                if count == k : 
                    count = 0
                    b_count +=1
            else : 
                count = 0

        return b_count