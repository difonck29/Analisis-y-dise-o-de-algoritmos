import time

def partition(A,p,q):
	x=A[p]
	i=p
	for j in range(p+1,q):
		if A[j]<=x:
			i=i+1
			aux=A[i]
			A[i]=A[j]
			A[j]=aux
	aux=A[p]
	A[p]=A[i]
	A[i]=aux
	return i;

def quicksort(A,p,r):
	if p<r:
		q=partition(A,p,r);
		quicksort(A,p,q-1);
		quicksort(A,q+1,r);
A=[3,4,6,2,10,9,8,7,6,5,4,3,2,1,8]

inicio=time.time()
quicksort(A,0,4)
fin=time.time()
print(A)
print "tiempo :",(fin-inicio)
		
