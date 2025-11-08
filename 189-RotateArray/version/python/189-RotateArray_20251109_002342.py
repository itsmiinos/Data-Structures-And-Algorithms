# Last updated: 11/9/2025, 12:23:42 AM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.rotateArray(0 , len(nums)-1 , nums)
        self.rotateArray(0 , k-1 , nums)
        self.rotateArray(k , len(nums)-1 , nums)

    def rotateArray(self , i : int , j : int , nums : list) -> None : 

        while i <= j : 
            [nums[i] , nums[j]] = [nums[j] , nums[i]]
            i+=1
            j-=1
        