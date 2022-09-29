#!/usr/bin/env python
# coding: utf-8

# # Boletín 2: Límites, continuidad, Lagrange y dicotomía

# 1. Calcula, si es posible,
#    
#     a. $\displaystyle{\lim_{x\rightarrow 0}{\frac{|2x-1|-|2x+1|}{x}}}$,
# 
#     b. $\displaystyle{\lim_{x\rightarrow 0}{\frac{\sqrt{x^2+4}-2}{x^2}}}$,
#     
#     c. $\displaystyle{\lim_{x\rightarrow 0}{\left (\frac{1}{x}-\frac{1}{|x|}\right)}}$.
# 

# 2. Calcula, si es posible, los siguientes límites:
#    
# $$
# \begin{array}{lllll}
# %\text{$(a)$ } \displaystyle{\lim_{x\rightarrow -\infty} \mathbf{e}^x}   &\qquad
# %\text{$(b)$ } \displaystyle{\lim_{x\rightarrow 0}       \mathbf{e}^x}   &\qquad
# %\text{$(c)$ } \displaystyle{\lim_{x\rightarrow +\infty} \mathbf{e}^x}   &\qquad
# \text{$a)$ } \displaystyle{\lim_{x\rightarrow -\infty} \sqrt[3]{x}}   & \qquad
#  \text{$b)$ } \displaystyle{\lim_{x\rightarrow +\infty} \sqrt{x}}  &\qquad
# \text{$c)$ } \displaystyle{\lim_{x\rightarrow 0^+}     \sqrt{x}}   &\qquad
# \text{$d)$ } \displaystyle{\lim_{x\rightarrow -\infty} \sqrt{x}}   \\
# \\
# \text{$e)$ } \displaystyle{\lim_{x\rightarrow +\infty} \dfrac{1}{\sqrt{x}}}  & \qquad
# \text{$f)$ } \displaystyle{\lim_{x\rightarrow 0^+}     \dfrac{1}{\sqrt{x}} }  &\qquad
# %\text{$j)$ } \displaystyle{\lim_{x\rightarrow +\infty} x^2}   &\qquad
# \text{$g)$ } \displaystyle{\lim_{x\rightarrow -\infty} x^2 }  &\qquad
# \text{$h)$ } \displaystyle{\lim_{x\rightarrow +\infty} \left( x^3 - 5x^2 + 8 \right)}
# \end{array}
# $$

# 3. El valor, en euros, de un coche $x$ años después de su adquisición (nuevo) viene dado por la función
#    
#     $$
#     v(x)=2000+\frac{60000}{4^{0.25 x}}.
#     $$
#     
#     Se llama *valor residual* del coche a su valor límite cuando el número de años aumenta indefinidamente.
#     
#       a. ¿Cuál fue el precio de compra del vehículo nuevo?
# 
#       b. ¿Cuál será su valor residual?
# 
#       c. ¿Al cabo de cuántos años diferirá su valor en menos de 1000 euros del valor residual? 
#     

# 4. Dibuja, con `Sympy` la gráfica de la curva $y=\sqrt{x^2+1}-x$. 
#    
#     Comprueba, con lápiz y papel y comprobando los resultados en el ordenador, si esta gráfica tiene alguna asíntota y, en caso afirmativo, obtén sus ecuaciones.

# 5. Calcula las asíntotas de las siguientes funciones:
# 
#     a. $\displaystyle{v_{1}(x)= \frac{3x^2-2}{4x^2 +1}}$,
# 
#     b. $\displaystyle{h(t)= \frac{t^2+2}{t -2}}$,
# 
#     c. $\displaystyle{v_{2}(x)= \frac{3x^2-2}{4x^2 -1}}$,   
# 
#     d. $\displaystyle{f(x)=x^\frac{|x|}{x} + \frac{1}{x}}$.

# 6. Considera la  función $f$, dada por $f(x) = \ln(x)$.
#    
#     a. ¿Cuál es su dominio? ¿Cuál es su imagen?
# 
#     b. ¿Cuánto valen $\displaystyle{\lim_{x\rightarrow  +\infty}\ln(x)} \,\,$ y $\displaystyle{\lim_{x\rightarrow 0^+}\ln (x)}$?
# 
#     c. ¿Existe $\displaystyle{\lim_{x\rightarrow -\infty}\ln(x)}$? ¿Por qué?
# 
#     d. ¿Posee $f$ alguna asíntota vertical? En caso afirmativo, ¿cuál es su ecuación?
# 
#     e. Dibuja la gráfica de $f$.
# 
#     f. Utilizando la relación entre la gráfica de una función y la de su inversa, esboza la gráfica de $g(x)=\mathbf{e}^x$. 
#     De la observación de esta gráfica deduce la existencia de una asíntota horizontal.

