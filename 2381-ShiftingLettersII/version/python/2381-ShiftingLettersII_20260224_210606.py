# Last updated: 2/24/2026, 9:06:06 PM
1class Solution:
2    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
3        diff = [0]*len(s)
4        
5        for shift in shifts :
6            l , r , d = shift
7            if d == 0 :
8                diff[l] -=1
9                if r + 1 < len(diff) :
10                    diff[r+1] +=1
11            else :
12                diff[l] +=1
13                if r + 1 < len(diff) :
14                    diff[r+1] -=1
15        
16
17        res = []
18        curr_shift = 0
19
20        for i in range(len(diff)):
21            curr_shift += diff[i]
22            original = ord(s[i]) - ord('a')
23            new_char = (original + curr_shift) % 26
24            res.append(chr(new_char + ord('a')))
25
26        return "".join(res)