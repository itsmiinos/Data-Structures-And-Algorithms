# Last updated: 1/15/2026, 9:23:21 PM
1class Solution:
2    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
3        hBars.sort()
4        vBars.sort()
5
6        max_con_hBars = 1
7        max_con_vBars = 1
8
9        
10        count = 1
11        for i in range(1 , len(hBars)) :
12            if hBars[i]-1 == hBars[i-1] :
13                count+=1
14            else :
15                count = 1
16            max_con_hBars = max(count , max_con_hBars)
17
18
19        count = 1
20        for i in range(1 , len(vBars)) :
21            if vBars[i]-1 == vBars[i-1] :
22                count+=1
23            else :
24                count = 1
25            
26            max_con_vBars = max(count , max_con_vBars)
27        
28        # print(max_con_hBars , max_con_vBars)
29        
30        return (min(max_con_hBars , max_con_vBars) + 1) * (min(max_con_hBars , max_con_vBars) + 1) 
31