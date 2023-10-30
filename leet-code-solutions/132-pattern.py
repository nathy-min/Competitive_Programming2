class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curr_min = nums[0]

        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            stack.append([num, curr_min])
            curr_min = min(curr_min, num)

        return False                                              