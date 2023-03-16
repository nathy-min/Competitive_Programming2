class Solution:
    def combination(self, visited, idx):
        if idx == len(self.candidates):
            return
        if sum(visited) == self.target:
            self.ans.append(list(visited))
            return
        if sum(visited) > self.target:
            return
        
        
        visited.append(self.candidates[idx])
        self.combination(visited, idx)
        
        visited.pop()
        self.combination(visited, idx + 1)
        
           
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.target = target
        self.candidates = candidates
        self.combination([], 0)
        return self.ans