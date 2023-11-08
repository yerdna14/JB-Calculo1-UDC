#!/usr/bin/env python
# coding: utf-8

# (sec_PythonIntegracion)=
# # Integración en `Python`
# 
# Esta sección pretende ser un compendio (esperemos que claro y ordenado) de todo el `Python` que hemos ido usando en el Capítulo 4.
# 
# Objetivos:
# 
# * Cálculo de primitivas con `Sympy`.
# * Cálculo de integrales definidas con `Sympy`.
# * Implementación en `Numpy` de los métodos de integración numérica.
# * Cálculo en `Sympy` de integrales impropias.
# * Uso de `Sympy` para resolver EDOs.

# ## Cálculo de primitivas con `SymPy`
# Para calcular la integral de una función con `SymPy`, se emplea la función *integrate*. 
# Por ejemplo, para calcular una primitiva de $\sin(x)$, escribiremos 

# In[86]:


import sympy as sp

x = sp.symbols('x')
f_exp = sp.sin(x)
I = sp.integrate(f_exp,x)

print('Una primitiva de ',f_exp, ' es = ',I)


# `SymPy` no siempre es capaz de calcular una primitiva. En caso de no poder hacerlo, devuelve como salida la integral de partida:

# In[87]:


I = sp.integrate(sp.sin(x*sp.cos(x)),x)
print(I)


# ## Cálculo de integrales definidas con `Sympy`
# 
# Para calcular una integral definida, simplemente tendremos que añadir los límites de integración al comando `sp.integrate`.
# 
# Por ejemplo, para integrar $\displaystyle\int_0^\pi\sin(x)\,dx$, escribiremos

# In[88]:


import sympy as sp

x = sp.symbols('x')
f_exp = sp.sin(x)
Idef = sp.integrate(f_exp,(x,0,sp.pi))  # Integral de f_exp con x entre 0 y pi

print('La integral de ',f_exp, ' entre 0 y pi es = ',Idef)


# ## Integración numérica con `Numpy`
# 
# ### Fórmulas simples
# 
# A continuación mostramos las *functions* que nos permiten la programación de las fórmulas simples que acabamos de ver en `Numpy` y un ejemplo de su aplicación. 
# 
# Probaremos sobre 
# 
# $$
# I=\int_{0}^{3}\left(x^4+1\right)\,dx\,,
# $$
# ya que, en este caso sencillo, podemos conocer el valor exacto de la integral:
# 
# $$
# I=\int_{0}^{3}\left(x^4+1\right)\,dx = \left[\frac{x^5}{5}+x\right]_{x=0}^{3} = \frac{3^5}{5}+3 = 51.6\, .
# $$

# In[89]:


import sympy as sp
import numpy as np

def pto_medio(a, b, fpm):
    aprox_pm = (b-a) * fpm
    return aprox_pm

def trapecio(a, b, fa, fb):
    aprox_tr = (b-a) * (fa + fb)/2
    return aprox_tr

def simpson(a, b, fa, fpm, fb):
    aprox_simp = (b-a) * (fa + 4*fpm + fb)/6
    return aprox_simp

x = sp.Symbol('x', real = True)

f_exp = x**4 + 1
f = sp.lambdify(x,f_exp)

a = 0
b = 3
pm = (a+b)/2

fa = f(a)
fpm = f(pm)
fb = f(b)

print('Valor aproximado de I mediante la fórmula del punto medio = ', pto_medio(a,b,fpm) ) 
print('Valor aproximado de I mediante la fórmula del trapecio = ', trapecio(a,b,fa,fb) ) 
print('Valor aproximado de I mediante la fórmula de Simpson = ', simpson(a,b,fa,fpm,fb) ) 


# ### Fórmulas compuestas
# 
# Como puedes ver en el apartado anterior, las fórmulas simples pueden dar resultdos bastante... pésimos.
# 
# Vamos a implementar ahora de manera eficiente las fórmulas compuestas utilizando la función de `np.sum`. 

# In[90]:


import sympy as sp
import numpy as np

x = sp.Symbol('x', real = True)
f_exp = x**4+1
f = sp.lambdify(x,f_exp)

a = 0; b = 3
n = 100

x1 = np.linspace(a,b,n+1) # aquí guardamos los x_{i}. 
                          # Recuerda que, en Python, se guarda x1[0], x1[1], ..., x1[(n+1)-1] = x1[n]
y1 = f(x1)

h = (b-a)/n # el tamaño de cada subintervalo

aprox_trap = h/2 * (y1[0]+2*np.sum(y1[1:n])+y1[n])
aprox_medio = 2*h * np.sum(y1[1:n:2])
aprox_simpson = 2*h/6 * (y1[0] + 4*np.sum(y1[1:n:2])+2*np.sum(y1[2:n-1:2])+y1[n])

