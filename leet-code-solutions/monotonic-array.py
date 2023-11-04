class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if temp < 0:
                    return False
            elif nums[i] < nums[i - 1]:
                if temp > 0:
                    return False
            if not temp:
                temp = nums[i] - nums[i - 1]     

        return True                   
