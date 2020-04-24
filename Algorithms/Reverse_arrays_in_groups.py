def reverseArray(N,K,arr):
        start = 0
        s = K + start
        oarr = []
        temp = [None]*N               
        while(start < len(arr)):                
                if len(arr[start:]) < K:
                        s = N
                        for i in range(len(arr[start:])):
                                temp[start] = arr[s-1]
                                start+=1
                                s-=1
                else:
                        s = start + K
                        for i in range(K):
                                temp[start] = arr[s-1]
                                start+=1
                                s-=1
        return temp
T = int(input())
for i in range(T):
        inValue = [int(i) for i in input().split(' ') if i]
        N = inValue[0]
        K = inValue[1]
        arr = [int(n) for n in input().split(' ') if n ]
        print(len(arr))
        ##	reversedArray(N,K,arr)
        oarr = reverseArray(N,K,arr)
        ostr = ''
        for i in range(len(oarr)):
                ostr+=str(oarr[i])+ ' '
        print(ostr)
