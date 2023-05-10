class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        inbound = [0 for _ in range(n)]
        ans = [set() for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            inbound[edge[1]] += 1

        q = deque()
        for i in range(n):
            if inbound[i] == 0:
                q.append(i)

        while  q:
            node = q.popleft()
            for neb in graph[node]:
              ans[neb].add(node)
              ans[neb].update(ans[node])
              inbound[neb] -= 1
              if inbound[neb] == 0:
                q.append(neb)
                
        ans = [sorted(list(s)) for s in ans]        
        return ans