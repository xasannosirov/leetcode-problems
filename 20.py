class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { ")":"(", "]":'[', "}":"{" }
        if s[0] in brackets:
            return False
        stack = [s[0]]
        for i in range(1,len(s)):
            if s[i] in brackets:
                if not stack:
                    return False
                check = stack.pop()
                if check != brackets[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return len(stack) == 0
