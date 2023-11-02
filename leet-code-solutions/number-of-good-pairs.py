class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        ans = 0
        for val in hashmap.values():
            ans += (val - 1) * val / 2

        return int(ans)    