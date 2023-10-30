class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = collections.defaultdict(list)
        for i, equ in enumerate(equations):
            a, b = equ
            dic[a].append([b, values[i]])
            dic[b].append([a, 1 / values[i]])

        ans = []
        for que in queries:
            a, b = que
            if a not in dic or b not in dic:
                ans.append( -1)
                continue

            q, visited = deque(), set()
            q.append([a, 1])

            flag = 1
            while q:
                n, w = q.popleft()
                if n == b:
                    ans.append( w)
                    flag = 0
                    break
                visited.add(n)

                for nei, weight in dic[n]:
                    if nei not in visited:
                        q.append([nei, w * weight])

            if flag:
                ans.append( -1)               
        
        return ans    