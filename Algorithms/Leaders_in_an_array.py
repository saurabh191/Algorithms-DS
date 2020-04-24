def fetchLeader(iarr,N):
	oarr = iarr
	larr = []
	for outerrange in range(N):
		if outerrange == N-1:
			larr.append(oarr[outerrange])
		else:
			for innerrange in range(N):
				if oarr[outerrange] >= iarr[innerrange]:
					if innerrange == N-1:
						larr.append(iarr[innerrange])
					pass
				elif oarr[outerrange] < iarr[innerrange]:
					continue
			
	return larr

T = int(input())
for i in range(T):
	N = int(input())
	arr = [int(i) for i in input().split(' ') if i]
	larr = fetchLeader(arr,N)
	s=''
	for i in range(len(larr)):
		s+= str(larr[i])+ ' '
	print(s)
		