import sys
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0]*(len(matrix[0]))
        max_rectangle_area = -sys.maxsize

        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) : 
                if matrix[i][j] == '1' : 
                    heights[j] += 1
                else : 
                    heights[j] = 0
        
            nse_on_right = self.nextSmallerElementOnTheRight(heights)
            nse_on_left = self.nextSmallerElementOnTheLeft(heights)

            
            for i in range(len(heights)) :
                nse_on_right_index = nse_on_right[i] - 1
                nse_on_left_index = nse_on_left[i] + 1

                area = heights[i] * (nse_on_right_index - nse_on_left_index + 1)

                max_rectangle_area = max(max_rectangle_area , area)

        return max_rectangle_area

    
    def nextSmallerElementOnTheRight(self, heights : [int]) -> [int] : 
        stack = []
        result = [-1]*len(heights)

        for i in range(len(heights)) : 

            while len(stack) > 0 and heights[i] < stack[-1].val : 
                popped = stack.pop(-1)
                result[popped.index] = i

            stack.append(Pair(heights[i] , i))

        while len(stack) > 0 : 
            popped = stack.pop(-1)
            result[popped.index] = len(heights)

        return result
    
    def nextSmallerElementOnTheLeft(self , heights : [int]) -> [int] : 
        stack = []
        result = [-1]*len(heights)

        for i in range(len(heights)-1 , -1 , -1) : 

            while len(stack) > 0 and heights[i] < stack[-1].val : 
                popped = stack.pop(-1)
                result[popped.index] = i

            stack.append(Pair(heights[i] , i))
        
        while len(stack) > 0 :
            popped = stack.pop(-1)
            result[popped.index] = -1
        
        return result


class Pair : 
    
    def __init__(self , value : int , index : int) :
        self.val = value
        self.index = index