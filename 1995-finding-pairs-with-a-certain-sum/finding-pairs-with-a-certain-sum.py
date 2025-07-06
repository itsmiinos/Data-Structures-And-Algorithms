class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.my_map = {}
        self.nums1 = [None]*len(nums1)
        self.nums2 = [None]*len(nums2)

        for i in range(len(nums1)) : 
            self.nums1[i] = nums1[i]
        
        for i in range(len(nums2)) : 
            self.nums2[i] = nums2[i]
            self.my_map[nums2[i]] = self.my_map.get(nums2[i] , 0) + 1
        

    def add(self, index: int, val: int) -> None:
        original_value = self.nums2[index]
        changed_value = original_value + val
        self.nums2[index] = changed_value

        self.my_map[original_value] = self.my_map.get(original_value) - 1

        if self.my_map[original_value] == 0 : 
            del self.my_map[original_value]

        self.my_map[changed_value] = self.my_map.get(changed_value , 0) + 1

    def count(self, tot: int) -> int:
        total_count = 0
        for i in range(len(self.nums1)) : 
            diff = tot - self.nums1[i]
            if diff in self.my_map : 
                count = self.my_map[diff]
                total_count += count

        return total_count

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)