class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s) # a, j, r
        t = sorted(t) # a, j. m

        if len(s) != len(t):
            return False
        
        i = 0

        for char in s:
            if char == t[i]:
                i += 1
            else:
                return False
        return True