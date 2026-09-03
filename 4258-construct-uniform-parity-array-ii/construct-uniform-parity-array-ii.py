class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        if nums1[0] % 2 == 0 :
            for i in range(len(nums1)) :
                if nums1[i] % 2 != 0  :
                    return False
        else :
            return True
        
        return True