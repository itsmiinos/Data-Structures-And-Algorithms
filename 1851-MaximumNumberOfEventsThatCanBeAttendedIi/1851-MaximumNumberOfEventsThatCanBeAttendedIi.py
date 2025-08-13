# Last updated: 8/13/2025, 8:16:57 PM
from bisect import bisect_left

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Step 1: Sort events by start time
        events.sort()
        n = len(events)
        
        # Step 2: Precompute next available event index for each event
        start_times = [event[0] for event in events]
        next_event = [0] * n
        for i in range(n):
            target = events[i][1] + 1
            next_event[i] = bisect_left(start_times, target)
        
        # Step 3: Initialize DP table
        # dp[i][j] = max value considering events[i:] and selecting j events
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Step 4: Fill DP table from bottom up
        for i in range(n - 1, -1, -1):         # Loop over events from end to start
            for j in range(1, k + 1):          # Loop over number of picks (1 to k)
                # Case 1: Skip current event
                skip = dp[i + 1][j]
                # Case 2: Attend current event
                next_i = next_event[i]
                take = events[i][2] + dp[next_i][j - 1]
                # Take the best of both
                dp[i][j] = max(skip, take)

        # Final answer is max value we can obtain from index 0 and k picks
        return dp[0][k]
