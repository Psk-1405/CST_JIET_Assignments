#Printing The Single Number without using Extra Memory
print("Enter The Numbers:-",end=' ')
arr= list(map(int,input().split()))
l=len(arr)
for i in range(1,l):
	arr[i]^=arr[i-1]
print("The Single Number is:- {0:d}".format(arr[l-1]))

