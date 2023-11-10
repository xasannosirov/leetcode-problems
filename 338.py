class Solution:
    def decimal_to_binary(self, num:int)->str:
        res = str()
        while num >= 2:
            res += str(num % 2)
            num //= 2
        res += str(num)
        return res[::-1]

    def countBits(self, n: int) -> list[int]:
        i = 0
        res = list()
        while i <= n:
            x = self.decimal_to_binary(i)
            res.append(sum(list(map(int, x))))
            i+=1
        return res
