# Last updated: 6/21/2026, 8:45:08 PM
1class Solution:
2    def removeStars(self, s: str) -> str:
3        my_stack = []
4        for i in range(len(s)) :
5            if s[i] == '*' :
6                my_stack.pop(-1)
7            else :
8                my_stack.append(s[i])
9        
10        return "".join(my_stack)