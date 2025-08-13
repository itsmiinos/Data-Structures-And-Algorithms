# Last updated: 8/13/2025, 8:22:32 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 1 : 
            return [[1]]
        elif numRows == 2 : 
            return [[1] , [1 , 1]]
        
        else : 
            result = [[1] , [1 , 1]]
            for i in range(2 , numRows) :
                result.append([1]*(i+1)) 
                for j in range(i) : 
                    if j!=0 and j!=i : 
                        result[i][j] = result[i-1][j] + result[i-1][j-1]
    
        return result