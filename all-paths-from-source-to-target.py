class Solution:
    def dfs(self, visited, node):
        if node == self.dest:
            self.paths.append(visited.copy())
        
        
        for val in self.graph[node]:
            visited.append(val)
            self.dfs(visited, val)
            visited.pop()
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        self.graph = graph
        self.dest = len(graph) - 1
        
        self.dfs([0], 0)
        
        return self.paths