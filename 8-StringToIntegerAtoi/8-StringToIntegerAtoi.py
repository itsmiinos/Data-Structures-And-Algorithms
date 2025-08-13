# Last updated: 8/13/2025, 8:24:36 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)
        sign = 1

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Recursive parsing of digits
        def helper(i: int, num: int) -> int:
            if i >= n or not s[i].isdigit():
                return num

            digit = int(s[i])
            # Handle overflow
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else -INT_MIN

            return helper(i + 1, num * 10 + digit)

        result = helper(i, 0) * sign
        return min(max(result, INT_MIN), INT_MAX)
