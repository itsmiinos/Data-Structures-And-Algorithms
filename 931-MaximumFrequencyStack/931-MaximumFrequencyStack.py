# Last updated: 8/13/2025, 8:18:28 PM
import sys
class FreqStack:

    def __init__(self):
        self.map_stack = {}
        self.freq_map = {}
        self.max_freq = -sys.maxsize

    def push(self, val: int) -> None:
        if val in self.freq_map : 
            self.freq_map[val] = self.freq_map.get(val) + 1
            freq = self.freq_map[val]
            self.max_freq = max(freq , self.max_freq)
            
            if freq in self.map_stack : 
                self.map_stack[freq].append(val)

            else : 
                self.map_stack[freq] = []
                self.map_stack[freq].append(val)


        else : 
            freq = 1
            self.freq_map[val] = freq
            self.max_freq = max(freq , self.max_freq)

            if freq in self.map_stack : 
                self.map_stack[freq].append(val)

            else : 
                self.map_stack[freq] = []
                self.map_stack[freq].append(val)

    def pop(self) -> int:
        
        popped = self.map_stack[self.max_freq].pop(-1)

        if len(self.map_stack[self.max_freq]) == 0 : 
            del self.map_stack[self.max_freq]
            self.max_freq -=1

        self.freq_map[popped] = self.freq_map.get(popped) - 1

        return popped
    


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()