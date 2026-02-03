# Last updated: 2/3/2026, 4:24:11 PM
1class Solution:
2    def maxScore(self, cardPoints: List[int], k: int) -> int:
3        n = len(cardPoints)
4        total = sum(cardPoints)
5
6        if k == n:
7            return total
8
9        window_size = n - k
10        curr_sum = sum(cardPoints[:window_size])
11        min_sum = curr_sum
12
13        left = 0
14        right = window_size
15
16        while right < len(cardPoints) :
17            curr_sum += cardPoints[right]
18            curr_sum -= cardPoints[left]
19            min_sum = min(curr_sum , min_sum)
20            right+=1
21            left+=1
22        
23        return total - min_sum