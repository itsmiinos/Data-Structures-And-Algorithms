# Last updated: 8/13/2025, 8:18:37 PM
import random
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.my_map = {}
        self.valid_number_count = n - len(blacklist)
        self.blacklist = set(blacklist)

        for i in range(len(blacklist)) : 
            self.my_map[blacklist[i]] = -1

        self.index = n-1
        for b in self.blacklist : 
            if b < self.valid_number_count : 
                while self.index in self.my_map : 
                    self.index-=1
                self.my_map[b] = self.index
                self.index-=1


    def pick(self) -> int:
        random_number = random.randint(0 , self.valid_number_count-1)
        if random_number in self.my_map : 
            return self.my_map[random_number]
        return random_number


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()