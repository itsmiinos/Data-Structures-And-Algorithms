# Last updated: 6/4/2026, 10:01:53 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        i = 0
7        j = 0
8        ans = []
9
10        while i < m and j < n :
11            if nums1[i] <= nums2[j] :
12                ans.append(nums1[i])
13                i+=1
14            else :
15                ans.append(nums2[j])
16                j+=1
17        
18        while i < m : 
19            ans.append(nums1[i])
20            i+=1
21        
22        while j < n : 
23            ans.append(nums2[j])
24            j+=1
25        
26        for i in range(len(ans)) :
27            nums1[i] = ans[i]