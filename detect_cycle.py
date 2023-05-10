from typing import List
from collections import deque
class Solution:
    def dfs(self, node, prev):
        if self.color[node] == 1:
            return False
        self.color[node] = 1
        
        for neb in self.graph[node]:
            if self.color[neb] == 2:
                continue
            if neb != prev and not self.dfs(neb, node):
                return False

        self.color[node] = 2
        return True    
            
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		self.color = [0 for _ in range(V)]
		self.graph = adj
		ans = True
		for i in range(V):
		    if not self.color[i] and ans:
		        ans = ans and self.dfs(i, -1)
		
		return 0 if ans else 1        
		        

