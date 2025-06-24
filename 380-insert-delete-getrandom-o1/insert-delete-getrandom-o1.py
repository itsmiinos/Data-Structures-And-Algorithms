import random
class RandomizedSet:

    def __init__(self):
        self.my_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.my_set : 
            self.my_set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.my_set : 
            self.my_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        temp_storage = []
        for key in self.my_set : 
            temp_storage.append(key)
        
        max = len(temp_storage)-1

        random_number = random.randint(0 , max)
        return temp_storage[random_number]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()