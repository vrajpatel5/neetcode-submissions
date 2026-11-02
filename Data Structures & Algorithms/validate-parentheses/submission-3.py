class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        sets = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for char in s:
            if char in sets:
                if stack and stack[-1] == sets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False