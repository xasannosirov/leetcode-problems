class Solution:   
    def checkCube(self, board, row, col):
        cube = list()
        for i in range(row, row+3):
            cube.extend(board[i][col:col+3])
        s = ''.join(cube).replace('.', '')
        if len(set(s)) != len(s):
            del board
            return False
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not self.checkCube(board, i, j):
                    del board
                    return False

        for i in board:
            s = ''.join(i).replace('.', '')
            if len(set(s)) != len(s):
                del board
                return False
            
        for i in zip(*board):
            s = ''.join(i).replace('.', '')
            if len(set(s)) != len(s):
                del board
                return False
        
        return True
