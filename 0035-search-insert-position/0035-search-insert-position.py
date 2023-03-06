class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target :
                return mid
            elif left == right :
                print("hi")
                if nums[left] > target :
                    return left
                else:
                    return left  + 1
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return left
                   