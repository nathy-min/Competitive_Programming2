class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        min_year = logs[0][0]
        max_year = logs[-1][1]
        n = max_year - min_year
        count = [0] * n

        for i in range(n):
            for start , end in logs:
                if i + min_year >= start and i + min_year < end:
                    count[i] += 1

        max_count = max(count)
        for i in range(n):
            if count[i] == max_count:
                return min_year + i            