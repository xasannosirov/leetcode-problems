class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        check = min(a,b)
        i = 1
        summa = 0
        while i <= check:
            if a % i == 0 and b % i == 0:
                summa += 1
            i+=1
        return summa
