# Last updated: 1/15/2026, 11:03:14 PM
1class MyHashMap:
2
3    def __init__(self):
4        self.arr = [None]* (10**6 + 1)
5
6    def put(self, key: int, value: int) -> None:
7        self.arr[key] = value
8
9    def get(self, key: int) -> int:
10        if self.arr[key] is not None :
11            return self.arr[key]
12        
13        return -1
14
15    def remove(self, key: int) -> None:
16        self.arr[key] = None
17
18
19# Your MyHashMap object will be instantiated and called as such:
20# obj = MyHashMap()
21# obj.put(key,value)
22# param_2 = obj.get(key)
23# obj.remove(key)