class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        weights = {}
        for i in range(n):
            weights[i] = float('inf')
        weights[src] = 0    

        for path in flights:
            graph[path[0]].append((path[1], path[2]))

        heap = [[0, src, 0]]       
        visited = set()
        ans = float('inf')

        while heap:
            s, v, w = heapq.heappop(heap)
            if v == dst:
                ans  = min(ans, w) 

            if s == k:
                for path in graph[v]:
                    if path[0] == dst:
                        ans = min(ans, w + path[1])
                continue        
            if (s, v) in visited :
                continue        
            visited.add((s, v))

            for node, weight in graph[v]:
                temp = weight + w
                if s < k:
                    heapq.heappush(heap, [s + 1, node, temp])

        if ans == float('inf'):
            return -1 
        return ans