# Last updated: 2/3/2026, 10:53:29 PM
1class Solution:
2    def calPoints(self, operations: List[str]) -> int:
3        score = []
4        for op in operations :
5            if op == "+" :
6                second = score[-1]
7                first = score[-2]
8                score.append(int(first) + int(second))
9            elif op == "C" :
10                score.pop(-1)
11            elif op == "D" :
12                score.append(int(score[-1]) * 2)
13            else :
14                score.append(int(op))
15            print(score)
16        
17        return sum(score)