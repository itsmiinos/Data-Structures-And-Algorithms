class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [0]*len(nums1)
        max_diff = -1
        my_map = collections.defaultdict(int)
        for i in range(len(nums1)) :
            diff[i] = abs(nums1[i] - nums2[i])
            my_map[diff[i]] +=1
            max_diff = max(max_diff , diff[i])
        
        k = k1+k2
        while k > 0 and max_diff > 0 :
            val = my_map[max_diff]
            if k > val :
                k = k - val
                del my_map[max_diff]
                max_diff -=1
                my_map[max_diff] += val
            else :
                diff = val - k
                k=0
                my_map[max_diff] = diff
                my_map[max_diff - 1] += val - diff
                break 
        
        total_diff = 0
        for key in my_map.keys() :
            if my_map[key] != 0 :
                total_diff += (key ** 2) * my_map[key] 
        
        return total_diff
        