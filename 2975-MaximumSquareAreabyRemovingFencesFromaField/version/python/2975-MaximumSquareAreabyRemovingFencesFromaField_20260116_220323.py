# Last updated: 1/16/2026, 10:03:23 PM
1class Solution:
2    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
3        hFences.extend([1, m])
4        vFences.extend([1, n])
5
6        stt = set()
7        ans = 0
8
9        for i in range(len(hFences)):
10            for j in range(i+1, len(hFences)):
11                stt.add(abs(hFences[j]-hFences[i]))
12        
13        for i in range(len(vFences)):
14            for j in range(i+1, len(vFences)):
15                val = abs(vFences[j]-vFences[i])
16                if val in stt:
17                    ans = max(ans, val)
18        
19        if ans == 0:
20            return -1
21        return (ans*ans)%(10**9+7)