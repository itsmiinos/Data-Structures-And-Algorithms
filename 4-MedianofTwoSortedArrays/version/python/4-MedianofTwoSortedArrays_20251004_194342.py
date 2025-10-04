# Last updated: 10/4/2025, 7:43:42 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total_elements = len(nums1) + len(nums2)
        min_elements = 0
        max_elements = len(nums1)

        low = min_elements
        high = max_elements

        half = (total_elements + 1) // 2
        
        while low <= high : 

            mid = low + ((high - low) // 2)
            mid2 = half - mid

            l1 = nums1[mid-1] if mid > 0 else float('-inf')
            l2 = nums2[mid2-1] if mid2 > 0 else float('-inf')
            r1 = nums1[mid] if mid < len(nums1) else float('inf')
            r2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if l1 <= r2 and l2 <= r1 : 
                if total_elements % 2 == 0 : 
                    return (max(l1 , l2) + min (r1 , r2)) / 2.0
                else : 
                    return max(l1 , l2)
            
            elif l2 > r1 : 
                low = mid + 1

            elif l1 > r2 : 
                high = mid - 1
        
        return 0
        
        
