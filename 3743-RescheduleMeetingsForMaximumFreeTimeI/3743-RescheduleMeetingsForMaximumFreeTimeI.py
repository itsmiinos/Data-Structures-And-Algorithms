# Last updated: 8/13/2025, 8:14:56 PM
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [startTime[0]]  # before first meeting
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])

        window = sum(gaps[:k+1])
        ans = window

        for i in range(k+1, len(gaps)):
            window += gaps[i] - gaps[i - (k+1)]
            ans = max(ans, window)

        return ans