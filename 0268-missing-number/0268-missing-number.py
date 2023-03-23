class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        first = 0
        
        while first < len(nums):
            if nums[first] == -1 or nums[first] == first:
                first += 1
            else:
                val = nums[first]
                nums[first] , nums[val] = nums[val] , nums[first]
        
        for idx , val in enumerate(nums):
            if val == -1:
                return idx
            