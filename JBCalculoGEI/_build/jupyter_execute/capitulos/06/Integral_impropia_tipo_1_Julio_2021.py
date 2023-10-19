#!/usr/bin/env python
# coding: utf-8

# ## **EJERCICIO 17, examen Julio 2021:**  
# 
# ### Se considera la función $f(x)=\frac{\ln x}{x^4}$. Calcula el área que encierra la gráfica de esta función y el eje OX en el intervalo $[1,+\infty]$.

# **Solución:**

# In[3]:


import sympy as sp
from sympy import oo

x = sp.Symbol('x', real=True) 
M = sp.Symbol('M', real=True) 

# Calculamos una primitiva de f 
f_expr = sp.ln(x)/x**4
F_expr = sp.integrate(f_expr,x) # esto es una expresión
print('Primitiva para f: ', F_expr)

F = sp.Lambda((x),F_expr) # convertimos la expresión anterior en una función Lambda

# Aplicamos Barrow en el intervalo [1,M]
print('Integral en [1,M]: ', F(M)-F(1))

#Finalmente, hacemos que M tienda a infinito (oo, en la notación de sympy)
print('Límite cuando M tiende a infinito: ', sp.limit(F(M)-F(1), M, oo))


# In[4]:


# importamos los módulos numpy y pyplot
import numpy as np
import matplotlib.pyplot as plt

# Damos valores de x para evaluar las funciones 
x = np.linspace(1, 10)

#Calculamos las 2 funciones (f y su primitiva, F) en los puntos de x
# y1 = F(x)
y1 = np.log(x)/x**4
y2 = -np.log(x)/(3*x**3) - 1/(9*x**3)
y3 = 1/9 - np.log(x)/(3*x**3) - 1/(9*x**3)

# plot
fig = plt.figure()
ax  = fig.add_subplot(111)
ax.plot(x, y1, c='b', label=r'$f(x)$',linewidth=3.0)
ax.plot(x, y2, c='r', label=r'$F(x)$',linewidth=3.0)
ax.plot(x, y3, c='g', label=r'$F(M)-F(1)$',linewidth=3.0)

# plt.ylim(-100,500)
leg = plt.legend()

plt.grid()
plt.show()

