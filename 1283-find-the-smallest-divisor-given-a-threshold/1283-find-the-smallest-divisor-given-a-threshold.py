class Solution:
    def isLess(self, mid, nums, threshold):
        
        for i in range(len(nums)):
            nums[i] = ceil(nums[i] / mid)
       
        new_sum = sum(nums)
        if new_sum <= threshold:
            return True
        else:
            return False
            
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        best_val = 0
        
        while left <= right:
            mid = (right + left) // 2
            print(mid)
            if self.isLess(mid, nums.copy(), threshold):
                best_val = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best_val