#programa realizado en python 2.7

a=1;
while a==1: 
	try:
    		masa=float(raw_input("Ingrese su masa corporal : "))
		estatura=0
		while estatura <= 0:
			estatura=float(raw_input("Ingrese su estatura  : "))
		a=0
	except ValueError:
    		print "Eso no es un numero"
imc=masa/(estatura**2)
if imc<16:
	print "Esta en delgadez severa"
elif imc<17:
	print "Esta en delgadez moderada"
elif imc<18.5:
	print "Delgadez no muy pronunciada"
elif imc<25:
	print "Normal"
elif imc<30:
	print "preobeso"
elif imc<35:
	print "Obeso tipo I"
elif imc<40.00:
	print "Obeso tipo II"
else:
	print "Obeso tipo III"
 
print "Su indice de masa corporal es : ",imc