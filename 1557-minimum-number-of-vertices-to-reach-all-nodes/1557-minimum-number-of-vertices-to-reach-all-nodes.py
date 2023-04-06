class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = set()
        parents = []
        
        for i in range(len(edges)):
            visited.add(edges[i][1])
        
        for i in range(n):
            if i not in visited:
                parents.append(i)
        
        return parents                
                
        