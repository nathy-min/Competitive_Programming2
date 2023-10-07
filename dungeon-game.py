class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[float('-inf') for _ in range(m)] for _ in range(n)]
        dp[n - 1][m - 1] = min(dungeon[n - 1][m - 1], 0)

        for i in range(m - 2, -1, - 1):
            temp = dungeon[n - 1][i] + dp[n - 1][i + 1]
            dp[n - 1][i] = min(temp, 0)

        for i in range(n - 2, -1, -1):
            temp = dungeon[i][m - 1] + dp[i + 1][m - 1]    
            dp[i][m - 1] = min(temp, 0)

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                temp = max(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = min(0, temp + dungeon[i][j])

        return abs(dp[0][0]) + 1 if dp[0][0] < 0 else 1