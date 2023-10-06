class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        weights = [float('-inf') for _ in range(n)]
        weights[start_node] = 1
        n = len(edges)
        for i in range(n):
            a, b = edges[i]
            c = succProb[i]
            graph[a].append((b, c))
            graph[b].append((a, c))

        heap = [[1, start_node]]
        visited = set()
        while heap:
            w, v = heapq.heappop(heap)
            if v in visited:
                continue
            for node, weight in graph[v]:
                if weights[node] < weights[v] * weight:
                    weights[node] = weights[v] * weight
                    heapq.heappush(heap, [-(weights[v] * weight), node])

        if weights[end_node] == float('-inf'):
            return 0
        return weights[end_node]