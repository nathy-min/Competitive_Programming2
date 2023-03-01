class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(left,right):
            if left == right:
                return nums[left]
            if left > right:
                return 0
            
            ch1 = nums[left] + min(winner(left + 2, right),winner(left + 1, right - 1) )
            ch2 = nums[right] + min(winner(left , right - 2),winner(left + 1, right - 1) )
            
            return max(ch1, ch2)
        return 2 * winner(0, len(nums) - 1) >= sum(nums)