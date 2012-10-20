import time

def countingSort(A, k):
	""" implementation of counting sort """
	B = [0 for el in A]
	C = [0 for el in xrange(0, k+1)]
 
	for i in xrange(0, k +1):
		C[i] = 0
 
	for j in xrange(0, len(A)):
		C[A[j]] += 1
 
	for i in xrange(1, k + 1):
		C[i] += C[i - 1]
 
	for j in xrange(len(A)-1, 0 - 1, -1):
		tmp = A[j]
		tmp2= C[tmp] -1
		B[tmp2] = tmp
		C[tmp] -= 1
	return B
 
inicio=time.time()
print countingSort([6,0,2,0,1,3,4,6,1,3,2], 6)
fin=time.time()
print "TIempo : ",(fin-inicio)