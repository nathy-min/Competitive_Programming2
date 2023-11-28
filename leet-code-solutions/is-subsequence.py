class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) * len(t) == 0:
            if len(s):
                return False
            else:
                return True

        ptr = 0
        n = len(t)
        for i in range(n):
            if ptr < len(s) and t[i] == s[ptr]:
                ptr += 1

        return ptr == len(s)                        
