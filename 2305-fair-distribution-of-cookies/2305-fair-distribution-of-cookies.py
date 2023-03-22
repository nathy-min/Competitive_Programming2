class Solution:
    def distribute(self, visited, idx):
        if idx == len(self.cookies):
            self.min_unfa = min(self.min_unfa, max(visited))
            return
        if max(visited)>=self.min_unfa:
            return
        for i in range(self.k):
            visited[i]+=self.cookies[idx]
            self.distribute(visited , idx + 1)
            visited[i]-=self.cookies[idx]
            if visited[i] == 0:
                    break

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.cookies = cookies
        self.k = k
        visited = [0 for _ in range(k)]
        self.min_unfa = float("inf")
        self.distribute(visited, 0)
        
        return self.min_unfa