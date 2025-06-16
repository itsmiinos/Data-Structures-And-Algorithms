class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0:
            sign = sign * (-1)
            dividend = -dividend  # fix: take absolute
        if divisor < 0:
            sign = sign * (-1)
            divisor = -divisor  # fix: take absolute

        temp = 0
        q = 0

        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp = temp + (divisor << i)
                q = q + (1 << i)

        q = q * sign  # apply sign after computing q

        if q >= 2**31:  # fix: clamp to 2^31 - 1
            return 2**31 - 1
        if q < -2**31:
            return -2**31

        return q