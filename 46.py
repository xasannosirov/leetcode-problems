from itertools import permutations

class Solution:
    def permute(self, nums):
        thisList = list()
        for i in permutations(nums):
            thisList.append(i)
        thisList = list(map(list, thisList))
        return thisList
