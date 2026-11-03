class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        c2o = {
            "}" : "{", 
            ")" : "(", 
            "]" : "["
            }

        for char in s:
            if char in c2o:
                if stack and stack[-1] == c2o[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
