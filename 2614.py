class Solution:
    def isPrime(self, i):
        if i <= 2:
            return True if i == 2 else False
        
        if i % 2 == 0:
            return False
        
        j = 3
        while j*j <= i:
            if i % j == 0:
                return False
            j+=2

        return True

    def diagonalPrime(self, nums: list[list[int]]) -> int:
        res = list()
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i == j or  i+j == len(nums)-1:
                    res.append(nums[i][j])
        
        res2 = list()
        for i in res:
            if self.isPrime(i):
                res2.append(i)

        if len(res2):
            return max(res2)

        return 0
