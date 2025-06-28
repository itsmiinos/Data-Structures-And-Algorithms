import sys
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nse_on_right = self.nextSmallerElementOnRight(heights)
        nse_on_left = self.nextSmallerElementOnLeft(heights)

        max_area = -sys.maxsize

        for i in range(len(heights)) : 
            
            nse_on_right_index = nse_on_right[i] - 1
            nse_on_left_index = nse_on_left[i] + 1

            area = heights[i] * (nse_on_right_index - nse_on_left_index + 1)
            max_area = max(area , max_area)  

        return max_area

    def nextSmallerElementOnRight(self , heights : [int]) -> [int] : 
        stack = []
        result= [-1]*len(heights)

        for i in range(len(heights)) :
            while len(stack) > 0 and heights[i] < stack[-1].val : 
                popped = stack.pop(-1)
                result[popped.index] = i
            
            stack.append(Pair(heights[i] , i))

        while(len(stack)) > 0 : 
            popped = stack.pop(-1)
            result[popped.index] = len(heights)
        
        return result

    def nextSmallerElementOnLeft(self, heights : [int]) -> [int] : 
        stack = []
        result = [-1]*len(heights)

        for i in range(len(heights)-1 , -1, -1) : 
            while len(stack) > 0 and heights[i] < stack[-1].val : 
                popped = stack.pop(-1)
                result[popped.index] = i

            stack.append(Pair(heights[i] , i))
        
        while(len(stack)) > 0 :
            popped = stack.pop(-1)
            result[popped.index] = -1

        return result


class Pair : 
    def __init__(self , value , index) : 
        self.val = value
        self.index = index