# Last updated: 1/1/2026, 12:53:20 AM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        res = []
4        i = 0
5
6        
7        while i < len(intervals) and intervals[i][1] < newInterval[0] :
8            res.append(intervals[i])
9            i+=1
10
11        new_start = newInterval[0]
12        new_end = newInterval[1]
13
14        while i < len(intervals) and intervals[i][0] <= newInterval[1] :
15            new_start = min(intervals[i][0] , new_start)
16            new_end = max(intervals[i][1] , new_end)
17            i+=1
18
19        res.append([new_start , new_end])
20
21        while i < len(intervals) :
22            res.append(intervals[i])
23            i+=1
24        
25        return res