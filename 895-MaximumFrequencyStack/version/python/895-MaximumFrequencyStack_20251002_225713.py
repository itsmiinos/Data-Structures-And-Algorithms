# Last updated: 10/2/2025, 10:57:13 PM
class FreqStack:

    def __init__(self):
        self.hashmap = {}
        self.max_freq = 0
        self.freq_map = {}

    def push(self, val: int) -> None:
        if val in self.freq_map : 
            self.freq_map[val] = self.freq_map.get(val) + 1
        else : 
            self.freq_map[val] = 1
        
        freq = self.freq_map[val]

        if freq in self.hashmap :
            self.hashmap[freq].append(val)
        else : 
            self.max_freq = max(self.max_freq , freq)
            self.hashmap[self.max_freq] = []
            self.hashmap[self.max_freq].append(val)

    def pop(self) -> int:
        popped = None
        if self.max_freq > 0 and len(self.hashmap[self.max_freq]) > 0 :
            popped = self.hashmap[self.max_freq].pop(-1)
            if len(self.hashmap[self.max_freq]) == 0 : 
                del self.hashmap[self.max_freq]
                self.max_freq -=1
        self.freq_map[popped] -=1
        if self.freq_map[popped] == 0 :
            del self.freq_map[popped]
        return popped


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()