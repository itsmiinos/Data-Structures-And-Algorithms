class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        pSum = [[0 for j in range(m)] for i in range(n)]

        for j in range(m) : 
            sum = 0
            for i in range(n) : 
                sum += int(matrix[i][j])
                if matrix[i][j] == '0' : 
                    sum = 0
                pSum[i][j] = sum

        max_area = -float('inf')

        for i in range(n) : 
    
            max_area = max(max_area , self.largestRectangleArea(pSum[i]))
        
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        left_smallest_element = [-1]*len(heights)
        right_smallest_element = [-1]*len(heights)

        left_stack = []
        right_stack = []

        for i in range(len(heights) - 1 , -1 , -1) : 
            while len(left_stack) > 0 and heights[i] < left_stack[-1][0] : 
                popped = left_stack.pop(-1)
                popped_value = popped[0]
                popped_index = popped[1]

                left_smallest_element[popped_index] = i
            
            left_stack.append([heights[i] , i])
        
        while len(left_stack) > 0 : 
            popped = left_stack.pop(-1)
            popped_index = popped[1]

            left_smallest_element[popped_index] = -1
        
        for i in range(len(heights)) : 
            while len(right_stack) > 0 and heights[i] < right_stack[-1][0] : 
                popped = right_stack.pop(-1)
                popped_value = popped[0]
                popped_index = popped[1]

                right_smallest_element[popped_index] = i
            
            right_stack.append([heights[i] , i])
        
        while len(right_stack) > 0 : 
            popped = right_stack.pop(-1)
            popped_index = popped[1]

            right_smallest_element[popped_index] = len(heights)

        max_area = -float('inf')
        for i in range(len(heights)) : 
            area = heights[i] * ((right_smallest_element[i]-1) - (left_smallest_element[i]+1) + 1)
            max_area = max(area , max_area)
        
        return max_area