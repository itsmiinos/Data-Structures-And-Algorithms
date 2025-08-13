# Last updated: 8/13/2025, 8:22:59 PM
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        histogram = [ [0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        for j in range(len(matrix[0])) :
            sum = 0 
            for i in range(len(matrix)) : 
                sum += int(matrix[i][j])
                if int(matrix[i][j]) == 0 : 
                    sum = 0

                histogram[i][j] = sum
        max_area = float('-inf')
        for h in histogram :
            max_area = max(max_area , self.calculateMaxArea(h))
        
        return max_area
    
    def calculateMaxArea(self , arr : list[int]) -> int :

        nsel = [-1]*len(arr)
        nser = [len(arr)]*len(arr)

        self.findNSEL(arr , nsel)
        self.findNSER(arr , nser)

        area = float('-inf')

        for i in range(len(arr)) : 
            smaller_on_left = nsel[i] + 1
            smaller_on_right = nser[i] - 1

            area = max(area , arr[i] * (smaller_on_right - smaller_on_left + 1))
        
        return area
            
    def findNSEL(self , arr : list[int] , nsel : list[int]) -> None : 
        stack = []

        for i in range(len(arr)-1 , -1 , -1) : 
            while len(stack) > 0 and stack[-1][0] > arr[i] : 
                popped = stack.pop(-1)
                index = popped[1]

                nsel[index] = i
            
            stack.append([arr[i] , i])
        
    def findNSER(self , arr : list[int] , nser : list[int]) -> None : 
        stack = []

        for i in range(len(arr)) : 
            while len(stack) > 0 and stack[-1][0] > arr[i] : 
                popped = stack.pop(-1)
                index = popped[1]

                nser[index] = i
        
            stack.append([arr[i] , i])