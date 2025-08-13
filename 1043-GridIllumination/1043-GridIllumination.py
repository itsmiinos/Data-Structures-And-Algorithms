# Last updated: 8/13/2025, 8:18:01 PM
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row_map = {}
        col_map = {}
        first_diag_map = {} #first diagonal array map (row - col)
        second_diag_map = {} #second diagonal array map (row + col)
        converted = {} #converted array map

        for u,v in lamps : 
            row_map[u] = row_map.get(u,0) + 1
            col_map[v] = col_map.get(v,0) + 1
            first_diag_map[u-v] = first_diag_map.get(u-v , 0) + 1
            second_diag_map[u+v] = second_diag_map.get(u+v , 0) + 1
            converted[u*n + v] = converted.get(u*n + v , 0) + 1

        direction_array = [[0,0] , [-1,-1] , [-1,0] , [-1,1] , [0,1] , [1,1] , [1,0] , [1,-1] , [0 , -1]]
        ans = []
        for x,y in queries : 

            if (row_map.get(x, 0) > 0 or
                col_map.get(y, 0) > 0 or
                first_diag_map.get(x - y, 0) > 0 or
                second_diag_map.get(x + y, 0) > 0):
                ans.append(1)
            else:
                ans.append(0)

            for u , v in direction_array : 
                x1 = u+x
                y1 = v+y

                if x1>=0 and y1>=0 and x1<n and y1<n and converted.get(x1*n+y1,0) > 0 : 
                    times = converted[x1*n+y1]
                    row_map[x1] = row_map.get(x1,0) - times
                    col_map[y1] = col_map.get(y1,0) - times
                    first_diag_map[x1-y1] = first_diag_map.get(x1-y1,0) - times
                    second_diag_map[x1+y1] = second_diag_map.get(x1+y1,0) - times
                    del converted[x1*n+y1]
            
        return ans