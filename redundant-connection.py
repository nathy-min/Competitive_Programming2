class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = [i for i in range(len(edges) + 1)]
        rank = [1 for _ in range(len(edges) + 1)]
        ans = []

        def find(x):
            if rep[x] == x:
                return x
            rep[x] = find(rep[x])
            return rep[x]

        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            ans = []
            
            if xrep == yrep:
                ans = [x, y]
            if rank[yrep] > rank[xrep]:
                xrep, yrep = yrep, xrep

            rep[yrep] = xrep
            rank[xrep] += rank[yrep]

            return ans

        for a, b in edges:
            if not ans:
                ans = union(a, b)

        return ans