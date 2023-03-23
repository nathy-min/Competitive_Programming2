class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_val = 0
        
        for i in range(n + 1):
            sum_val += i
        
        sum_nums = sum(nums)
        
        return sum_val - sum_nums