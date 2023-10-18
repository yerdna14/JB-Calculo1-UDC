#!/usr/bin/env python
# coding: utf-8

# # Derivación en **Python**
# 
# Esta sección pretende ser un compendio (esperemos que claro y ordenado) de todo el `Python` que hemos ido usando en el Capítulo 3.
# 
# Objetivos:
# 
# * Cálculo de derivadas con `Sympy`.
# * Implementación en `Numpy` del método numérico de Newton-Raphson.
# * Derivadas sucesivas con `Sympy`.
# * Uso de `Python` en problemas de máximos y mínimos.
# * Cálculo, con `Sympy`, del polinomio de Taylor y del resto. 

# ## Derivación en `Sympy`
# 
# La realizaremos con el comando `sp.diff`, como mostramos en el siguiente ejemplo:

# In[1]:


import sympy as sp
x=sp.symbols('x')
f_exp=sp.exp(x)*sp.cos(x)
d1f_exp=sp.diff(f_exp,x)
print('Para la función: ',f_exp)
print('La derivada primera es: ',d1f_exp)


# ## Implementación en `Numpy` del método numérico de Newton-Raphson
# 
# Mostramos a continuación una implementación directa, mediante un bucle, de este método:

# In[2]:


import numpy as np
import sympy as sp

x = sp.symbols('x', real=True) # define la variable simbólica x

f_expr = x**3+2*x-2
f_der_expr = sp.diff(f_expr,x)

f = sp.Lambda(x,f_expr)
f_der = sp.Lambda(x,f_der_expr)

N_max = 10
tol = 1.e-9

x_aprox = np.zeros(N_max)
x_aprox[0] = 2

for k in range(1,N_max):
    if f_der(x_aprox[k-1]) == 0: break

    x_aprox[k] = x_aprox[k-1] - f(x_aprox[k-1])/f_der(x_aprox[k-1])

    if ( (k > 0) and (np.abs(x_aprox[k]-x_aprox[k-1]) / np.abs(x_aprox[k]) < tol) ): break

print('Número de iteraciones realizadas: ', k) 
print('Aproximación de la raíz: ', x_aprox[k])


# En la Sección {ref}`sec_NewtonRaphson` puedes ver el gráfico de este caso con `Matplotlib`.

# ## Derivadas sucesivas con `Sympy`
# 
# Para calcular derivadas sucesivas en `Sympy` tenemos que añadir un parámetro en `sp.diff` que indique el número de veces que queremos derivar:

# In[3]:


import sympy as sp

x = sp.symbols('x', real=True)
f_exp = sp.sin(x) + x**2
print('Expresión que queremos derivar: ',f_exp)
print('Primera derivada: ',sp.diff(f_exp,x))
print('Segunda derivada: ',sp.diff(f_exp,x,2))
print('Tercera derivada: ',sp.diff(f_exp,x,3))
# Nota: también se puede usar la siguiente escritura:
# print(f_exp.diff(x,3))


# ## Uso de `Python` en problemas de máximos y mínimos
# 
# Dado un canal de sección trapezoidal de lado 2, calcular el ángulo $\alpha$ (ver dibujo) que maximiza el área de la sección del canal.
# 
# <img src="../../images/cap3-canal.svg" width="300"/>
# 
# 1. A mano. Obtener la función que proporciona el área del canal en función del ángulo $ \alpha $
# 2. Simbólicamente: con **Sympy**.
# 3. Numéricamente mediante el método de Newton con error menor que $ 10^{-4} $.

# In[4]:


import sympy as sp
# 2. Resolvemos el problema utilizando Sympy
x,xn=sp.symbols('x,xn')
# Funcion que describe el area de la seccion en funcion del angulo
f=4*sp.sin(x)*(1+sp.cos(x))
d1f=sp.diff(f,x)
d1fn=sp.lambdify(x,d1f)
alphamax=sp.solve(d1f)
print('La sección máxima se alcanza con ángulo: ',float(alphamax[1]))


# In[5]:


# 3. Aproximamos el máximo con el método de Newton
maxit=100
eps=1e-4
d2f=sp.diff(d1f,x)
d2fn=sp.lambdify(x,d2f)
xn=np.pi/2
for i in range(0,maxit):
    res=d1fn(xn)/d2fn(xn)
    xn=xn-res
    if (np.abs(res)<eps):
        break
print('Numero de iteraciones realizadas: ',i)
print('Aproximación del ángulo para la sección máxima con NR: ',xn)


# ## Cálculo, con `Sympy`, del polinomio de Taylor y del resto. 
# 
# La siguiente función calcula, de forma simbólica, el polinomio de Taylor de una función dada. 
# 
# * Argumentos de entrada: 
#     * expresión f, 
#     * punto x0, que será el centro de Taylor, 
#     * orden del polinomio, n.
# * Salida:
#     * expresión del polinomio de Taylor, p,
#     * epresión del resto de Taylor, r.

# In[6]:


import sympy as sp

x,t=sp.symbols('x,t')

# p: polinomio de Taylor
# R: resto en valor absoluto
def taylor(f,x0,n):
    p=0
    for i in range(n+1):
        p+=sp.diff(f,x,i).subs(x,x0)/sp.factorial(i)*(x-x0)**i
    R=sp.diff(f,x,n+1).subs(x,t)/sp.factorial(n+1)*(x-x0)**(n+1)
    return p,R


# En la Sección {ref}`sec_Taylor` puedes ver cómo se aplica esta función a un problema concreto.