# 7. Vamos a repasar la función arco-tangente:
# 
#     a. ¿Cuál es el dominio de la función $f(x)=\arctan(x)$? ¿Y su imagen?
# 
#     b. ¿Es cierto que $\dfrac{1}{\tan(x)} = \arctan(x)$? ¿Por qué?
# 
#     c. ¿Cuáles son los ángulos cuya tangente vale $1$?
# 
#     d. ¿Es correcto decir que $\arctan (1)=\dfrac{\pi}{4}+k\pi$, $\,k \in \mathbb{Z}$? ¿Por qué?
# 

# 8. Si la longitud de un animal $t$ días después de su nacimiento es 
# 
#     $$
#     \ell(t)= \frac{300}{1+9\left(0.8\right)^t}
#     $$  
#     ¿cuánto midió al nacer? Obtén una cota superior de su tamaño máximo. 

# 9. Elige la opción correcta: 
#     
#     Para aproximar el valor de la solución de la ecuación  $x^3+2=0$ con un error menor que $0.30$ usando el algoritmo de dicotomía en el intervalo $[-2,\,2]$:
# 
#     a. debemos realizar cinco iteraciones y las cuatro primeras son $x_1=0$, $x_2=-1$, $x_3=-3/2$ y $x_4=-5/4$
# 
#     b. debemos realizar cinco iteraciones y las cuatro primeras son $x_1=0$, $x_2=-1$,  $x_3=-3/2$ y $ x_4=-7/4$
# 
#     c. debemos realizar cuatro iteraciones y las tres primeras son $x_1=0$, $x_2=-1$ y $x_3=-3/2$
# 
#     d. debemos realizar cuatro iteraciones y las tres primeras son $x_1=0$, $x_2=-1$ y $x_3=-5/4$

# 10. ¿Dónde es continua la función $f$ dada por $f(x)=\displaystyle{\frac{e^x+\ln(2x)}{x^2-3}}?$

# 11. Elige la opción correcta:
# 
#     La función $f : \mathbb{R} \longrightarrow \mathbb{R}$ dada por:
# 
#     $$
#     f(x) =
#     \begin{cases}
#     \sqrt{{x}^{2}-1} \,\,\,\,  \qquad\,  \text{  si  } x \in (-\infty,-1] \\
#                 {x}^{2}+2x+1 \qquad    \text{si } x \in (-1,10] \\
#                 \frac{121}{10}x   \qquad\, \, \, \, \qquad   \text{     si   } x \in (10,+\infty)
#     \end{cases}
#     $$
# 
#     a. No es continua en $x=-1$
# 
#     b. Es continua en $(-\infty,\infty)$
# 
#     c. No es continua en $x=10$
# 
#     d. No es continua en $x=0$
# 

# 12. Estudia la continuidad en $x=0$ de la función $f : \mathbb{R} \longrightarrow \mathbb{R}$ dada por:
# 
#     $$
#     f(x) =
#     \begin{cases}
#     x\mathbf{e}^{-x} \,  \qquad\,\quad  \text{si } x < 0 \\
#                 1 \qquad \qquad \,\,\,\,\,\,   \text{si } x = 0 \\
#                 \sqrt{x^2+1}   \qquad   \text{si } x > 0
#     \end{cases}
#     $$
# 

# 13. Si $a>1$ estudia la continuidad de la función $f : \mathbb{R} \longrightarrow \mathbb{R}$ dada por:
# 
#     $$
#     f(x) =
#     \begin{cases}
#     {x}^{2} {\cos^2(\frac{1}{x})}   \qquad\,\quad  \text{si } x < 0 \\
#                 0 \qquad \qquad \,\,\,\,\,\,\,\,\quad   \text{     si } x = 0 \\
#             \dfrac{x {a}^{x}-x} {\sqrt{1+x}-1}  \qquad   \text{si } x > 0
#     \end{cases}
#     $$
