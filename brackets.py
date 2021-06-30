# por: Pamela Lincoqueo
from sympy import *
from matplotlib.pyplot import figure, show
import matplotlib as mpl
mpl.rcParams['text.usetex'] = False#usa latex integrado de matplotlib
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
expresion = input(" Ingrese expresión (ejemplo: ((2/x)+3*x)**2): ")
original = parse_expr(expresion); a = ""
if unaInte and definida:# función con una sola integral definida
	sol = integrate(expresion,(x,limInf,limSup))
	a = "\int_{"+limInf+"}^{"+limSup+"}"

if unaInte and not definida:# función con una sola integral no definida
	sol = integrate(expresion,x)
	a = "\int"

if not unaInte:# función de varias integrales no definidas
	sol = integrate(expresion,x)
	a = a + "\int "
	for i in range(1,cInte):
		sol = integrate(sol,x)
		a = a + "\int "

print("\n Respuesta:",sol)

a = a + latex(original)
sol = latex(sol)

fig = figure(figsize=(5, 3.5))
fig.text(0.5,0.5,"Expresión: $%s$\nSolución: $%s$"%(a,sol),ha='center', va='center', size=20)
fig.canvas.set_window_title('Método de (los no) Brackets')
show()