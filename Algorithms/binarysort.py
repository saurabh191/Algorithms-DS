

##Binary sort algorithm

def binsort(arr,k):
    r = len(arr) -1
    l = 0
    while l <=r:
        mid = (l+r)//2
        if arr[mid] == k:
            posn = mid
            return posn
        else:
            if arr[mid] < k:
                l = mid
            else:
                r = mid
    
    




#if __name__ == 'main':
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
k = 56
n_value = binsort(arr,k)
print(n_value+1)
    
    
