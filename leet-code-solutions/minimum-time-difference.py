class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_lst = []
        for time in timePoints:
            a, b = map(int, time.split(":"))
            min_lst.append(a * 60 + b)

        min_lst.sort()
        min_min = float('inf')
        for i in range(1, len(min_lst)):
            min_min = min(min_min, min_lst[i] - min_lst[i - 1])
        min_min = min(min_min, 24 * 60 - min_lst[-1] + min_lst[0])
        return min_min