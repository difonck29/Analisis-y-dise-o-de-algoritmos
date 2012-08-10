import time

a=[10,9,8,7,6,5,4,3,2,1]
inicio = time.time()
for j in range(1,len(a)):
	key=a[j]
	i=j-1
	while i>-1 and a[i]>key:
		a[i+1]=a[i]
		i=i-1
	a[i+1]=key
fin = time.time()
for j in range(len(a)):
	print a[j]
print fin-inicio
