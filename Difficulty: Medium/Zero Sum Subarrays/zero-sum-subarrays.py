class Solution:
    def findSubarray(self, nums):
        n = len(nums)
        k=0
        map = {}
        map[0] = 1
        ans = 0
        psum = [0] * n
        psum[0] = nums[0]

        for i in range(1, n):
            psum[i] = psum[i - 1] + nums[i]

        for ep in range(n):
            diff = psum[ep] - k
            ans += map.get(diff , 0) #valid starting points with diff as prefix sum
            map[psum[ep]] = map.get(psum[ep] , 0) + 1

        return ans