print('aprox_trap: ',aprox_trap) 
print('aprox_medio: ',aprox_medio) 
print('aprox_simpson: ',aprox_simpson) 

print('Exacta: ',b**5/5+b)


# ## Cálculo de integrales impropias con `Sympy`
# 
# Es posible calcular con `Sympy` integrales impropias de primera especie, es decir, integrales con límites de integración $-\infty$ y/o $+\infty$.
# 
# Esto se puede hacer bien directamente, bien aplicando la definición de integral impropia (es decir, combinando una integral de Riemann con un límite). Veámoslo:

# In[91]:


import sympy as sp
x = sp.symbols('x', real = True)
M = sp.Symbol('M', real = True)

f_exp = sp.exp(x)

# Cálculo directo
I_directo = sp.integrate(f_exp,(x,-sp.oo,0))
print('Integral de ',f_exp,' entre -oo y 0 es = ',I_directo)

# Cálculo con límites
I_limites = sp.limit( sp.integrate(f_exp,(x,-M,0)), M, +sp.oo )
print('Integral de ',f_exp,' entre -oo y 0 es = ',I_limites)


# Del mismo modo podemos calcular una integral impropia de segunda especie. Por ejemplo, 
# 
# $$
# \int_{0}^2\dfrac{1}{\sqrt{x}}\,dx\, .
# $$

# In[92]:


import sympy as sp
x = sp.symbols('x', real = True)
c = sp.Symbol('c', real = True)

f_exp = 1/sp.sqrt(x)

# Cálculo directo
I_directo = sp.integrate(f_exp,(x,0,2))
print('La integral vale = ', I_directo)

# Cálculo con límites
I_limites = sp.limit( sp.integrate(f_exp,(x,c,2)), c, 0, dir='+')
print('La integral vale = ', I_limites)


# Por supuesto, en ocasiones nos encontraremos con integrales no convergentes:

# In[93]:


import sympy as sp
x = sp.symbols('x', real = True)
c = sp.Symbol('c', real = True)

f_exp = 1/x

# Cálculo con límites
I_limites = sp.limit( sp.integrate(f_exp,(x,c,2)), c, 0, dir='+')
print('La integral vale = ', I_limites)


# ## Uso de `Sympy` para resolver EDOs
# 
# A continuación mostramos cómo se puede utilizar `Sympy` en la resolución de EDOs. 
# 
# Realmente, es muy sencillo. 
# 
# 1. Las variables independientes se definen como símbolos (`sp.Symbol`), mientras que las variables dependientes se definen como funciones (`sp.Function`).  
# 2. Definimos la EDO con el comando `sp.Eq`, destacando la dependencia de la variable dependiente de la independiente. En el siguiente ejemplo, puedes ver cómo en la línea 7 escribimos `v(x)' cada vez que aparece la variable dependiente $v$.
# 3. Las derivadas se escriben, dentro de la definición `sp.Eq` indicando la variable dependiente y la variable dependiente respecto a la que se derivan. En el ejemplo que aparece a continuación, escribimos $v'$ como `v(x).diff(x)`.
# 4. Una vez definida la EDO, la resolvemos con el comando `sp.dsolve`.
# 5. Podemos usar `sp.dsolve` sin más atributos para encontrar la solución general, o podemos incluir una condición inicial, que debemos definir como `ics`, como se puede ver en la penúltima línea del siguiente código.
# 
# Como ejemplo, vamos a calcular la velocidad de un cuerpo con masa $72$ kilogramos, si suponemos que su velocidad inicial es nula y su coeficiente de resistencia al aire es $k=0.2$. 
# 
# Es decir, en función de lo que vimos en la sección anterior, vamos a resolver el problema de valor inicial
# 
# $$
#     \left\{\begin{array}{rcl}
#     72 v'&=& 72*9.81 - 0.2 v\,,\\
#     v(0) &=& 0\,,
#     \end{array}\right.
# $$

# In[94]:


import sympy as sp

# Variable independiente
x = sp.Symbol ('x')
# Variable dependiente (definida como Function)
v = sp.Function ('v')

# Escribimos la EDO 
eq = sp.Eq (72*v(x).diff(x), 72*9.81 - 0.2*v(x))

# Calculamos su solución general (este paso no sería necesario, pero queda como ejemplo)
s_general = sp.dsolve (eq)   
display (s_general)

# Calculamos la solución particular que nos preguntan
s_particular = sp.dsolve (eq, ics={v(0): 0.0}) 
display (s_particular)

