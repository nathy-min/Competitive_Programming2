class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        lst = [(0,1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        q = []
        q.append([0, 0, 0])
        weight = {}
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                weight[(i, j)] = float('inf')
        weight[(0, 0)] = 0

        while q:
            mh, r, c = heapq.heappop(q)
            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                return mh

            for a, b in lst:
                nr = a + r
                nc = b + c
                
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]):
                    cm = max(mh, abs(heights[nr][nc] - heights[r][c]))
                    if cm < weight[(nr, nc)]:
                        weight[(nr, nc)] = cm
                        heapq.heappush(q, [cm, nr, nc])

                 
