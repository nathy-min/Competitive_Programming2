class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            if not temp[nums[i] - 1]:
                temp[nums[i] - 1] = nums[i]
            else:
                res = nums[i]
        
        return res