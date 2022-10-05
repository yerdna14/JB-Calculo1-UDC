#!/usr/bin/env python
# coding: utf-8

# # Aplicaciones de la derivada
# 
# ## Extremos relativos y absolutos
# 
# Supongamos un intervalo abierto $A \subset \mathbb{R}$ y una aplicación $f : A \longrightarrow \mathbb{R}$.
# 
# ````{prf:definition} 
# :label: def_extremo_relativo
# :nonumber: 
# 
# Decimos que $f$ presenta un **máximo relativo** en $a \in A$ si y sólo si existe $h > 0$ tal que
# 
# \begin{equation*}
# f(x) \leq f(a) , \quad \forall x \in (a-h,a+h) \, .
# \end{equation*}
# Análogamente, decimos que $f$ presenta un **m\'{i}nimo relativo** en $a \in A$ si y sólo si existe $h > 0$ tal que:
# 
# \begin{equation*}
# f(x) \geq f(a) , \quad \forall x \in (a-h,a+h) \, .
# \end{equation*}
# Por extremo relativo entendemos, indistintamente, un máximo o un mínimo relativo.
# ````
# 
# Definiremos, a continuación, punto crítico (o punto estacionario) y, acto seguido, nos ponemos a estudiar la relación entre extremos relativos y puntos críticos.
# 
# ````{prf:definition} 
# :label: def_punto_critico
# :nonumber: 
# Si en un punto $a$ se tiene $f'(a) = 0$, decimos que $a$ es un **punto crítico** (o **estacionario**) de la función $f$.
# ````
# 
# En cuanto a la relación entre puntos críticos y extremos relativos (que tienden a confundirse... aunque no son lo mismo),
# en primer lugar, tenemos que destacar que un extremo relativo puede ser un punto en el que ni siquiera exista derivada (y, por lo tanto, no será punto crítico). 
# El ejemplo más clásico es la función valor absoluto. Si recuerdas su dibujo, verás fácilmente que esta función tiene un mínimo relativo en $x=0$... ¡pero en ese punto la 
# función valor absoluto no es derivable!
# 
# Para cubrir esta primera posibilidad vamos a ver el primer criterio para localizar extremos relativos. Suele conocerse por *criterio de la primera derivada* y, si lo lees atentamente,
# verás que pedimos que la función sea derivable cerca del punto en cuestión, pero no necesariamente en él (es decir, valdría para la función valor absoluto en $x_{0}=0$):
# 
# ````{prf:property} Criterio de la primera derivada
# :label: prop_criterio_primera_derivada
# :nonumber: 
# 
# Sea $f:[a,b] \longrightarrow \mathbb{R}$ una función continua, $x_0 \in (a,b)$ y sea $r > 0$ tal que $f$ es derivable en 
# $(x_0-r,x_0) \cup (x_0,x_0+r)$. Entonces
# * Si $f'(x)<0$, $\forall x\in (x_0-r,x_0)$ y $f'(x)>0$, $\forall x\in (x_0,x_0+r)$, entonces $f$ presenta en $x_0$ un mínimo relativo.
# * Si $f'(x)>0$, $\forall x\in (x_0-r,x_0)$ y $f'(x)<0$, $\forall x\in (x_0,x_0+r)$, entonces $f$ presenta en $x_0$ un máximo relativo.
# 
# ````
# 
# Pero, ¿qué pasa si la función sí es derivable en un extremo relativo? En este caso, tenemos el siguiente teorema:
# 
# ````{prf:theorem} 
# :label: th_cond_necesaria_extremo
# :nonumber: 
# 
# Si $f$ presenta un extremo relativo en el punto $a \in A$ y $f$ es derivable en
# dicho punto, entonces $f'(a) = 0$.
# ````
# 
# Fíjate bien en que **la condición anterior es necesaria, pero no suficiente**: la función puede presentar derivada nula en un punto, pero no tener un extremo en él. 
# Es decir, para funciones derivables, *extremo relativo $\Rightarrow$ punto crítico*, pero *punto crítico $\not\Rightarrow$ extremo relativo*.
# 
# Por ejemplo, la función $f(x) = x^3$ verifica $f'(0) = 0$, pero no se trata de un máximo ni de un mínimo.
# 
# Entonces, resumiendo lo que acabamos de ver, cuando nos interesa localizar los extremos relativos de una función en un determinado intervalo (abierto), lo primero que haremos será buscar sus puntos críticos (es decir, buscar los $x$ tales que $f'(x)=0$) y, a continuación, aplicar alguno de los criterios para la identificación de extremos relativos. Ya hemos visto el de la primera derivada, vamos a ver ahora el más utilizado:
# 
# ````{prf:property} Criterio de la segunda derivada
# :label: prop_criterio_segunda_derivada
# :nonumber: 
# 
#  Sea $f: (a,b) \longrightarrow \mathbb{R}$ con derivada segunda continua en $(a,b)$. Sea $x_0 \in (a,b)$ tal que $f'(x_0) = 0$. Entonces:
# * si $f''(x_0) < 0$, $f$ presenta en $x_0$ un máximo relativo,
# * si $f''(x_0) > 0$, $f$ presenta en $x_0$ un mínimo relativo.
# 
# ````
# 
# ¿Y si no podemos aplicar la propiedad anterior? Es decir, si hemos encontrado un punto $x_{0}$ en el que $f'(x_{0})=0$ y $f''(x_{0})=0$, ¿qué hacemos?
# Pues utilizar el siguiente criterio:
# 
# ````{prf:property} Criterio de la n-ésima derivada
# :label: prop_criterio_derivada_n
# :nonumber:
# 
# Sea $f \in \mathcal{C}^{n} (a,b)$ para algún $n \geq 1$. Sea $x_0 \in (a,b)$ tal que $f'(x_0) = f''(x_0) = \ldots = f^{(n-1)}(x_0) = 0$ y $f^{(n)}(x_0) \neq 0$. Entonces
# * Si $n$ es par y $f^{(n)}(x_0)<0$, $f$ presenta en $x_0$ un máximo relativo.
# * Si $n$ es par y $f^{(n)}(x_0)>0$, $f$ presenta en $x_0$ un mínimo relativo.
# * Si $n$ es impar, $f$ no tiene extremo relativo en $x_0$.
# 
# ````

