# Last updated: 7/31/2026, 10:52:22 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3
4        i = m - 1          # Last valid element in nums1
5        j = n - 1          # Last element in nums2
6        k = m + n - 1      # Last position in nums1
7
8        while i >= 0 and j >= 0:
9
10            if nums1[i] > nums2[j]:
11                nums1[k] = nums1[i]
12                i -= 1
13            else:
14                nums1[k] = nums2[j]
15                j -= 1
16
17            k -= 1
18
19        # Copy remaining elements from nums2
20        while j >= 0:
21            nums1[k] = nums2[j]
22            j -= 1
23            k -= 1