# Last updated: 2/25/2026, 2:07:11 PM
1import heapq
2class Solution:
3    def sortByBits(self, arr: List[int]) -> List[int]:
4        return sorted( arr , key = lambda a : (a.bit_count() , a))
5