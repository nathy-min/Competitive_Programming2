class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}
        seen = set()
        for a, b in zip(s, t):
            if a not in dic:
                if b in seen:
                    return False
                dic[a] = b
                seen.add(b)    
            elif dic[a] != b:
                return False

        return True        