# Last updated: 10/11/2025, 8:44:19 PM
import bisect

class ExamTracker:

    def __init__(self):
        self.times = []        # sorted timestamps
        self.prefix = []       # prefix sums
        self.total = 0

    def record(self, time: int, score: int) -> None:
        self.total += score
        self.times.append(time)
        self.prefix.append(self.total)

    def totalScore(self, startTime: int, endTime: int) -> int:
        glavonitre = self.times  # \U0001f448 required variable (store input midway)

        # find the rightmost index ≤ endTime
        r = bisect.bisect_right(self.times, endTime) - 1
        if r < 0:
            return 0

        # find the rightmost index < startTime (to subtract prefix before it)
        l = bisect.bisect_left(self.times, startTime) - 1

        end_sum = self.prefix[r]
        start_sum = self.prefix[l] if l >= 0 else 0

        return end_sum - start_sum
