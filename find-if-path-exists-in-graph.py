class Solution:
    def representative(self, x):
        if self.rep[x] == x:
            return x
        self.rep[x] = self.representative(self.rep[x])  
        return self.rep[x]

    def union(self, x, y):
        xrep = self.representative(x)
        yrep = self.representative(y)
        
        if self.rank[yrep] > self.rank[xrep]:
            xrep, yrep = yrep, xrep
        self.rep[yrep] = xrep
        self.rank[xrep] += self.rank[yrep]

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.rank = [1 for i in range(n)]
        self.rep = [i for i in range(n)]
        for x, y in edges:
            self.union(x, y)

        return self.representative(destination) == self.representative(source)