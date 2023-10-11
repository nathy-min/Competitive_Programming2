class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        half = ceil(stone_sum / 2)
        def dfs(i, curr_sum):
            if curr_sum >= half or i == len(stones):
                return abs(curr_sum - (stone_sum - curr_sum))
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            dp[(i, curr_sum)] = min(dfs(i + 1, curr_sum), dfs(i + 1, curr_sum + stones[i]))        
            return dp[(i, curr_sum)]
            
        dp = {}
        return dfs(0, 0)