# 
# ````{prf:definition} 
# :label: def_extremo_absoluto
# :nonumber: 
# 
# Se denomina supremo e ínfimo de $f$ en $A$, respectivamente, a las cantidades:
# \begin{equation*}
# \underset{x \in A}{\sup} f(x) \quad \quad \text{ e } \quad \quad 
# \underset{x \in A}{\inf} f(x) \, , 
# \end{equation*}
# es decir, al supremo e ínfimo del conjunto imagen $f(A)$.
# 
# Cuando el supremo o el ínfimo de $f$ en $A$ existen y pertenecen a $f(A)$, se denominan **máximo absoluto** y **mínimo absoluto** de $f$ en $A$, respectivamente. 
# 
# El máximo y el mínimo absoluto se denominan, globalmente, **extremos absolutos**.
# ````
# 
# 
# 
# Entonces, para encontrar los extremos (máximos y mínimos) absolutos de una función en un intervalo cerrado $[a,b]$, debemos estudiar:
# - los puntos estacionarios de $f$ en $(a,b)$, es decir, los puntos $x\in (a,b)$ tales que $f$ es derivable y $f'(x) = 0$,
# - los puntos donde $f$ no es derivable,
# - los extremos ($a$ y $b$) del intervalo.
# 
# Ya conocéis, de bachillerato, los problemas en los que hay que buscar el máximo y el mínimo absoluto de una función (continua) en determinado intervalo cerrado y acotado. 
# Suelen disfrazarse con un texto más o menos imaginativo (*Cortamos una hoja cuadrada de cartón de forma que [...]*). Aquí tenéis 10 ejemplos (de diferentes tipos), para que vayáis practicando:
# https://existelimite.blogspot.com/search/label/M%C3%A1ximos%20y%20m%C3%ADnimos.

# **Teorema de Rolle.**
# Sea una aplicación $f : [a,b] \longrightarrow \mathbb{R}$, continua en $[a,b]$ y derivable en $(a,b)$.  Si $f(a) = f(b)$, entonces existe un punto $\xi \in (a,b)$ tal que:
# \begin{equation*}
# f^{\prime} (\xi) = 0 \, .
# \end{equation*}
# ![Teorema de Rolle](./rolle.png)
# 
# **Teorema de Cauchy, o del valor medio generalizado.**
# Sean dos aplicaciones $f, g : [a,b] \rightarrow \mathbb{R}$ continuas en $[a,b]$ y derivables en $(a,b)$.  Entonces existe un punto $\xi \in (a,b)$ tal que:
# \begin{equation*}
# \left[ f(b) - f(a) \right] g' (\xi) = f' (\xi) \left[ g(b) - g(a) \right] \, .
# \end{equation*}
# 
# **Teorema de Lagrange, o del valor medio , o de los incrementos finitos.**
# Sea una aplicaci\'{o}n $f : [a,b] \longrightarrow \mathbb{R}$ continua en $[a,b]$ y derivable en $(a,b)$.  Entonces, existe un punto $\xi \in (a,b)$ tal que:
# \begin{equation*}
# f(b) - f(a) = f' (\xi) (b - a) \, .
# \end{equation*}
# ![Teorema de Lagrange](./lagrange.png)
# 

# ## Aplicaciones inmediatas de la derivación de funciones
# 
# Sea $f$ una función real derivable en $(a,b)$.
# - Si $f' (x) \geq 0$, $\forall x \in (a,b)$, entonces $f$ es monótona creciente.
# - Si $f' (x) \leq 0$, $\forall x \in (a,b)$, entonces $f$ es monótona decreciente.
# - Si $f' (x) = 0$, $\forall x \in (a,b)$, entonces $f$ es constante.
# - Si $f' (x) \neq 0$, $\forall x \in (a,b)$, entonces $f$ es inyectiva.
# 
# El signo de $f'$ puede utilizarse para determinar el carácter de máximo o mínimo de un punto estacionario: si $f$
# presenta en $a$ un máximo relativo y es continua en $(a - \delta , a + \delta)$, entonces
# \begin{equation*}
# \begin{cases}
# f' (x) > 0 , \quad \text{si } x < a \\
# f' (x) < 0 , \quad \text{si } x > a
# \end{cases}
# \end{equation*}
# y lo contrario si $f$ presenta un mínimo.
# 
# 

# In[ ]:




