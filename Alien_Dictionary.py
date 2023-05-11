from collections import defaultdict
from collections import deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        graph = defaultdict(list)
        indgree = defaultdict(int)
        for i in range(N):
            for ch in alien_dict[i]:
                indgree[ch] = 0
                
        for i in range(N - 1):
            a = alien_dict[i]
            b = alien_dict[i + 1]
            ptr = 0
            for j in range(min(len(a), len(b))):
                if a[j] == b[j]:
                    continue
                graph[a[j]].append(b[j])            
                indgree[b[j]] += 1
                break
        q = deque([key for key in indgree if indgree[key] == 0])
        order = []
        
        while q:
            ch = q.popleft()
            order.append(ch)
            
            for let in graph[ch]:
                indgree[let] -= 1
                if indgree[let] == 0:
                    q.append(let)
        return order