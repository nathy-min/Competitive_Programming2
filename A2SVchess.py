
def mergesort(left, right, arr):
    global k
    
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left) // 2
    arr1 = mergesort(left, mid, arr)
    arr2 = mergesort(mid + 1, right, arr)
    ptr1 = ptr2 = 0
            
    return merger(arr1, arr2)

def merger(arr1, arr2):
    global k
    res = []
    ptr1 = ptr2 = 0
    
    while ptr2 < len(arr2) and arr2[ptr2][1] < arr1[0][1] - k:
        ptr2 += 1
    while ptr1 < len(arr1) and arr1[ptr1][1] < arr2[0][1] - k:
        ptr1 += 1
        
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1][1] <= arr2[ptr2][1]:
            res.append(arr1[ptr1])
            ptr1 += 1
        else:
            res.append(arr2[ptr2])
            ptr2 += 1
    
    if ptr1 < len(arr1):
        res.extend(arr1[ptr1:])
  
    if ptr2 < len(arr2):
        res.extend(arr2[ptr2:])
   
    return res 

n, k = map(int, input().split())
lst = list(map(int, input().split()))
arr = []
for idx, val in enumerate(lst):
    arr.append([idx, val])
    
ans = [val[0] + 1 for val in mergesort(0, len(arr) - 1, arr)] 
ans.sort()
print(*ans)
    
    
    
