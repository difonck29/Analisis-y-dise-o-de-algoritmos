d=0
num = input("Introduzca un numero para empezar la serie : ")
a=0
b=1
print a
print b
c=0
while d<num-2:
	c=a+b
	print c
	a=b
	b=c
	d=d+1