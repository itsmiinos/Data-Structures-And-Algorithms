class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_container_area = float('-inf')

        while i < j :

            max_container_area = max(max_container_area , min(height[i] , height[j]) * (j-i))

            if height[j] <= height[i] :
                j-=1
            else :
                i+=1
        
        return max_container_area