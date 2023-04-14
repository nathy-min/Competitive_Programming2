class Solution:
    def dfs(self, node):
        count = 1
        temp = [0, 0]
        for num in self.graph[node]:
            prev_count, prev_char = self.dfs(num)
            if prev_char != self.character[node]:
                if prev_count > temp[0] or prev_count > temp[1]:
                    if prev_count > temp[0]:
                        temp[0] = prev_count
                temp.sort()       
        count += max(temp)
        self.max_path = max(self.max_path, 1 + sum(temp))

        return count, self.character[node]

    def longestPath(self, parent: List[int], s: str) -> int:
        if len(parent) == 1:
            return 1
        self.graph = defaultdict(list)
        self.character = {}  
        self.max_path = 0  
        
        for i in range(len(parent)):
            self.graph[parent[i]].append(i)
            self.character[i] = s[i]
        
        self.dfs(0)

        return self.max_path