class Solution:
    def getXor(self, cur_val, idx):
        if idx == len(self.nums):
            return
        
        for i in range(idx, len(self.nums)):
            temp = cur_val
           
            cur_val |= self.nums[i]
            self.dic[cur_val] += 1
            self.getXor(cur_val, i + 1)
            
            cur_val = temp
            
            
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.nums = nums
        self.dic = defaultdict(int)
        
        self.getXor(0, 0)
    
        return self.dic[max(self.dic)]