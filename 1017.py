class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        s = str()
        while n != 0:
            temp = n % -2
            n //= -2
            if temp < 0:
                temp += 2
                n += 1
            s = str(temp) + s
        return s
