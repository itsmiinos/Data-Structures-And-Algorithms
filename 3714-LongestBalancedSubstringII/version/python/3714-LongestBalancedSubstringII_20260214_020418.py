# Last updated: 2/14/2026, 2:04:18 AM
1class Solution:
2    def mono(self, s: str) -> int:
3        if not s:
4            return 0
5        cnt = 1
6        ans = 1
7        for i in range(1, len(s)):
8            if s[i] == s[i - 1]:
9                cnt += 1
10            else:
11                cnt = 1
12            ans = max(ans, cnt)
13        return ans
14
15    def duo(self, s: str, c1: str, c2: str) -> int:
16        pos: Dict[int, int] = {0: -1}
17        ans = 0
18        delta = 0
19        for i, ch in enumerate(s):
20            if ch != c1 and ch != c2:
21                pos.clear()
22                pos[0] = i
23                delta = 0
24                continue
25
26            if ch == c1:
27                delta += 1
28            else:
29                delta -= 1
30
31            if delta in pos:
32                ans = max(ans, i - pos[delta])
33            else:
34                pos[delta] = i
35
36        return ans
37
38    def trio(self, s: str) -> int:
39        cnt0 = cnt1 = cnt2 = 0  
40        pos: Dict[Tuple[int, int], int] = {(0, 0): -1}
41        ans = 0
42        for i, ch in enumerate(s):
43            if ch == 'a':
44                cnt0 += 1
45            elif ch == 'b':
46                cnt1 += 1
47            else:  
48                cnt2 += 1
49
50            key = (cnt1 - cnt0, cnt2 - cnt0)
51
52            if key in pos:
53                ans = max(ans, i - pos[key])
54            else:
55                pos[key] = i
56
57        return ans
58
59    def longestBalanced(self, s: str) -> int:
60        return max(
61            self.mono(s),
62            self.duo(s, 'a', 'b'),
63            self.duo(s, 'a', 'c'),
64            self.duo(s, 'b', 'c'),
65            self.trio(s),
66        )