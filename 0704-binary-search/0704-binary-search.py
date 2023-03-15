class Solution:
    def find(self, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2
        if self.nums[mid] == self.target:
            return mid
        elif self.nums[mid] < self.target:
            return self.find(mid + 1, high)
        else:
            return self.find(low, mid - 1)
    
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        
        return self.find(0, len(nums) - 1)