class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(n):
            dic[manager[i]].append(i)
        def dfs(i):
            temp = 0
            for num in dic[i]:
                temp = max(temp, dfs(num))    

            return informTime[i] + temp    

        return dfs(headID)    