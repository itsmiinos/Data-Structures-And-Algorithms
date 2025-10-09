# Last updated: 10/9/2025, 11:36:38 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2) : 
            nums1 , nums2 = nums2 , nums1
        
        low = 0
        high = len(nums1)

        total = (len(nums1) + len(nums2))
        half = (total + 1) // 2

        while low <= high : 

            mid = low + (high - low) // 2
            mid2 = half - mid

            l1 = nums1[mid-1] if mid > 0 else float('-inf')
            l2 = nums2[mid2-1] if  mid2 > 0 else float('-inf')

            r1 = nums1[mid] if mid < len(nums1) else float('inf')
            r2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if l2 <= r1 and l1<= r2 : 
                if total % 2 == 0 :
                    return (max(l1 , l2) + min(r1 , r2)) / 2.0
                else :
                    return max(l1 , l2)
            
            elif l1 > r2 : 
                high = mid - 1
            
            elif l2 > r1 : 
                low = mid + 1
        
        return 0
                
