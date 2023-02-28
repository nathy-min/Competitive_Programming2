class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        pref_sum=0
        d={0:1}

        for num in nums:
            pref_sum = pref_sum + num

            if pref_sum-k in d:
                ans = ans + d[pref_sum-k]

            if pref_sum not in d:
                d[pref_sum] = 1
            else:
                d[pref_sum] = d[pref_sum]+1

        return ans        