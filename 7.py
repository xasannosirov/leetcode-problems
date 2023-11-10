class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if str(x)[0] == '-':
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])

        if -2147483648 < res < 2147483647:
            return res
        else:
            return 0
