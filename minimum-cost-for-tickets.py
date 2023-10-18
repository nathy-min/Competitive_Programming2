class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (len(days) + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for c in range(3):
                if c == 0:
                    dp[i] = min(dp[i], costs[c] + dp[i - 1])
                elif c == 1:
                    if i >= 1:  
                        a = i - 2
                        while a != -1:
                            if days[i - 1] - 7 >= days[a]:
                                break
                            a -= 1     
                        
                        dp[i] = min(dp[i], costs[c] + dp[a + 1])
                else:
                    if i >= 1:  
                        a = i - 2
                        while a != -1:
                            if days[i - 1] - 30 >= days[a]:
                                break
                            a -= 1     
                        
                        dp[i] = min(dp[i], costs[c] + dp[a + 1])

        print(dp)
        return dp[-1]