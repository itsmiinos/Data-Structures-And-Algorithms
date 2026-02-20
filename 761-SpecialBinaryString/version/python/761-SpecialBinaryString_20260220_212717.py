# Last updated: 2/20/2026, 9:27:17 PM
1class Solution:
2    def makeLargestSpecial(self, s: str) -> str:
3        count = 0
4        i = 0
5        res = []
6        
7        for j in range(len(s)):
8            # Track balance: +1 for '1', -1 for '0'
9            count += 1 if s[j] == '1' else -1
10            
11            # Found a balanced chunk when count returns to 0
12            if count == 0:
13                # Recursively maximize inner part, wrap with 1...0
14                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
15                i = j + 1  # Move to next potential chunk
16        
17        # Sort chunks in descending order for largest arrangement
18        res.sort(reverse=True)
19        return ''.join(res)