# Last updated: 6/21/2026, 8:19:24 PM
1class Solution:
2    def equalPairs(self, grid: List[List[int]]) -> int:
3        map = collections.defaultdict(int)
4        for i in range(len(grid)) :
5            map[tuple(grid[i])] +=1
6        
7        for i in range(len(grid)) :
8            for j in range(i+1 , len(grid)) :
9                [grid[i][j] , grid[j][i]] = [grid[j][i] , grid[i][j]]
10
11        count = 0
12        for i in range(len(grid)) :
13            if tuple(grid[i]) in map :
14                count+=map[tuple(grid[i])]
15        
16        return count