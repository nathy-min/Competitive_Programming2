class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        while l < r:
            m = (l + r + 1) // 2
            if citations[m] > n - m: r = m - 1
            else: l = m
        return n - l - (citations[l] < n - l)