class Solution:
    def computeGCD(self, x, y):
        if x > y:
            small = y
        else:
            small = x
        for i in range(1, small + 1):
            if((x % i == 0) and (y % i == 0)):
                gcd = i

        return gcd

    def smallestEvenMultiple(self, n: int) -> int:
        return 2*n//self.computeGCD(2,n)
