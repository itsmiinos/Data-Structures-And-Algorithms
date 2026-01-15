# Last updated: 1/15/2026, 9:37:53 PM
1class MyHashSet:
2
3    def __init__(self):
4        self.my_set = []
5
6    def add(self, key: int) -> None:
7        if self.contains(key) == False :
8            self.my_set.append(key)
9
10    def remove(self, key: int) -> None:
11        if self.contains(key) == True :
12            j = 0
13            for i in range(len(self.my_set)) :
14                if self.my_set[i] == key :
15                    j = i
16                    break
17            
18            while j < len(self.my_set)-1 :
19                self.my_set[j] , self.my_set[j+1] = self.my_set[j+1] , self.my_set[j]
20                j+=1
21        
22            self.my_set.pop(-1)
23
24    def contains(self, key: int) -> bool:
25        for i in range(len(self.my_set)) :
26            if self.my_set[i] == key :
27                return True
28        
29        return False
30
31
32# Your MyHashSet object will be instantiated and called as such:
33# obj = MyHashSet()
34# obj.add(key)
35# obj.remove(key)
36# param_3 = obj.contains(key)