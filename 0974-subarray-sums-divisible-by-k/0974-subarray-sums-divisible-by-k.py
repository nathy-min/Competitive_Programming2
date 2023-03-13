class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        multiples = 0
        remainder_count = defaultdict(int)
        
        remainder_count[0] = 1
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            multiples += remainder_count[prefix_sum%k]
            remainder_count[prefix_sum%k] += 1
        
        return multiples