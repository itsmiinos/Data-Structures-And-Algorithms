# Last updated: 1/30/2026, 10:42:00 PM
1class Solution:
2    def minimumCost(self, source, target, original, changed, cost):
3        INF = 10**30
4        id = {}
5        lens = set()
6        sz = 0
7
8        dist = [[INF]*201 for _ in range(201)]
9
10        for s, t, c in zip(original, changed, cost):
11            if s not in id:
12                id[s] = sz
13                lens.add(len(s))
14                sz += 1
15            if t not in id:
16                id[t] = sz
17                sz += 1
18            dist[id[s]][id[t]] = min(dist[id[s]][id[t]], c)
19
20        for i in range(sz):
21            dist[i][i] = 0
22
23        for k in range(sz):
24            for i in range(sz):
25                if dist[i][k] < INF:
26                    for j in range(sz):
27                        if dist[k][j] < INF:
28                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
29
30        n = len(source)
31        dp = [INF] * (n + 1)
32        dp[0] = 0
33
34        for i in range(n):
35            if dp[i] == INF:
36                continue
37
38            if source[i] == target[i]:
39                dp[i + 1] = min(dp[i + 1], dp[i])
40
41            for L in lens:
42                if i + L > n:
43                    continue
44                s = source[i:i+L]
45                t = target[i:i+L]
46                if s in id and t in id:
47                    dp[i + L] = min(dp[i + L], dp[i] + dist[id[s]][id[t]])
48
49        return -1 if dp[n] == INF else dp[n]