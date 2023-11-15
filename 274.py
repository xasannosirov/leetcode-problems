class Solution:
    def hIndex(self, citations: list[int]) -> int:
        length = len(citations)
        citations.sort()
        for i in range(length):
            if citations[i] >= length - i:
                return length - i
        return 0
