# Last updated: 8/13/2025, 8:14:43 PM
from collections import defaultdict
import heapq

class Solution:
    def maxSumDistinctTriplet(self, x, y):
        max_y_for_x = dict()

        # Track max y for each distinct x
        for xi, yi in zip(x, y):
            if xi not in max_y_for_x:
                max_y_for_x[xi] = yi
            else:
                max_y_for_x[xi] = max(max_y_for_x[xi], yi)

        # Not enough distinct x values
        if len(max_y_for_x) < 3:
            return -1

        # Get top 3 largest y-values from distinct x
        top_y = heapq.nlargest(3, max_y_for_x.values())
        return sum(top_y)