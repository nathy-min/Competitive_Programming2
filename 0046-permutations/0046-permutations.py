class Solution:
    def find(self, visited):
        if len(visited) == len(self.nums):
            self.ans.append(list(visited))
            return
        
        for idx, val in enumerate(self.nums):
            if self.used & (1 << idx) == 0:
                visited.append(val)
                self.used |= (1 << idx)
                self.find(visited)
                visited.pop()
                self.used ^= (1 << idx)
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.ans = []
        self.used  = 0
        self.find([])
        
        return self.ans