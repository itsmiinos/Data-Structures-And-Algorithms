# Last updated: 12/29/2025, 12:20:52 AM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key = lambda x : x[0])
4        L = intervals[0]
5        i = 1
6        count = 0
7
8        while i < len(intervals) :
9            current_start = intervals[i][0]
10            current_end = intervals[i][1]
11
12            last_start = L[0]
13            last_end = L[1]
14
15            if current_start >= last_end :
16                L = intervals[i]
17                
18            elif current_end >= last_end :
19                count+=1
20            elif current_end < last_end :
21                L = intervals[i]
22                count+=1
23            
24            
25            i+=1
26        return count
27        