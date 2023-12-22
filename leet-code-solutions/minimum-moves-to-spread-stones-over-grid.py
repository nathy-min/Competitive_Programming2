class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        left = {}
        zeros = []
        for i in range(3):
            for j in range(3):
                if not grid[i][j]:
                    zeros.append((i, j))
                if grid[i][j] > 1:
                    left[(i, j)] = grid[i][j] - 1

        def dfs(i):
            if i == len(zeros):
                return 0
            ans = float('inf')
            for key in left.keys():
                if left[key]:
                    temp = (abs(zeros[i][0] - key[0]) + abs(zeros[i][1] - key[1]))
                    left[key] -= 1
                    ans = min(ans, temp + dfs(i + 1))
                    left[key] += 1  
            return ans

        return dfs(0)                                                