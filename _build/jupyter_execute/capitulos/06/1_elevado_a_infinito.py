#!/usr/bin/env python
# coding: utf-8

# # EJERCICIO: Calcula el siguiente límite: $\;\; \displaystyle\lim_{x\to 0}\left({\cos(3x)}^{\frac{1}{x^2}}\right)$.
# 

# ## Solución:

# En primer lugar, intentamos una sustitución directa:
# 
# $$
# \lim_{x\to 0}\left({\cos(3x)}^{\frac{1}{x^2}}\right) = \cos(0)^{+\infty} = 1^{+\infty} = \text{Indeterminado}.
# $$
# 
# Estamos ante una indeterminación del tipo $1^{\infty}$. Para resolverla tenemos que hacer *saltar* el exponente, y eso se conigue con un logaritmo (neperiano, por supuesto).
# 
# $$
# L=\lim_{x\to 0}\left({\cos(3x)}^{\frac{1}{x^2}}\right) \Rightarrow 
# \ln L = \ln \left[\lim_{x\to 0}\left({\cos(3x)}^{\frac{1}{x^2}}\right)\right].
# $$
# 
# Utilizamos ahora que, al ser el logaritmo neperiano una función continua en su dominio, conmuta con el límite. Entonces:
# 
# $$
# \ln L =
# \lim_{x\to 0}\left[\ln\left({\cos(3x)}^{\frac{1}{x^2}}\right)\right] =
# \lim_{x\to 0}\frac{1}{x^2}\ln\left({\cos(3x)}\right).
# $$
# 
# Vamos a resolver este límite, que ahora ya es una indeterminación del tipo 0.$(\infty)$:
# 
# \begin{align*}
# \ln L &=& \lim_{x\to 0}\frac{1}{x^2}\ln\left({\cos(3x)}\right) = 
# \lim_{x\to 0}\frac{\ln\left({\cos(3x)}\right)}{x^2} = \frac{\ln 1}{0} = \frac{0}{0} = \text{Ind} \\
# \vphantom{lim}\\
# &\stackrel{\stackrel{\color{blue}{\text{l'Hopital}}}{\downarrow}}{=}& 
# \lim_{x\to 0}\frac{\frac{1}{\cos(3x)}\left(-\sin(3x)\right)3}{2x}=
# -\frac{3}{2}\lim_{x\to 0}\frac{\sin(3x)}{x\cos(3x)} = \frac{0}{0} = \text{Ind} \\
# \vphantom{lim}\\
# &\stackrel{\stackrel{\color{blue}{\text{l'Hopital}}}{\downarrow}}{=}& 
# -\frac{3}{2}\lim_{x\to 0}\frac{3\cos(3x)}{\cos(3x)-3x\sin(3x)}0-\frac{3}{2}\frac{3}{1-0} = -\frac{9}{2}.
# \end{align*}
# 
# De donde obtenemos, finalmente, que,
# 
# $$
# \ln L = -\frac{9}{2} \Rightarrow L = e^{-\frac{9}{2}} = \frac{1}{e^{\frac{9}{2}}} = \frac{1}{\sqrt{e^9}}
# = \frac{1}{e^4\sqrt{e}} = \frac{\sqrt{e}}{e^5}.
# $$

# ### Vamos a comprobar nuestros cálculos utilizando *python* y, en concreto, su librería *sympy*:

# In[1]:


import sympy as sp

x = sp.Symbol('x', real=True) 

expr = sp.cos(3*x)**(1/x/x)
print('f(x) = ',expr)

L = sp.limit(expr,x,0)
print('L = ',L)


# ### Ahora vamos a dibujar la gráfica de la función utilizando *numpy* y *matplotlib*. Fijémonos en el valor de $f$ en el $0$, que es el límite que hemos estado calculando.

# In[2]:


# importamos los módulos numpy y pyplot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.49, 0.49)
y1 = np.cos(3*x)**(1/x/x)

# plot
fig = plt.figure()
ax  = fig.add_subplot(111)
ax.plot(x, y1, c='b', label=r'$\cos(3x)^{\frac{1}{x^2}}$',linewidth=3.0)

plt.axhline(y=np.exp(-9/2), xmin=-0.49, xmax=1.0, label=r'$\frac{\sqrt{e}}{e^5}$', color='r', linestyle='--')

leg = plt.legend(loc="upper right")

plt.grid()
plt.show()

