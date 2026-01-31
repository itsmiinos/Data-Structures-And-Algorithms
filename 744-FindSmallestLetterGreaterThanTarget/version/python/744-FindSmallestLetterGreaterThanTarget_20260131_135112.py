# Last updated: 1/31/2026, 1:51:12 PM
1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        max_diff = float('inf')
4        greater_element = -1
5
6        for i in range(len(letters)) :
7            if abs(ord(letters[i]) - ord(target)) < max_diff and ord(letters[i]) > ord(target):
8                max_diff = abs(ord(letters[i]) - ord(target))
9                greater_element = i
10            
11        
12        return letters[greater_element] if greater_element != -1 else letters[0]