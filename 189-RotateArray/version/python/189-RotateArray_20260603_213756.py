# Last updated: 6/3/2026, 9:37:56 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        k = k % len(nums)
7        self.reverseArray(0 , len(nums)-1 , nums)
8        self.reverseArray(0 , k-1 , nums)
9        self.reverseArray(k , len(nums)-1 , nums)
10        
11    
12    def reverseArray(self , i : int , j : int , nums : list) -> None :
13        while i < j : 
14            nums[i] , nums[j] = nums[j] , nums[i]
15            i+=1
16            j-=1
17
18