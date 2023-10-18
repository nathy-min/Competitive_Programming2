class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        for i in range(len(s1)):
            parent[s1[i]] = s1[i]
            parent[s2[i]] = s2[i]

        def find(ch):
            if ch not in parent:
                return ch
            res = ch
            while res != parent[res]:
                res = parent[res]

            return res

        def union(ch1, ch2):
            p1, p2 = find(ch1), find(ch2)
            if ord(p1) < ord(p2):
                parent[p2] = p1
            else:
                parent[p1] = p2 

        for a, b in zip(s1, s2):
            union(a, b)

        ans = ''
        for ch in baseStr:
            ans += find(ch)

        return ans