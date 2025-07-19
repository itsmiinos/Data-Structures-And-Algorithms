class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_limit = self.findLeftLimit(nums , target)
        # print(left_limit)
        right_limit = self.findRightLimit(nums , target)

        return [left_limit , right_limit]

    
    def findRightLimit(self , nums : List[int] , target : int) -> int : 
        low = 0
        high = len(nums)-1
        ans = -1

        while low <= high : 
            mid = low + ((high - low)//2)

            if nums[mid] <= target : 
                if nums[mid] == target : ans = mid
                low = mid + 1
            
            elif nums[mid] > target : 
                high = mid - 1

        return ans

    def findLeftLimit(self , nums : List[int] , target : int) -> int : 
        low = 0
        high = len(nums)-1
        ans = -1

        while low <= high : 
            mid = low + ((high - low)//2)

            if nums[mid] < target : 
                low = mid + 1
            
            elif nums[mid] >= target : 
                if nums[mid] == target : ans = mid
                high = mid - 1

        return ans