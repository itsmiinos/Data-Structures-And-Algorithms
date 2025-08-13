# Last updated: 8/13/2025, 8:23:47 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transposeMatrix(matrix)
        
        for mat in matrix : 
            self.reverseArray(mat)

    def transposeMatrix(self , matrix : list[list[int]]) -> None : 
        n = len(matrix)

        for i in range(n) : 
            for j in range(i+1,n) : 
                if i!=j : 
                    [matrix[i][j] , matrix[j][i]] = [matrix[j][i] , matrix[i][j]]

    def reverseArray(self , arr : [int]) -> None : 
        i = 0 
        j = len(arr)-1 

        while i<=j : 
            [arr[i] , arr[j]] = [arr[j] , arr[i]]
            i+=1
            j-=1

        