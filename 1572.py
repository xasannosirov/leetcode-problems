class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        l = 0
        r = len(mat)-1
        summa=0
        
        for i in range(len(mat)):
            if l == r:
                summa+=mat[i][l]
            else:
                summa+=mat[i][l] + mat[i][r]
            l+=1
            r-=1
        return summa
