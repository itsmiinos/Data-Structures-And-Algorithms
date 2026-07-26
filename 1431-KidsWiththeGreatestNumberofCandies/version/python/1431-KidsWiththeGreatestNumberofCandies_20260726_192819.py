# Last updated: 7/26/2026, 7:28:19 PM
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        max_before = float('-inf')
4
5        for i in range(len(candies)) :
6            if candies[i] > max_before :
7                max_before = candies[i]
8        
9        result = []
10        for i in range(len(candies)) :
11            if candies[i] + extraCandies >= max_before : 
12                result.append(True)
13            else :
14                result.append(False)
15
16        return result