class Solution:
    def dfs(self, bomb):
        if bomb in self.visited:
            return 0
        count = 1
        self.visited.add(bomb) 

        for bom in self.graph[bomb]:
            count += self.dfs(bom)

        return count        
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        self.visited = set()
        max_boms = 1

        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i][0], bombs[i][1], bombs[i][2]
            for j in range(i + 1, len(bombs)):
                x2, y2, r2 = bombs[j][0], bombs[j][1], bombs[j][2]
                x = x2 - x1
                y = y2 - y1
                dist = sqrt(x**2 + y**2)

                if dist <= r1:
                    self.graph[i].append(j)
                if dist <= r2:
                    self.graph[j].append(i)

        for i in range(len(bombs)):
            
            max_boms = max(max_boms,self.dfs(i))
            self.visited = set()
                
        print(self.graph)
        return max_boms        