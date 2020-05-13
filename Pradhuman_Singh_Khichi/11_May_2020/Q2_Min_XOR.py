print("Enter The Numbers:- ",end=' ')
arr= list(map(int,input().split()))
arr.sort()
m=999999999
res=0
for i in range(0,len(arr)-1):
	res = arr[i] ^ arr[i+1]
	m=min(m,res)
print("Minimum XOR value is:- {0:d}".format(m))