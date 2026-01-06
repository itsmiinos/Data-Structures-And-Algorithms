# Last updated: 1/6/2026, 9:01:57 PM
1class Solution:
2    def numOfWays(self, n: int) -> int:
3        self.modulo = (10 ** 9) + 7
4        self.states = ["rgr","rgb","rbg","rbr","grg","grb","gbg","gbr","bgr","bgb","brb","brg"]
5        result = 0
6        self.dp = [[-1 for _ in range(12)] for _ in range(n+1)]
7        for i in range(len(self.states)) :
8            result += (self.solve(n-1 , i) % self.modulo)
9        
10        return result % self.modulo
11
12    
13    def solve(self , n : int , prev : int) -> int :
14
15        if n == 0 :
16            return 1
17        
18        if self.dp[n][prev] != -1:
19            return self.dp[n][prev]
20
21        last = self.states[prev]
22        result = 0
23        for i in range(len(self.states)) :
24            if i == prev : 
25                continue
26            
27            conflict = False
28            for j in range(len(last)) :
29                if last[j] == self.states[i][j] :
30                    conflict = True
31                    break
32            
33            if conflict == False :
34                result += (self.solve(n-1 , i) % self.modulo)
35        
36        self.dp[n][prev] = result % self.modulo
37
38        return self.dp[n][prev]
39        
40