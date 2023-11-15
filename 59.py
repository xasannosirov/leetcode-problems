class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = list()
        for _ in range(n):
            row = list()
            for _ in range(n):
                row.append(0)
            result.append(row)
        son = n
        i, c, m = 0, 1, 0
        while i <= son // 2:
            j = m
            while j < son - m:
                result[i][j] = c
                c+=1
                j+=1
            j = m+1
            while j < son-m-1:
                result[j][son-m-1] = c
                c+=1
                j+=1
            j = son-m-1
            while c <= son*son and j >= m:
                result[son-i-1][j] = c
                c+=1
                j-=1
            j = son-m-2
            while j > m:
                result[j][i] = c
                c+=1
                j-=1
            i+=1
            m+=1

        return result
