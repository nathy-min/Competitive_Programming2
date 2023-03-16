class Solution:
    def combination(self, visited, idx):
        if sum(visited) == self.target:
            self.ans.append(list(visited))
            return
        if sum(visited) > self.target:
            return
        
        for i in range(idx, len(self.candidates)):
            visited.append(self.candidates[i])
            self.combination(visited, i)
            visited.pop()
        
           
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.target = target
        self.candidates = candidates
        self.combination([], 0)
        return self.ans