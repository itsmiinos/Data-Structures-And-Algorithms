import random
class RandomizedCollection:

    def __init__(self):
        self.my_map = {}
        self.temp_storage = []

    def insert(self, val: int) -> bool:
        self.temp_storage.append(val)
        last_index = len(self.temp_storage)-1
        if val in self.my_map : 
            self.my_map[val].append(last_index)
            return False
        else : 
            self.my_map[val] = [last_index]
            return True

    def remove(self, val: int) -> bool:
        if val not in self.my_map or not self.my_map[val]:
            return False

        # Index of val to be removed
        remove_index = self.my_map[val].pop()
        last_index = len(self.temp_storage) - 1
        last_val = self.temp_storage[last_index]

        # Swap if not removing last element
        if remove_index != last_index:
            # Move last_val to remove_index
            self.temp_storage[remove_index] = last_val

            # Update last_val's index in map
            self.my_map[last_val].remove(last_index)
            self.my_map[last_val].append(remove_index)

        # Remove last element
        self.temp_storage.pop()

        # Clean up if no more val entries
        if not self.my_map[val]:
            del self.my_map[val]

        return True
        

    def getRandom(self) -> int:
        random_number = random.randint(0 , len(self.temp_storage)-1)
        return self.temp_storage[random_number]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()