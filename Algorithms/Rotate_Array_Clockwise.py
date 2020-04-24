#code
def rotateArray(arr,d,N):
    temp = []
    rarr = []
    if d > 0 and N > 1:
        for i in range(d):
            temp.append(arr[i])
        for j in range(d,N):
            rarr.append(arr[j])
        for k in range(d):
            rarr.append(temp[k])
        return rarr
    else:
        return arr
T = int(input())
for testcase in range(T):
    inValue = [int(i) for i in input().split(' ') if i]
    d = inValue[0]
    N = inValue[1]
    arr = [int(i) for i in input().split(' ') if i]
    rarr = rotateArray(arr,d,N)
    s = ''
    for i in range(N):
        s+=rarr[i]
    print(s)
	
# 1 2 3 4 5 6