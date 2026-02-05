# Last updated: 2/5/2026, 9:53:31 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.min_value = None
6
7    def push(self, val: int) -> None:
8        if len(self.stack) == 0 :
9            self.min_value = val
10            self.stack.append(0)
11        else:
12            diff = val - self.min_value
13            self.stack.append(diff)
14            if diff < 0:
15                self.min_value = val
16
17    def pop(self) -> None:
18        if len(self.stack) == 0 :
19            return None
20        else :
21            val = self.stack.pop(-1)
22            if val < 0 :
23                self.min_value = self.min_value - val
24            return self.min_value + val
25
26    def top(self) -> int:
27        
28        if not self.stack:
29            return None
30        diff = self.stack[-1]
31        if diff >= 0:
32            return self.min_value + diff
33        else:
34            return self.min_value       
35
36    def getMin(self) -> int:
37        if len(self.stack) == 0 :
38            return None
39        else :
40            return self.min_value
41
42
43# Your MinStack object will be instantiated and called as such:
44# obj = MinStack()
45# obj.push(val)
46# obj.pop()
47# param_3 = obj.top()
48# param_4 = obj.getMin()