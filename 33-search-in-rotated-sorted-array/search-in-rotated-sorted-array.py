class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        result = -1

        while low <= high : 
            
            mid = low + ((high - low) // 2)

            if nums[mid] > nums[high] : #we are in the left side of the array
                
                if target >= nums[low] and target <= nums[mid] : 
                    result = self.doBinarySearch(low , mid , nums , target)
                    return result
                
                else : 
                    low = mid + 1
            
            else : 

                if target >= nums[mid] and target <= nums[high] : 
                    result = self.doBinarySearch(mid , high , nums , target)
                    return result
                
                else : 
                    high = mid - 1
            
        
        return result
    
    def doBinarySearch(self , low : int , high : int , nums : [int] , target : int) -> int : 

        while low<=high : 

            mid = low + ((high - low) // 2)

            if nums[mid] == target : 
                return mid
            
            elif nums[mid] < target : 
                low = mid + 1
            
            else :
                high = mid - 1
        
        return -1