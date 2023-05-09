class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indgree = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)
            indgree[a] += 1

        q = deque()
        for i in range(numCourses):
            if indgree[i] == 0:
                q.append(i)   
        ans = []
        while q:
            course = q.popleft()
            ans.append(course)
            for c in graph[course]:
                indgree[c] -=  1
                if indgree[c] == 0:
                    q.append(c)         

        return len(ans) == numCourses