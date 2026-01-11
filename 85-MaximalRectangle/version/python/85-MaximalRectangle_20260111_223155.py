# Last updated: 1/11/2026, 10:31:55 PM
1class Solution:
2    def maximalRectangle(self, matrix: List[List[str]]) -> int:
3        heights = [0]*len(matrix[0])
4        max_rectangle = 0
5
6        for i in range(len(matrix)) :
7            for j in range(len(matrix[0])) : 
8                if matrix[i][j] == "1" : 
9                    heights[j] += 1
10                else :
11                    heights[j] = 0
12        
13            max_rectangle = max(max_rectangle , self.solve(heights))
14        
15        return max_rectangle
16    
17    def solve(self , heights : list) -> int :
18
19        nsel = self.next_smallest_element_on_left(heights)
20        nser = self.next_smallest_element_on_right(heights)
21
22        max_area = 0
23
24        for i in range(len(heights)) :
25            right_small = nser[i] - 1
26            left_small = nsel[i] + 1
27
28            distance = right_small - left_small + 1
29
30            max_area = max(max_area , heights[i] * distance)
31
32        
33        return max_area
34    
35    def next_smallest_element_on_left(self , arr : list) -> list :
36
37        nsel = [-1] * len(arr)
38        stack = []
39
40        for i in range(len(arr)-1 , -1 , -1) :
41            while stack and stack[-1][0] > arr[i] :
42                res = stack.pop(-1)
43                index = res[1]
44
45                nsel[index] = i
46            
47            stack.append([arr[i] , i])
48        
49        return nsel
50
51    def next_smallest_element_on_right(self , arr : list) -> list :
52
53        nser = [len(arr)]*len(arr)
54        stack = []
55        
56        for i in range(len(arr)) :
57            while stack and stack[-1][0] > arr[i] :
58                res = stack.pop(-1)
59                index = res[1]
60
61                nser[index] = i
62            
63            stack.append([arr[i] , i])
64
65        return nser