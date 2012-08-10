import random
import time

a=[]
for i in range(0,1000):
       numero = int(random.randint(0,1000))
       a.append(numero)
inicio=time.time()
for j in range(1,len(a)):
	key=a[j]
	i=j-1
	while i>-1 and a[i]>key:
		a[i+1]=a[i]
		i=i-1
	a[i+1]=key
fin=time.time()
for j in range(len(a)):
	print a[j]
print fin-inicio