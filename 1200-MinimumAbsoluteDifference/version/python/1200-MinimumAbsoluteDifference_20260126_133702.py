# Last updated: 1/26/2026, 1:37:02 PM
1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        arr.sort()
4        abs_diff = float('inf')
5        for i in range(1 , len(arr)) :
6            abs_diff = min(abs_diff , abs(arr[i] - arr[i-1]))
7        
8        result = []
9        for i in range(1 , len(arr)) :
10            if abs(arr[i] - arr[i-1]) == abs_diff :
11                result.append([arr[i-1] , arr[i]])
12        
13        return result