# Last updated: 1/6/2026, 9:57:23 PM
1class Solution:
2    def colorTheGrid(self, m: int, n: int) -> int:
3        self.states = []
4        self.generateStates(0 , m , "" , "")
5        self.modulo = (10 ** 9) + 7
6        result = 0
7        self.dp = [[-1 for _ in range(n+1)] for _ in range(len(self.states)+1)]
8        for i in range(len(self.states)) :
9            result += self.solve(n-1 , i) % self.modulo
10        
11        return result % self.modulo
12    
13    def solve(self , n : int , prevState : int) -> int :
14        if n == 0 : 
15            return 1
16
17        if self.dp[prevState][n] != -1 : 
18            return self.dp[prevState][n]
19
20        result = 0
21        last = self.states[prevState]
22
23        for i in range(len(self.states)) :
24            if i == prevState : 
25                continue
26            
27            curr = self.states[i]
28            conflict = False
29            for j in range(len(last)) :
30                if last[j] == curr[j] :
31                    conflict = True
32                    break
33            
34            if conflict == False :
35                result += self.solve(n-1 , i) % self.modulo
36        
37        self.dp[prevState][n] = result % self.modulo
38        return self.dp[prevState][n]
39    
40    def generateStates(self , l : int , m : int , prevChar : str , currState : str) -> None :
41        if l == m :
42            self.states.append(currState)
43            return
44        
45        for ch in ['r' , 'g' , 'b'] :
46            if ch == prevChar :
47                continue
48            
49            self.generateStates(l+1 , m , ch , currState + ch)
50        
51