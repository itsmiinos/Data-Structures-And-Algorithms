# Last updated: 8/13/2025, 8:23:02 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        nser = [len(heights)]*len(heights)
        nsel = [-1]*len(heights)

        self.findNSER(heights , nser)
        self.findNSEL(heights , nsel)

        max_rectangle = float('-inf')

        for i in range(len(heights)) : 
            smaller_on_right = nser[i] - 1
            smaller_on_left = nsel[i] + 1

            max_rectangle = max(max_rectangle , heights[i] * (smaller_on_right - smaller_on_left + 1))
        
        return max_rectangle
    

    def findNSER(self , heights : list[int] , nser : list[int]) -> None : 

        stack = []
        for i in range(len(heights)) : 
            while len(stack) > 0 and stack[-1][0] > heights[i] : 
                popped = stack.pop(-1)
                index = popped[1]

                nser[index] = i

            stack.append([heights[i] , i])
        
        print(nser)
        
    def findNSEL(self , heights : list[int] , nsel : list[int]) -> None : 
        stack = []
        for i in range(len(heights)-1 , -1 , -1) : 
            while len(stack) > 0 and stack[-1][0] > heights[i] : 
                popped = stack.pop(-1)
                index = popped[1]

                nsel[index] = i

            stack.append([heights[i] , i])
        
        print(nsel)