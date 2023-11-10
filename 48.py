class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        for i in range(1, len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
