class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        res = list()
        row = len(grid)
        col = len(grid[0])
        for i in grid:
            for j in i:
                res.append(j)
        k %= len(res)
        while k:
            res.insert(0,res.pop())
            k-=1
        result = list()
        p = 0
        for i in range(row):
            roww = list()
            for j in range(col):
                roww.append(res[p])
                p+=1
            result.append(roww)
        return result
