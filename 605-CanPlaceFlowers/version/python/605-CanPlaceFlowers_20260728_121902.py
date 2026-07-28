# Last updated: 7/28/2026, 12:19:02 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        for i in range(len(flowerbed)):
4
5            if flowerbed[i] == 1:
6                continue
7
8            if i != 0 and flowerbed[i - 1] == 1:
9                continue
10
11            if i != len(flowerbed) - 1 and flowerbed[i + 1] == 1:
12                continue
13
14            flowerbed[i] = 1
15            n -= 1
16
17        return n <= 0