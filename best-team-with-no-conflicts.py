class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()
        dp = [pairs[i][0] for i in range(len(pairs))]

        for i in range(len(pairs)):
            s, a = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if a >= age:
                   
                    
                    dp[i] = max(dp[i], s + dp[j])
        return max(dp)