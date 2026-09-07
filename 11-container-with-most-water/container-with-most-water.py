class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1

        max_container_size = float('-inf')
        while i < j :
            container_size = min(height[i] , height[j]) * (j-i)
            max_container_size = max(max_container_size , container_size)

            if height[i] > height[j] :
                j-=1
            
            else :
                i+=1

        return max_container_size