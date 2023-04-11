class Solution:
    def dfs(self, num):
        if num in self.visited:
            return
        
        self.visited.add(num)
        
        for i in range(len(self.isconnected[num])):
            if self.isconnected[num][i]:
                self.dfs(i)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        self.isconnected = isConnected
        no_province = 0
        
        for i in range(len(isConnected)):
            if i not in self.visited:
                no_province += 1
                self.dfs(i)
        
        return no_province