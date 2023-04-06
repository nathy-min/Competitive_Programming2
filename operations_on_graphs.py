from collections import defaultdict
def addEdge(u, v):
    global dic
    dic[u].append(v)
    dic[v].append(u)

def vertex(u):
    global dic
    if not dic[u]:
        print()
    else:
        print(*dic[u])
    
no_v = int(input())
no_ops = int(input())
dic = defaultdict(list)

for i in range(no_ops):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        addEdge(lst[1], lst[2])
    else:
        vertex(lst[1])
    
