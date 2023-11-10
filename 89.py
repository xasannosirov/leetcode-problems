class Solution:
    def grayCode(self, n: int) -> list[int]:
        res = [0, 1]
        for i in range(2, n+1):
            summand = 2**(i-1)
            res = res+[elem+summand for elem in reversed(res)]
        return res
