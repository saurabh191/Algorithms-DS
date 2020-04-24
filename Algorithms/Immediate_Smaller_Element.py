def findsmall(arr):
    u = len(arr) - 1
    rarr = []
    for l in range(0,len(arr)):
        if l < u:
            if int(arr[l]) < int(arr[l+1]):
                rarr.append(-1)
            elif arr[l] == arr[l+1]:
                rarr.append(-1)
            else:
                rarr.append(arr[l+1])
        elif l == u:
                rarr.append("-1")
    return rarr
    
testcase_num = int(input())
#for i in range(1,testcase_num+1):
arr_size = input()
input_string = input()
arr = [int(i) for i in input_string.split(" ") if i]
rarr = findsmall(arr)
s = ''
for i in range(len(rarr)):
    s += str(rarr[i])+' '
print(s)





##def findsmall(arr):
##    #l = 0
##    u = len(arr) - 1
##    p = 1
##    rarr = []
##    for l in range(0,len(arr)):
##        if l < u:
##            if arr[l] > arr[l+1]:
##                rarr.append(arr[l+1])
##            else:
##                rarr.append(-1)
##        elif l == u:
##                rarr.append(-1)
##    print(rarr)
##
##arr = [4,2,1,5,3]
##findsmall(arr)
#print(rarr)
            
                
                            
            
            
