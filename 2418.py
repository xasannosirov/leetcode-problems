class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        people = dict()
        for i in range(len(names)):
            people[heights[i]] = names[i]
        people = sorted(people.items(), key=lambda x: x[0], reverse=True)
        res = list()
        for i in people:
            res.append(i[1])
        return res
