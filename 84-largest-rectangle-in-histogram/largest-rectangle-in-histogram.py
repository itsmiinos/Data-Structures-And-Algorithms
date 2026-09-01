class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_min_stack = [-1] * len(heights)
        right_min_stack = [len(heights)] * len(heights)

        my_stack = []

        for i in range(len(heights)) :
            while len(my_stack) > 0 and my_stack[-1][0] > heights[i] :
                value , index = my_stack.pop(-1)

                right_min_stack[index] = i
            
            my_stack.append([heights[i] , i])
        
        my_stack = []

        for i in range(len(heights)-1 , -1 , -1) :
            while len(my_stack) > 0 and my_stack[-1][0] > heights[i] :
                value , index = my_stack.pop(-1)

                left_min_stack[index] = i
            
            my_stack.append([heights[i] , i])
        
        print(left_min_stack , right_min_stack)
        max_area = float('-inf')
        for i in range(len(heights)) :
            max_distance_on_left = i - left_min_stack[i]
            max_distance_on_right = right_min_stack[i] - i

            area = heights[i] * ((max_distance_on_left + max_distance_on_right)-1)
            print(max_distance_on_left , max_distance_on_right)

            max_area = max(max_area , area)
        
        return max_area