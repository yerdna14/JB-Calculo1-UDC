#!/usr/bin/env python
# coding: utf-8

# # Teorema Fundamental del Cálculo
# 
# Calcular el valor de una integral definida empleando geometría o límites de las sumas de Riemann para particiones infinitamente refinadas, es, en general, una tarea complicada. En esta sección presentamos el teorema fundamental del cálculo, que nos da un medio para calcular muchas integrales. De hecho, reducirá el problema de integración al cálculo de primitivas, es decir, al problema inverso de la derivación.
# 
# 
# **Teorema** Sea $f \in {\cal R}[a,b]$.  Para $a \leq x \leq b$, sea: $$F(x) = \int_a ^x f(t) \,dt .$$
# Entonces, $F \in {\cal C}[a,b]$.  Además, si $f$ es continua en $[a,b]$, entonces $F$ es derivable en $[a,b]$
# y $F^{\,\prime} (x) = f(x)$, $\forall x \in [a,b]$.
# 
# También puede enunciarse de la siguiente manera:
# 
# Si $f : I \longrightarrow \mathbb R$ es continua en $I$, entonces tiene primitivas en $I$; 
# una de ellas es la integral definida $F$ dada por:
# $$F(x) = \int_a ^x f(t) \,dt,$$
# donde $a \in I$ *es cualquiera*.

# ## Consecuencia
# 
# **Teorema**
# Sea la función $F$ dada por la integral definida:
# $$F(x) = \int_{a(x)}^{b(x)} f(t) \, dt.$$
# Entonces, la derivada de $F$ con respecto a $x$ viene dada por: 
# $$F^{\,\prime}(x) = f(b(x)) \, b^{\prime}(x) - f(a(x)) \, a^{\prime}(x). $$

# ## Ejercicios de aplicación del teorema fundamental del cálculo.
# 
# * https://existelimite.blogspot.com/2017/01/examen-de-enero-de-2017-aplicacion-del.html
# * https://existelimite.blogspot.com/2014/02/calculo-de-extremos-de-f-mediante-el.html

# ## Regla de Barrow
# Si $f \in {\cal R}[a,b]$ y existe una primitiva $F$ de $f$ en $[a,b]$, entonces: $$\int_a ^b f(x) \,dx = \left. \begin{array}{c} \, \\ \, \end{array} F(x) \right|_a^b = F(b) - F(a).$$
# 
# Ejemplo:
# Calcula el área bajo la curva $y=\cos x$ en $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$.
# 
# Solución: $$A = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \cos x \, dx = \sin x \lvert_{-\frac{\pi}{2}}^{\frac{\pi}{2}} = \sin\left(\frac{\pi}{2}\right) - \sin\left(-\frac{\pi}{2}\right) = 1 - (-1) = 2.$$
# Así, el área de la región son dos unidades cuadradas.
# 
# 
# 
# 
# ### Integración por partes
# 
# **Teorema**
# Si $F$ y $G$ son dos funciones derivables en $[a,b]$, y se tiene: 
# $$\begin{cases} F^{\,\prime} = f \\ G^{\,\prime} = g \end{cases} \hspace{20mm} \text{en } [a,b],$$ siendo $f$ y $g$ integrables en $[a,b]$, entonces $$\int_a ^b F(x) \,g(x) \,dx = F(b) \,G(b) - F(a) \,G(a) - \int_a ^b f(x) \,G(x) \,dx.$$
