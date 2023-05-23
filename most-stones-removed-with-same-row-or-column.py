class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(a):
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if rank[pb] > rank[pa]:
                pa, pb = pb, pa 

            parent[pb] = pa
            rank[pa] += rank[pb]

        n = len(stones)
        parent = {}
        rank = {}
        for point in stones:
            parent[tuple(point)] = tuple(point)
            rank[tuple(point)] = 1
        

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(tuple(stones[i]), tuple(stones[j]))
        for key in parent:
            find(key)
        s = set()
        for key in parent:
            s.add(parent[key])

        return n - len(s)