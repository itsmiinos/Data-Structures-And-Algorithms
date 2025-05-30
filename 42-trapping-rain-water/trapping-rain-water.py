class Solution:
    def trap(self, height: List[int]) -> int:
        total_trapped = 0

        
        prefixMaxArray = [-1]*len(height)
        suffixMaxArray = [-1]*len(height)

        prefixMaxArray[0] = height[0]
        suffixMaxArray[len(height)-1] = height[len(height)-1]

        for i in range(1 , len(height)) :
            prefixMaxArray[i] = max(prefixMaxArray[i-1] , height[i])
        
        for i in range(len(height)-2 , -1 , -1) :
            suffixMaxArray[i] = max(suffixMaxArray[i+1] , height[i])
        
        for i in range (len(height)) :
            total_trapped += min(prefixMaxArray[i] , suffixMaxArray[i]) - height[i]
        
        return total_trapped