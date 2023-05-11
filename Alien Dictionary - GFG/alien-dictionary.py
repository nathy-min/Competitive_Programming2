#User function Template for python3
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
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends