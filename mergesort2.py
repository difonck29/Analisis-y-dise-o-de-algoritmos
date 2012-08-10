import time
import random

def funcion(n):
	if n==0:
		print("Hola")
	print n
	if n<1:
		exit()
	funcion(n-1)


def merge(left, right):
	result = []
	i ,j = 0, 0
    	while i < len(left) and j < len(right):
        	if left[i] <= right[j]:
            		result.append(left[i])
            		i += 1
       		else:
            		result.append(right[j])
            		j += 1
    	result += left[i:]
    	result += right[j:]
    	return result

def mergesort(list):
	if len(list) < 2:
		return list
    	middle = len(list) / 2
    	left = mergesort(list[:middle])
    	right = mergesort(list[middle:])
    	return merge(left, right)

vector3=[]
for i in range(0,100):
       numero = int(random.randint(0,100))
       vector3.append(numero)

#operacion mergesort con vector de 10 posiciones


print"__________________________________________"
print "Mergesort vector 100 posiciones"
print
inicio=time.time();
print mergesort(vector3)
fin=time.time()
print
print "El tiempo fue : ",fin-inicio
print"__________________________________________"