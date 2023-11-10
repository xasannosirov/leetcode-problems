class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        h = sorted(heights)
        ind = 0
        for i in range(0, len(heights)):
            if h[i] != heights[i]:
                ind += 1
        return ind
