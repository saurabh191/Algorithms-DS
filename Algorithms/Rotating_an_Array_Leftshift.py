def rotateArray(arr,d,N):
    rarr = []
    temp=[]
    if d > 0 and N > 1:
        for i in range(d):
            temp.append(arr[i])
        for j in range(d,N):
            rarr.append(arr[j])
        for k in range(len(temp)):
            rarr.append(temp[k])
        return rarr
    elif d == N:
        return arr
    else:
        return arr
T = input()
N = int(input())
arr = [int(i) for i in input().split(' ') if i]
d = int(input())
rarr = rotateArray(arr,d,N)
s = ''
for i in range(N):
    s += str(rarr[i]) + " "
print(s)
