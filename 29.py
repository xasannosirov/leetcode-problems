class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend < 0 and divisor == -1 and dividend != -1:
            return (dividend * -1)-1
        return int(dividend/divisor)
