class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        occurrences = []
        visited = [False]*len(nums)

        for i in range(len(nums)) : 
            if nums[i] == key : 
                occurrences.append(i)

        ans = []
        for i in range(len(occurrences)) : 
            j=0
            while j < len(nums) :
                if abs(j - occurrences[i]) <= k and visited[j] == False: 
                    ans.append(j)
                    visited[j] = True
                j+=1
        
        return ans