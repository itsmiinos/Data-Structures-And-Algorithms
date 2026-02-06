# Last updated: 2/6/2026, 7:28:38 PM
1class FreqStack:
2
3    def __init__(self):
4        self.lookup = collections.defaultdict(list)
5        self.max_freq = 0
6        self.freq = collections.defaultdict(int)
7
8    def push(self, val: int) -> None:
9        if len(self.lookup) == 0 :
10            self.max_freq = 1
11            self.lookup[self.max_freq].append(val)
12            self.freq[val] +=1
13        else :
14            if val in self.freq :
15                self.freq[val] +=1
16                f = self.freq[val]
17                if f in self.lookup :
18                    self.lookup[f].append(val)
19                else :
20                    self.max_freq = f
21                    self.lookup[f].append(val)
22            else :
23                self.freq[val] = 1
24                self.lookup[1].append(val)
25
26    def pop(self) -> int:
27        val = self.lookup[self.max_freq].pop(-1)
28        self.freq[val] -=1
29        if self.freq[val] == 0 :
30            del self.freq[val]
31        if len(self.lookup[self.max_freq]) == 0 :
32            del self.lookup[self.max_freq]
33            self.max_freq -=1
34        
35        return val
36
37
38# Your FreqStack object will be instantiated and called as such:
39# obj = FreqStack()
40# obj.push(val)
41# param_2 = obj.pop()