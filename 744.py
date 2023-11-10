class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        find = -1
        for i in letters:
            if ord(i) - find > ord(target) and target != i:
                find = ord(i)
        
        if find == -1:
            return letters[0]
        return chr(find)
