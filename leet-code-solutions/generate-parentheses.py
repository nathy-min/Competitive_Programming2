class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(i, j, s):
            if i == n and j == n:
                self.ans.append(s)
                return

            if i < n :
                if i == j:
                    dfs(i + 1, j, s + '(')
                if i > j:
                    dfs(i + 1, j, s + '(')
                    dfs(i, j + 1, s + ')')

            elif j < n:
                dfs(i, j + 1, s + ')')

        self.ans = []
        dfs(0, 0, "")
        return self.ans