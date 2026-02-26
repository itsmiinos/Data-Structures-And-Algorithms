# Last updated: 2/26/2026, 9:17:41 PM
1class Solution:
2    def numSteps(self, s: str) -> int:
3        steps = 0
4        carry = 0
5
6        # process from right to left, skipping MSB
7        for i in range(len(s) - 1, 0, -1):
8            bit = int(s[i])
9
10            if bit + carry == 1:
11                # odd → add 1
12                steps += 2
13                carry = 1
14            else:
15                # even → divide by 2
16                steps += 1
17
18        # final carry may add one extra step
19        return steps + carry