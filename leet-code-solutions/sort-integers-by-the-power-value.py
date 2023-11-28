class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        dp = {}
        def power(n):
            if n == 1:
                return 0
            if n in dp:
                return dp[n]
            if not n % 2:
                dp[n] = 1 + power(n // 2)
            else:
                dp[n] = 1 + power(n * 3 + 1)            
            return dp[n]

        for num in range(lo, hi + 1):
            p_num = power(num)
            res.append((p_num, num))

        res.sort()
        return res[k - 1][1]            