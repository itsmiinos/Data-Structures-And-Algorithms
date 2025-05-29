class NumArray:

    def __init__(self, nums: List[int]):
        self.array = []
        self.array = nums
        self.prefixSum = [-1]*len(self.array)
        self.prefixSum[0] = self.array[0]

        for i in range(1 , len(self.array)) :
            self.prefixSum[i] = self.prefixSum[i-1] + self.array[i]
        
        print(self.prefixSum)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 :
            return self.prefixSum[right] - self.prefixSum[left-1]
        else :
            return self.prefixSum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)