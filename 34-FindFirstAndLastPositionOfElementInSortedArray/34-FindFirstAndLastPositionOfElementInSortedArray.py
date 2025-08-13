# Last updated: 8/13/2025, 8:24:03 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_position = self.first_position_finder(nums , target)
        second_position = self.second_position_finder(nums , target)
        return [first_position , second_position]

    
    def first_position_finder(self , nums : list[int] , target : int) -> int : 
        ans = -1
        low = 0
        high = len(nums)-1

        while low <= high : 
            mid = low + (high - low) // 2

            if nums[mid] == target : 
                ans = mid
                high = mid - 1
            
            elif nums[mid] > target : 
                high = mid - 1
            
            else : 
                low = mid + 1
        
        return ans
    
    def second_position_finder(self , nums : list[int] , target : int) -> int : 
        ans = -1
        low = 0
        high = len(nums)-1

        while low <= high : 
            mid = low + (high - low) // 2

            if nums[mid] == target : 
                ans = mid
                low = mid + 1
            
            elif nums[mid] < target : 
                low = mid + 1

            else : 
                high = mid - 1
        
        return ans