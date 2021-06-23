# por: Pamela Lincoqueo
from sympy import *
x,y,z,t,a,b,c,n,m,p,k = symbols('x y z t a b c n m p k')#define variables incognitas para operar

unaInte = str(input(" Tiene una sola integral? (y/n): "))
if unaInte=="y":
	unaInte = True
	definida = str(input(" Es definida? (y/n): "))
	if definida=="y":
		definida = True
		limInf = str(input(" Limite inferior: "))
		limSup = str(input(" Limite superior: "))
	else:
		definida = False
# ---------------------------------------------------------
elif unaInte=="n":
	unaInte = False
	cInte = int(input(" Cuantas integrales tiene? (ejemplo: 2): "))
	definida = 0

# ---------------------------------------------------------
func = input(" Ingrese función: ")
if unaInte and definida:# funcion con una sola integral definida
	print("\n Respuesta: ",integrate(func,(x,limInf,limSup)))

if unaInte and not definida:# funcion con una sola integral no definida
	print("\n Respuesta: ",integrate(func,x))

if not unaInte:# funcion de varias integrales no definidas
	for i in range(cInte):
		func = integrate(func,x)
	print("\n Respuesta: ",func)