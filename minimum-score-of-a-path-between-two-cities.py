class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        root = [i for i in range(n+ 1)]
        rank = [1 for i in range(n+ 1)]
        min_dist = [float('inf') for i in range(n + 1)]

        def find(a):
            if root[a] == a:
                return a
            root[a] = find(root[a])  
            return root[a]

        def union(a, b, road):
            a = find(a)
            b = find(b)
            if rank[b] > rank[a]:
                a, b = b, a
            
            root[b] = a
            rank[a] += rank[b]
            min_dist[a] = min(road, min_dist[a], min_dist[b])

        for a, b, r in roads:
            union(a, b, r)

        return min_dist[find(1)]