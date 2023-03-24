t = int(input())

def mergesort(left, right, arr):
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left) // 2
    arr1 = mergesort(left, mid, arr)
    arr2 = mergesort(mid + 1, right, arr)
    
    return merger(arr1, arr2)

def merger(arr1, arr2):
    global no_swap
    if not arr1 or not arr2:
        no_swap = - 1
        return []
    if arr1[0] < arr2[0] and arr1[-1] < arr2[0]:
        res = arr1 + arr2
        return res
    elif arr2[0] < arr1[0] and arr2[-1] < arr1[0]:
        no_swap += 1
        res = arr2 + arr1
        return res
    else:
        no_swap = - 1
        return []
    
   
for _ in range(t):
    p = int(input())
    lst = list(map(int, input().split()))
    no_swap = 0   
    
    mergesort(0, len(lst) - 1, lst)
    
    print( no_swap)
    
