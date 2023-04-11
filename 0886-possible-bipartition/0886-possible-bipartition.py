class Solution:
    def dfs(self, num, color):
        if self.color_arr[num - 1] != -1:
            if self.color_arr[num - 1] != color:
                return False
            else:
                return True
         
        self.color_arr[num - 1] = color
        color = 1 - color
        self.visited.add(num)
        
        ans = True
        for n in self.dic[num]:
            ans = (ans and self.dfs(n, color))
        
        return ans
        
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.color_arr = [-1 for _ in range(n)]
        self.visited = set()
        self.dic = defaultdict(list)
        res = True
        
        for val in dislikes:
            self.dic[val[0]].append(val[1])
            self.dic[val[1]].append(val[0])
        
        keys = list(self.dic.keys())
        for num in keys:
            if num not in self.visited:
                res = res and self.dfs(num, 0)
                
        return res        
        
        