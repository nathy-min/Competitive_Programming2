class Solution:
    def dfs(self, node):
        if self.colors[node] == 1:
            return False
        self.colors[node] = 1    
        for neb in self.graph[node]:
            if self.colors[neb] == 2:
                continue
            if not self.dfs(neb):
                return False

        self.colors[node] = 2
        self.ans.append(node)
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.graph = graph
        self.colors = [0 for _ in range(len(graph))]
        self.ans = []
        for i in range(len(graph)):
            if not self.colors[i]:
                if self.dfs(i):
                    pass

        return sorted(self.ans)