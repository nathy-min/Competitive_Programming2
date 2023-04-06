from collections import defaultdict

no_v = int(input())

for i in range(no_v):
    lst = list(map(int, input().split()))
    count = lst.count(1)
    adj_elements = []
    
    for j in range(no_v):
        if lst[j]:
            adj_elements.append(j + 1)
    
    print(count, *adj_elements)
    
    
