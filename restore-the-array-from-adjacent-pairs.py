class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        indgree = defaultdict(int)
        graph = defaultdict(list)

        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            indgree[a] += 1
            indgree[b] += 1

        q = deque()
        for key in indgree:
            if indgree[key] == 1:
                q.append(key)
                indgree[key] -= 1
                break    

        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for val in graph[node]:
                if indgree[val] == 2:
                    q.append(val)
                    indgree[val] -= 2
        
        for key in indgree:
            if indgree[key] == 1:
                order.append(key)
                break

        return order