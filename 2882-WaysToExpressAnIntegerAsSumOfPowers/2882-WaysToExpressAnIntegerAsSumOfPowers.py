# Last updated: 8/13/2025, 8:15:39 PM
M = int(1e9 + 7)

class Solution:
    def __init__(self):
        self.memo = [[-1] * 301 for _ in range(301)]

    def func(self, n, sum_, x, num):
        if sum_ == n:
            return 1
        tmp = pow(num, x)

        if sum_ + tmp > n:
            return 0

        if self.memo[num][sum_] != -1:  # added
            return self.memo[num][sum_]

        take = self.func(n, sum_ + tmp, x, num + 1)
        not_take = self.func(n, sum_, x, num + 1)

        self.memo[num][sum_] = (take + not_take) % M  # updated
        return self.memo[num][sum_]

    def numberOfWays(self, n, x):
        return self.func(n, 0, x, 1)