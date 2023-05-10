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
		        


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends