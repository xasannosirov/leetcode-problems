class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        for i in ghosts:
            if abs(i[0]-target[0]) + abs(i[1]-target[1]) <= abs(target[0])+abs(target[1]):
                return False
        return True
