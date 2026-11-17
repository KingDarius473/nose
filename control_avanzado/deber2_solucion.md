# Deber # 2 — Control Avanzado (EYAG 1030) — Solución completa

Todos los resultados se verificaron numéricamente con Python (sympy / numpy / scipy). Al final de cada ejercicio se indica la comparación con las "respuestas a problemas selectos" del profesor, y al final del documento hay una tabla resumen y la lista de discrepancias.

## Convenciones usadas (las mismas del profesor y del formulario)

**Criterio de Jury (orden 3).** Para $P(z)=a_3z^3+a_2z^2+a_1z+a_0$ con $a_3>0$:

| Fila | $z^0$ | $z^1$ | $z^2$ | $z^3$ |
|---|---|---|---|---|
| 1 | $a_0$ | $a_1$ | $a_2$ | $a_3$ |
| 2 | $a_3$ | $a_2$ | $a_1$ | $a_0$ |
| 3 | $b_2$ | $b_1$ | $b_0$ | |

$$b_2=\begin{vmatrix}a_0&a_3\\a_3&a_0\end{vmatrix}=a_0^2-a_3^2,\qquad b_1=\begin{vmatrix}a_0&a_2\\a_3&a_1\end{vmatrix}=a_0a_1-a_3a_2,\qquad b_0=\begin{vmatrix}a_0&a_1\\a_3&a_2\end{vmatrix}=a_0a_2-a_3a_1$$

Condiciones de estabilidad (en el orden que usa el profesor):

1. $|a_0|<a_3$
2. $P(1)>0$
3. $P(-1)<0$ (porque $n=3$ es impar)
4. $|b_2|>|b_0|$

**Formulario:** $t_p=\dfrac{\pi}{\omega_n\sqrt{1-\zeta^2}}$, $\%OS=100\,e^{-\zeta\pi/\sqrt{1-\zeta^2}}$, $t_s=\dfrac{4}{\zeta\omega_n}$, $|z|=e^{-T\zeta\omega_n}$, $\angle z=T\omega_n\sqrt{1-\zeta^2}=T\omega_d$, muestras por oscilación $=\dfrac{\omega_s}{\omega_d}=\dfrac{2\pi}{\angle z}$.

**Controladores (forma posicional del formulario):**

$$\text{PD: } G_D(z)=K_P+K_D(1-z^{-1})=\frac{(K_P+K_D)z-K_D}{z}=K\,\frac{z-a}{z},\quad K=K_P+K_D,\ a=\frac{K_D}{K_P+K_D}\ \Rightarrow\ K_D=Ka,\ K_P=K(1-a)$$

$$\text{PI: } G_D(z)=K_P+\frac{K_I}{1-z^{-1}}=\frac{(K_P+K_I)z-K_P}{z-1}=K\,\frac{z-a}{z-1},\quad a=\frac{K_P}{K_P+K_I}\in(0,1)$$

---

## Ejercicio 1 ($T=0.1$ s, $K>0$)

### a) Función de transferencia pulso y polinomio característico

Trayectoria directa (los tres bloques en cascada):

$$G(z)=K\,(1+z^{-1})\,\frac{0.1}{z^2-0.2z-0.03}=K\,\frac{z+1}{z}\cdot\frac{0.1}{z^2-0.2z-0.03}=\frac{0.1K(z+1)}{z^3-0.2z^2-0.03z}$$

Realimentación unitaria negativa:

$$\frac{C(z)}{R(z)}=\frac{G}{1+G}=\frac{0.1K(z+1)}{z^3-0.2z^2-0.03z+0.1Kz+0.1K}$$

$$\boxed{\frac{C(z)}{R(z)}=\frac{0.1K(z+1)}{z^3-0.2z^2+(0.1K-0.03)z+0.1K}}\qquad \boxed{P(z)=z^3-0.2z^2+(0.1K-0.03)z+0.1K=0}$$

### b) Arreglo de Jury

$a_3=1,\ a_2=-0.2,\ a_1=0.1K-0.03,\ a_0=0.1K$.

| Fila | $z^0$ | $z^1$ | $z^2$ | $z^3$ |
|---|---|---|---|---|
| 1 | $0.1K$ | $0.1K-0.03$ | $-0.2$ | $1$ |
| 2 | $1$ | $-0.2$ | $0.1K-0.03$ | $0.1K$ |
| 3 | $b_2$ | $b_1$ | $b_0$ | |

$$b_2=(0.1K)^2-(1)^2=0.01K^2-1$$
$$b_1=(0.1K)(0.1K-0.03)-(1)(-0.2)=0.01K^2-0.003K+0.2$$
$$b_0=(0.1K)(-0.2)-(1)(0.1K-0.03)=-0.02K-0.1K+0.03=0.03-0.12K$$

### c) Condiciones de Jury

1. $|a_0|<a_3$: $|0.1K|<1\Rightarrow -10<K<10$; con $K>0$: $\boxed{0<K<10}$
2. $P(1)=1-0.2+0.1K-0.03+0.1K=0.77+0.2K>0\Rightarrow K>-3.85$; con $K>0$: $\boxed{K>0}$
3. $P(-1)=-1-0.2-(0.1K-0.03)+0.1K=-1.17<0$: $\boxed{-1.17<0}$, se cumple para todo $K$ (no restringe).
4. $|b_2|>|b_0|$: $\boxed{|0.01K^2-1|>|0.03-0.12K|}$ (no se resuelve, según el enunciado).

> Dato adicional (no pedido): resolviendo la cuarta condición queda $0<K<5.7898$, que es el rango real de estabilidad. Verificado calculando raíces: en $K=5$ el polo mayor tiene $|z|=0.946$ y en $K=6$, $|z|=1.014$.

### d) $K=1$

$P(z)=z^3-0.2z^2+0.07z+0.1$

1. $|0.1|<1$ ✓
2. $P(1)=0.97>0$ ✓
3. $P(-1)=-1.17<0$ ✓
4. $b_2=0.01-1=-0.99$, $b_0=0.03-0.12=-0.09$: $|-0.99|>|-0.09|$ ✓

Se cumplen las cuatro condiciones: **el sistema es estable**. (Raíces: $z=0.2818\pm j0.4422$, $z=-0.3637$; todas con $|z|<1$, la mayor $|z|=0.524$.)

### e) $K=10$

$P(z)=z^3-0.2z^2+0.97z+1$

1. $|a_0|=|1|<1$ ✗ (no se cumple, es igualdad)
4. $b_2=0.01(100)-1=0$, $b_0=0.03-1.2=-1.17$: $|0|>|-1.17|$ ✗

**El sistema no es estable.** (Raíces: $z=0.4271\pm j1.1603$ con $|z|=1.236>1$, y $z=-0.6541$.)

**Comparación con el profesor:** coincide en todo (a, b, c, d, e).

---

## Ejercicio 2 ($T=0.05$ s, $K>0$)

### a) Función de transferencia pulso

$$G(z)=\frac{K}{(z+0.2)(z-0.5)},\qquad H(z)=\frac1z$$

$(z+0.2)(z-0.5)=z^2-0.3z-0.1$.

$$\frac{C(z)}{R(z)}=\frac{G}{1+GH}=\frac{\dfrac{K}{z^2-0.3z-0.1}}{1+\dfrac{K}{z(z^2-0.3z-0.1)}}=\frac{Kz}{z(z^2-0.3z-0.1)+K}$$

$$\boxed{\frac{C(z)}{R(z)}=\frac{Kz}{z^3-0.3z^2-0.1z+K}}\qquad\boxed{P(z)=z^3-0.3z^2-0.1z+K=0}$$

### b) Arreglo de Jury

$a_3=1,\ a_2=-0.3,\ a_1=-0.1,\ a_0=K$.

| Fila | $z^0$ | $z^1$ | $z^2$ | $z^3$ |
|---|---|---|---|---|
| 1 | $K$ | $-0.1$ | $-0.3$ | $1$ |
| 2 | $1$ | $-0.3$ | $-0.1$ | $K$ |
| 3 | $K^2-1$ | $-0.1K+0.3$ | $-0.3K+0.1$ | |

$$b_2=K\cdot K-1\cdot1=K^2-1$$
$$b_1=K(-0.1)-(1)(-0.3)=-0.1K+0.3$$
$$b_0=K(-0.3)-(1)(-0.1)=-0.3K+0.1$$

### c) Inecuaciones e intervalos

1. $|a_0|<a_3$: $|K|<1\Rightarrow-1<K<1$; con $K>0$: $\boxed{0<K<1}$
2. $P(1)=1-0.3-0.1+K=0.6+K>0\Rightarrow K>-0.6$; con $K>0$: $\boxed{K>0}$
3. $P(-1)=-1-0.3+0.1+K=K-1.2<0\Rightarrow K<1.2$; con $K>0$: $\boxed{0<K<1.2}$
4. $|b_2|>|b_0|$: $|K^2-1|>|0.1-0.3K|$.

   Elevando al cuadrado: $b_2^2-b_0^2>0\Rightarrow(b_2-b_0)(b_2+b_0)>0$:

   $$b_2-b_0=K^2+0.3K-1.1=0\Rightarrow K=\frac{-0.3\pm\sqrt{0.09+4.4}}{2}=\frac{-0.3\pm2.1190}{2}\Rightarrow K=0.9095,\ K=-1.2095$$
   $$b_2+b_0=K^2-0.3K-0.9=0\Rightarrow K=\frac{0.3\pm\sqrt{0.09+3.6}}{2}=\frac{0.3\pm1.9209}{2}\Rightarrow K=1.1105,\ K=-0.8105$$

   Tabla de signos del producto $(K+1.2095)(K-0.9095)(K+0.8105)(K-1.1105)$:

   | Intervalo | $K<-1.2095$ | $(-1.2095,-0.8105)$ | $(-0.8105,0.9095)$ | $(0.9095,1.1105)$ | $K>1.1105$ |
   |---|---|---|---|---|---|
   | Signo | $+$ | $-$ | $+$ | $-$ | $+$ |

   $$\boxed{K<-1.2095\ \lor\ -0.8105<K<0.9095\ \lor\ K>1.1105}$$

   (comprobación: $K=0$: $|-1|>|0.1|$ ✓; $K=1$: $|0|>|-0.2|$ ✗; $K=2$: $|3|>|-0.5|$ ✓)

### d) Rango de estabilidad

Intersección de $0<K<1$, $K>0$, $0<K<1.2$ y la condición 4:

$$\boxed{0<K<0.9095}$$

**Verificación numérica:** $K=0.90\Rightarrow\max|z|=0.9966$ (estable); $K=0.9095\Rightarrow\max|z|=1.00001$ (límite); $K=0.92\Rightarrow\max|z|=1.0038$ (inestable). Un barrido de $K$ da el cambio de estabilidad en $K=0.90948$.

**Comparación con el profesor:** coincide en a, b, c.1–c.3 y d. En c.4 el profesor imprime "$-0.8015<K<0.9095$"; el valor correcto es $-0.8105$ (raíz de $K^2-0.3K-0.9=0$). Es una **errata de dígitos transpuestos** del solucionario que no afecta la respuesta final (está en la zona $K<0$).

---

## Ejercicio 3 ($T=0.2$ s, $M>0$)

### a) Función de transferencia pulso

Las dos ramas en paralelo (la inferior suma, la superior resta) y luego la ganancia 2.5:

$$G(z)=2.5\left[\frac{1}{z-0.6}-\frac{1}{z-0.4}\right]=2.5\,\frac{(z-0.4)-(z-0.6)}{(z-0.6)(z-0.4)}=\frac{2.5(0.2)}{(z-0.6)(z-0.4)}=\frac{0.5}{z^2-z+0.24}$$

$$H(z)=\frac{M}{z-0.2}$$

$$\frac{C(z)}{R(z)}=\frac{G}{1+GH}=\frac{0.5(z-0.2)}{(z^2-z+0.24)(z-0.2)+0.5M}$$

$(z^2-z+0.24)(z-0.2)=z^3-0.2z^2-z^2+0.2z+0.24z-0.048=z^3-1.2z^2+0.44z-0.048$

$$\boxed{\frac{C(z)}{R(z)}=\frac{0.5(z-0.2)}{z^3-1.2z^2+0.44z+0.5M-0.048}}\qquad\boxed{P(z)=z^3-1.2z^2+0.44z+0.5M-0.048=0}$$

### b) Arreglo de Jury

$a_3=1,\ a_2=-1.2,\ a_1=0.44,\ a_0=0.5M-0.048$.

| Fila | $z^0$ | $z^1$ | $z^2$ | $z^3$ |
|---|---|---|---|---|
| 1 | $0.5M-0.048$ | $0.44$ | $-1.2$ | $1$ |
| 2 | $1$ | $-1.2$ | $0.44$ | $0.5M-0.048$ |
| 3 | $0.25M^2-0.048M-0.9977$ | $0.22M+1.1789$ | $-0.6M-0.3824$ | |

$$b_2=(0.5M-0.048)^2-1=0.25M^2-0.048M+0.002304-1=0.25M^2-0.048M-0.997696$$
$$b_1=(0.5M-0.048)(0.44)-(1)(-1.2)=0.22M-0.02112+1.2=0.22M+1.17888$$
$$b_0=(0.5M-0.048)(-1.2)-(1)(0.44)=-0.6M+0.0576-0.44=-0.6M-0.3824$$

### c) Tres primeras condiciones

1. $|0.5M-0.048|<1\Rightarrow-1<0.5M-0.048<1\Rightarrow-1.904<M<2.096$; con $M>0$: $\boxed{0<M<2.096}$
2. $P(1)=1-1.2+0.44+0.5M-0.048=0.192+0.5M>0\Rightarrow M>-0.384$; con $M>0$: $\boxed{M>0}$
3. $P(-1)=-1-1.2-0.44+0.5M-0.048=0.5M-2.688<0\Rightarrow\boxed{M<5.376}$

### d) Cuarta condición

$$\boxed{|0.25M^2-0.048M-0.9977|>|-0.6M-0.3824|}$$

$(b_2-b_0)(b_2+b_0)>0$:

$$b_2-b_0=0.25M^2+0.552M-0.615296=0\Rightarrow M=\frac{-0.552\pm\sqrt{0.304704+0.615296}}{0.5}=\frac{-0.552\pm0.959166}{0.5}\Rightarrow M=0.8143,\ M=-3.0223$$
$$b_2+b_0=0.25M^2-0.648M-1.380096=0\Rightarrow M=\frac{0.648\pm\sqrt{0.419904+1.380096}}{0.5}=\frac{0.648\pm1.341641}{0.5}\Rightarrow M=3.9793,\ M=-1.3873$$

| Intervalo | $M<-3.0223$ | $(-3.0223,-1.3873)$ | $(-1.3873,0.8143)$ | $(0.8143,3.9793)$ | $M>3.9793$ |
|---|---|---|---|---|---|
| Signo | $+$ | $-$ | $+$ | $-$ | $+$ |

Con $M>0$:

$$\boxed{0<M<0.8143\ \lor\ M>3.9793}$$

(comprobación: $M=3.5$: $b_2=1.8968$, $b_0=-2.4824$, $|1.8968|>|2.4824|$ ✗; $M=4$: $b_2=2.8103$, $b_0=-2.7824$ ✓)

### e) Rango de estabilidad

Intersección de $0<M<2.096$, $M>0$, $M<5.376$ y ($0<M<0.8143\ \lor\ M>3.9793$):

$$\boxed{0<M<0.8143}$$

**Verificación numérica:** $M=0.80\Rightarrow\max|z|=0.9959$; $M=0.8143\Rightarrow\max|z|=0.99999$; $M=0.83\Rightarrow\max|z|=1.0044$; $M=4\Rightarrow\max|z|=1.497$ (inestable, lo descarta la condición 1). Barrido: cambio en $M=0.81434$.

**Comparación con el profesor:** coincide en a, b, c, e y en el primer tramo de d. En d el profesor imprime "$M>3.3309$" y aquí se obtiene $M>3.9793$. Se revisó el cálculo (los coeficientes $b_2$ y $b_0$ son idénticos a los del profesor; con ellos $b_2+b_0=0.25M^2-0.648M-1.3801$, cuya raíz positiva es $3.9793$; además en $M=3.5$ la inecuación NO se cumple). Se concluye que **$3.3309$ es una errata del solucionario**. No afecta la respuesta final porque ese tramo queda fuera de $M<2.096$.

---

## Ejercicio 4 ($T=0.01$ s, $K>0$)

### a) Función de transferencia pulso

**Lazo interno** (realimentación negativa de $G_1$ con $H$):

$$G_{int}(z)=\frac{G_1}{1+G_1H}=\frac{\dfrac{0.4}{z+0.4}}{1+\dfrac{0.4(0.5)}{(z+0.4)(z+0.1)}}=\frac{0.4(z+0.1)}{(z+0.4)(z+0.1)+0.2}=\frac{0.4(z+0.1)}{z^2+0.5z+0.24}$$

**Trayectoria directa del lazo externo:**

$$G(z)=G_{int}\cdot K\cdot G_2=\frac{0.4(z+0.1)}{z^2+0.5z+0.24}\cdot K\cdot\frac{5}{z-0.3}=\frac{2K(z+0.1)}{(z^2+0.5z+0.24)(z-0.3)}$$

$(z^2+0.5z+0.24)(z-0.3)=z^3-0.3z^2+0.5z^2-0.15z+0.24z-0.072=z^3+0.2z^2+0.09z-0.072$

**Lazo externo unitario:**

$$\frac{C(z)}{R(z)}=\frac{G}{1+G}=\frac{2K(z+0.1)}{z^3+0.2z^2+0.09z-0.072+2Kz+0.2K}$$

$$\boxed{\frac{C(z)}{R(z)}=\frac{2K(z+0.1)}{z^3+0.2z^2+(0.09+2K)z+0.2K-0.072}}\qquad\boxed{P(z)=z^3+0.2z^2+(0.09+2K)z+0.2K-0.072=0}$$

### b) Arreglo de Jury

$a_3=1,\ a_2=0.2,\ a_1=0.09+2K,\ a_0=0.2K-0.072$.

| Fila | $z^0$ | $z^1$ | $z^2$ | $z^3$ |
|---|---|---|---|---|
| 1 | $0.2K-0.072$ | $0.09+2K$ | $0.2$ | $1$ |
| 2 | $1$ | $0.2$ | $0.09+2K$ | $0.2K-0.072$ |
| 3 | $0.04K^2-0.0288K-0.9948$ | $0.4K^2-0.126K-0.20648$ | $-1.96K-0.1044$ | |

$$b_2=(0.2K-0.072)^2-1=0.04K^2-0.0288K+0.005184-1=0.04K^2-0.0288K-0.994816$$
$$b_1=(0.2K-0.072)(0.09+2K)-(1)(0.2)=0.4K^2+0.018K-0.144K-0.00648-0.2=0.4K^2-0.126K-0.20648$$
$$b_0=(0.2K-0.072)(0.2)-(1)(0.09+2K)=0.04K-0.0144-0.09-2K=-1.96K-0.1044$$

### c) Tres primeras condiciones

1. $|0.2K-0.072|<1\Rightarrow-0.928<0.2K<1.072\Rightarrow-4.64<K<5.36$; con $K>0$: $\boxed{0<K<5.36}$
2. $P(1)=1+0.2+0.09+2K+0.2K-0.072=1.218+2.2K>0\Rightarrow K>-0.5536$; con $K>0$: $\boxed{K>0}$
3. $P(-1)=-1+0.2-(0.09+2K)+0.2K-0.072=-0.962-1.8K<0\Rightarrow K>-0.5344$; con $K>0$: $\boxed{K>0}$

### d) Cuarta condición

$$\boxed{|0.04K^2-0.0288K-0.9948|>|-1.96K-0.1044|}$$

$(b_2-b_0)(b_2+b_0)>0$:

$$b_2-b_0=0.04K^2+1.9312K-0.890416=0\Rightarrow K=\frac{-1.9312\pm\sqrt{3.729533+0.142467}}{0.08}=\frac{-1.9312\pm1.967740}{0.08}\Rightarrow K=0.4567,\ K=-48.7367$$
$$b_2+b_0=0.04K^2-1.9888K-1.099216=0\Rightarrow K=\frac{1.9888\pm\sqrt{3.955325+0.175875}}{0.08}=\frac{1.9888\pm2.032535}{0.08}\Rightarrow K=50.2667,\ K=-0.5467$$

| Intervalo | $K<-48.7367$ | $(-48.7367,-0.5467)$ | $(-0.5467,0.4567)$ | $(0.4567,50.2667)$ | $K>50.2667$ |
|---|---|---|---|---|---|
| Signo | $+$ | $-$ | $+$ | $-$ | $+$ |

Con $K>0$:

$$\boxed{0<K<0.4567\ \lor\ K>50.2667}$$

### e) Rango de estabilidad

Intersección con $0<K<5.36$:

$$\boxed{0<K<0.4567}$$

**Verificación numérica:** $K=0.45\Rightarrow\max|z|=0.9933$; $K=0.4567\Rightarrow\max|z|=0.99995$; $K=0.46\Rightarrow\max|z|=1.0032$; $K=1\Rightarrow\max|z|=1.443$. Barrido: cambio en $K\approx0.4567$.

**Comparación con el profesor:** coincide en $P(z)$, b, c, d y e. **Discrepancia en el numerador de a:** el profesor imprime $0.2K(z+0.1)$ y lo correcto es $\mathbf{2K(z+0.1)}$. Es una errata del solucionario: (i) $0.4\times K\times5=2K$; (ii) el propio denominador del profesor contiene $2Kz+0.2K=2K(z+0.1)$, que es exactamente el numerador de $G(z)$ sumado al denominador de lazo abierto, así que el numerador de $C/R$ debe ser ese mismo término; (iii) sympy da $C/R=\dfrac{2K(z+0.1)}{\dots}$. Probablemente el profesor escribió $0.2K(z+0.1)$ por confusión con el término independiente $0.2K$. No afecta el análisis de estabilidad.

---

## Ejercicio 5 (realimentación unitaria)

**Suposición:** el enunciado no da el periodo de muestreo $T$. La constante de error de posición no depende de $T$; la de velocidad sí, así que se deja en función de $T$ (y se da además el valor para $T=1$ s). Definiciones (Ogata):

$$K_p=\lim_{z\to1}G(z),\qquad K_v=\lim_{z\to1}\frac{(1-z^{-1})G(z)}{T}=\lim_{z\to1}\frac{(z-1)G(z)}{Tz}$$

$$e_{ss}^{\text{escalón}}=\frac{1}{1+K_p},\qquad e_{ss}^{\text{rampa}}=\frac{1}{K_v}$$

Estas fórmulas salen del teorema del valor final, $e_{ss}=\lim_{z\to1}(1-z^{-1})\dfrac{R(z)}{1+G(z)}$, con $R(z)=\dfrac{1}{1-z^{-1}}$ (escalón) y $R(z)=\dfrac{Tz^{-1}}{(1-z^{-1})^2}$ (rampa), y son válidas solo si el lazo cerrado es estable (se comprueba abajo).

> Si en clase se definió $K_v$ sin dividir para $T$ (es decir $K_v'=\lim(1-z^{-1})G(z)$), entonces $K_v'=K_vT$ y $e_{ss}^{\text{rampa}}=T/K_v'$; el error en estado estable resultante es el mismo.

### Sistema i) $G(z)=\dfrac{0.4(z+0.2)}{(z-1)(z-0.1)}$ — tipo 1 (un polo en $z=1$)

Estabilidad del lazo cerrado: $(z-1)(z-0.1)+0.4(z+0.2)=z^2-0.7z+0.18=0\Rightarrow z=0.35\pm j0.2398$, $|z|=0.424<1$ ✓ estable.

a) $K_p=\lim_{z\to1}\dfrac{0.4(z+0.2)}{(z-1)(z-0.1)}=\boxed{\infty}$

b) $K_v=\dfrac1T\lim_{z\to1}\dfrac{z-1}{z}\cdot\dfrac{0.4(z+0.2)}{(z-1)(z-0.1)}=\dfrac1T\cdot\dfrac{0.4(1.2)}{(1)(0.9)}=\dfrac{0.48}{0.9T}=\boxed{\dfrac{0.5333}{T}}$ (con $T=1$ s: $K_v=0.5333$)

c) $e_{ss}^{\text{escalón}}=\dfrac{1}{1+\infty}=\boxed{0}$

d) $e_{ss}^{\text{rampa}}=\dfrac1{K_v}=\boxed{1.875\,T}$ (con $T=1$ s: $1.875$)

### Sistema ii) $G(z)=\dfrac{0.5(z+0.2)}{(z-0.1)(z-0.8)}$ — tipo 0 (sin polos en $z=1$)

Estabilidad del lazo cerrado: $(z-0.1)(z-0.8)+0.5(z+0.2)=z^2-0.4z+0.18=0\Rightarrow z=0.2\pm j0.3742$, $|z|=0.424<1$ ✓ estable.

a) $K_p=\dfrac{0.5(1.2)}{(0.9)(0.2)}=\dfrac{0.6}{0.18}=\boxed{3.3333}$

b) $K_v=\dfrac1T\lim_{z\to1}\dfrac{(z-1)}{z}G(z)=\dfrac1T(0)(3.3333)=\boxed{0}$

c) $e_{ss}^{\text{escalón}}=\dfrac{1}{1+3.3333}=\dfrac{3}{13}=\boxed{0.2308}$

d) $e_{ss}^{\text{rampa}}=\dfrac{1}{0}=\boxed{\infty}$

**Doble verificación:** (1) simbólica con sympy aplicando el teorema del valor final directamente a $E(z)$: da $0$, $15T/8$, $3/13$, $\infty$. (2) simulación de la ecuación en diferencias del lazo cerrado con $T=1$: i) error ante escalón $\to0$, error ante rampa $\to1.875$; ii) error ante escalón $\to0.230769$, error ante rampa creciente sin cota.

---

## Ejercicio 6 ($T=0.1$ s)

$$G(z)=\frac{K(z+1)}{(z-1)(z-0.6065)},\qquad 1+G(z)=0\Rightarrow z^2+(K-1.6065)z+(0.6065+K)=0$$

### Lugar geométrico de las raíces

1. **Polos de lazo abierto:** $z=1$, $z=0.6065$. **Cero:** $z=-1$ (y un cero en infinito). Hay 2 ramas.
2. **Tramos sobre el eje real** (número impar de polos+ceros reales a la derecha): $0.6065\le z\le1$ y $-\infty<z\le-1$.
3. **Asíntota:** $n-m=1\Rightarrow$ una sola, a $180°$ (eje real negativo).
4. **Puntos de ruptura:** $K=-\dfrac{(z-1)(z-0.6065)}{z+1}=-\dfrac{z^2-1.6065z+0.6065}{z+1}$

   $$\frac{dK}{dz}=0\Rightarrow(2z-1.6065)(z+1)-(z^2-1.6065z+0.6065)=0\Rightarrow z^2+2z-2.213=0$$
   $$z=-1\pm\sqrt{1+2.213}=-1\pm1.7925\Rightarrow\boxed{z=0.7925}\ (\text{salida}),\qquad\boxed{z=-2.7925}\ (\text{llegada})$$

   Ganancias: en $z=0.7925$: $K=\dfrac{(0.2075)(0.1860)}{1.7925}=0.0215$; en $z=-2.7925$: $K=\dfrac{(3.7925)(3.3990)}{1.7925}=7.1915$.

5. **Parte compleja: es una circunferencia.** Con $z=x+jy$, la condición de ángulo $\angle(z+1)-\angle(z-1)-\angle(z-0.6065)=\pm180°$ conduce a

   $$(x+1)^2+y^2=(1+1)(1+0.6065)=3.213\Rightarrow\text{centro en el cero } z=-1,\ \text{radio}=\sqrt{3.213}=1.7925$$

   (pasa por los dos puntos de ruptura: $-1\pm1.7925$).

6. **Corte con el círculo unitario / ganancia crítica.** Para raíces complejas conjugadas el producto de raíces es $|z|^2=0.6065+K$. En el círculo unitario $|z|=1$:

   $$\boxed{K_{cr}=1-0.6065=0.3935}$$

   Con ese valor: $z^2-1.213z+1=0\Rightarrow z=0.6065\pm j0.7951$ ($|z|=1$, $\angle z=\pm52.66°=\pm0.9191$ rad, es decir oscilación sostenida de $\omega=0.9191/0.1=9.19$ rad/s).

   Confirmación con Jury (orden 2): $|a_0|<a_2\Rightarrow|0.6065+K|<1\Rightarrow K<0.3935$; $P(1)=2K>0\Rightarrow K>0$; $P(-1)=1-(K-1.6065)+0.6065+K=3.213>0$ ✓. **Estable para $0<K<0.3935$.**

**Descripción del trazado.** Las dos ramas nacen ($K=0$) en los polos $z=1$ y $z=0.6065$, se mueven una hacia la otra sobre el eje real y se encuentran en $z=0.7925$ ($K=0.0215$). Ahí salen del eje real a $\pm90°$ y recorren la circunferencia de centro $-1$ y radio $1.7925$, hacia la izquierda; cruzan el círculo unitario en $z=0.6065\pm j0.7951$ con $K=0.3935$ (a partir de ahí el sistema es inestable); siguen por la circunferencia, fuera del círculo unitario, hasta reencontrarse en el eje real en $z=-2.7925$ ($K=7.1915$). Luego una rama va hacia la derecha por el eje real hasta el cero $z=-1$ (llega cuando $K\to\infty$) y la otra va hacia $-\infty$. Puntos de apoyo calculados: $K=0.3\Rightarrow0.6533\pm j0.6927$; $K=0.5\Rightarrow0.5533\pm j0.8947$; $K=5\Rightarrow-1.6968\pm j1.6515$; $K=7\Rightarrow-2.6968\pm j0.5780$.

### Ganancia para $\zeta=0.5$

En el plano $z$ la curva de $\zeta$ constante es una espiral logarítmica. Con $\theta=\angle z=T\omega_d$:

$$|z|=e^{-T\zeta\omega_n}=e^{-\frac{\zeta}{\sqrt{1-\zeta^2}}\theta}=e^{-0.57735\,\theta}\qquad(\zeta=0.5)$$

Se busca el punto de la espiral que cumple la condición de ángulo (equivalentemente, que cae sobre la circunferencia: $|z|^2+2\,\mathrm{Re}(z)+1=3.213$). Por tanteo:

| $\theta$ (rad) | $\lvert z\rvert$ | $z$ | $\angle(z+1)$ | $\angle(z-1)$ | $\angle(z-0.6065)$ | Suma |
|---|---|---|---|---|---|---|
| 0.20 | 0.8909 | $0.8732+j0.1770$ | 5.40° | 125.62° | 33.57° | −153.79° |
| 0.30 | 0.8410 | $0.8034+j0.2485$ | 7.85° | 128.35° | 51.61° | −172.11° |
| 0.34 | 0.8218 | $0.7747+j0.2740$ | 8.78° | 129.42° | 58.46° | −179.10° |
| **0.3453** | **0.8193** | $\mathbf{0.7709+j0.2773}$ | 8.90° | 129.56° | 59.34° | **−180.00°** |
| 0.35 | 0.8170 | $0.7675+j0.2802$ | 9.01° | 129.69° | 60.12° | −180.80° |

$$\boxed{z=0.7709\pm j0.2773}\qquad(|z|=0.8193,\ \angle z=0.3453\text{ rad}=19.78°)$$

**Condición de magnitud:**

$$K=\frac{|z-1|\,|z-0.6065|}{|z+1|}=\frac{(0.35969)(0.32237)}{1.79248}=\boxed{0.0647}$$

Comprobación algebraica independiente: $K=|z|^2-0.6065=0.67119-0.6065=0.0647$ ✓ y $\mathrm{Re}(z)=\dfrac{1.6065-K}{2}=0.7709$ ✓. Además $0.0647<K_{cr}=0.3935$ (estable).

### Frecuencia natural amortiguada y muestras por ciclo

$$\omega_d=\frac{\angle z}{T}=\frac{0.3453}{0.1}=\boxed{3.453\ \text{rad/s}}\qquad\left(\omega_n=\frac{\omega_d}{\sqrt{1-\zeta^2}}=3.987\ \text{rad/s}\right)$$

$$\text{muestras por ciclo}=\frac{\omega_s}{\omega_d}=\frac{2\pi}{\angle z}=\frac{360°}{19.78°}=\boxed{18.2}$$

**Doble verificación:** (1) resolviendo numéricamente la condición de ángulo sobre la espiral (método de Brent): $\theta=0.345289$ rad, única solución en $0<\theta<\pi$. (2) con $K=0.064688$ las raíces de $z^2+(K-1.6065)z+0.6065+K$ son $0.77091\pm j0.27729$, y convirtiéndolas a plano $s$ con $s=\ln(z)/T$ se obtiene $\zeta=0.5000$, $\omega_n=3.9871$, $\omega_d=3.4529$. (3) $K_{cr}$: barrido de $K$ calculando raíces da estabilidad hasta $K=0.39346$.

---

## Ejercicio 7 ($T=0.2$ s, $\ge10$ muestras por oscilación, $t_s=0.8$ s)

Planta: $G_p(z)=\dfrac{0.02(z+0.7)}{z^2-1.2z+0.27}=\dfrac{0.02(z+0.7)}{(z-0.9)(z-0.3)}$

### a) $\zeta$, $\omega_n$, $t_p$

- Muestras por oscilación (se toma el límite, 10): $\dfrac{2\pi}{\angle z}=10\Rightarrow\angle z=0.6283\text{ rad}=36°\Rightarrow\omega_d=\dfrac{\angle z}{T}=\dfrac{0.6283}{0.2}=3.1416$ rad/s
- $t_s=\dfrac{4}{\zeta\omega_n}=0.8\Rightarrow\zeta\omega_n=5$
- $\omega_n=\sqrt{(\zeta\omega_n)^2+\omega_d^2}=\sqrt{25+9.8696}=\boxed{5.9050\ \text{rad/s}}$
- $\zeta=\dfrac{5}{5.9050}=\boxed{0.8467}$
- $t_p=\dfrac{\pi}{\omega_d}=\dfrac{\pi}{3.1416}=\boxed{1\ \text{s}}$

### b) Polos deseados y prueba con solo ganancia

$$|z|=e^{-T\zeta\omega_n}=e^{-0.2(5)}=e^{-1}=0.3679,\qquad\angle z=36°$$
$$\boxed{z_1=0.3679\angle\pm36°=0.2976\pm j0.2162}$$

Condición de ángulo con $G_D=K$, en $z_1=0.2976+j0.2162$:

| Factor | Valor | Ángulo | Magnitud |
|---|---|---|---|
| $z_1+0.7$ | $0.9976+j0.2162$ | $12.23°$ | $1.0208$ |
| $z_1-0.9$ | $-0.6024+j0.2162$ | $160.25°$ | $0.6400$ |
| $z_1-0.3$ | $-0.0024+j0.2162$ | $90.63°$ | $0.2162$ |

$$\angle G_p(z_1)=12.23°-160.25°-90.63°=-238.65°\ (\equiv121.35°)\ne\pm180°$$

**No se cumple la condición de ángulo: con simple ajuste de ganancia NO se satisfacen los requerimientos.** (El LGR con solo ganancia es una circunferencia centrada en $z=-0.7$ de radio $\sqrt{(1.6)(1.0)}=1.265$; el punto deseado está a $1.0208$ del cero, o sea dentro de la circunferencia, más cerca del origen que cualquier punto del lugar.)

### c) ¿PD o PI?

Falta ángulo: el controlador debe aportar $\phi=-180°-(-238.65°)=\mathbf{+58.65°}$ (adelanto).

- **PD:** $G_D=K\dfrac{z-a}{z}$ aporta $\angle(z_1-a)-\angle z_1$, que es **positivo** si $a>0$ (el cero está a la derecha del polo en el origen). Atrae el lugar de las raíces hacia el origen ⇒ polos con menor $|z|$ ⇒ respuesta más rápida, menor $t_s$.
- **PI:** $G_D=K\dfrac{z-a}{z-1}$ con $0<a<1$ aporta $\angle(z_1-a)-\angle(z_1-1)$, que es **siempre negativo** (el polo en $z=1$ está a la derecha del cero): p. ej. $-18.5°$ con $a=0.6$, $-2.6°$ con $a=0.9$. Solo atrasa; mejora el error estacionario pero empuja el lugar hacia el círculo unitario (más lento). No puede dar los $+58.65°$.

**Se debe usar un control PD** (la prioridad es reducir el tiempo de estabilización).

### d) Diseño del PD

$G_D(z)=K\dfrac{z-a}{z}$.

**Condición de ángulo:**
$$\angle(z_1-a)-\angle z_1=58.65°\Rightarrow\angle(z_1-a)=58.65°+36°=94.65°$$
$$\tan(94.65°)=\frac{0.2162}{0.2976-a}\Rightarrow a=0.2976-\frac{0.2162}{\tan94.65°}=0.2976+0.0176=\boxed{0.3152}$$

**Condición de magnitud:**
$$|G_p(z_1)|=\frac{0.02(1.0208)}{(0.6400)(0.2162)}=0.14751,\qquad|z_1-a|=|-0.0176+j0.2162|=0.21695$$
$$K=\frac{|z_1|}{|z_1-a|\,|G_p(z_1)|}=\frac{0.36788}{(0.21695)(0.14751)}=\boxed{11.495}$$

$$\boxed{G_D(z)=11.495\,\frac{z-0.3152}{z}}\qquad K_D=Ka=3.624,\quad K_P=K-K_D=7.872$$

**Verificación numérica:** polos de lazo cerrado de $z(z-0.9)(z-0.3)+0.02K(z-a)(z+0.7)=0$: $z=0.29762\pm j0.21623$ (exactamente los deseados) y un tercer polo real en $z=0.3749$.

Observaciones: (1) el tercer polo ($0.375$) tiene magnitud similar a la de los polos deseados, así que estos no son estrictamente "dominantes"; la respuesta simulada al escalón es casi sin sobrepaso y se asienta en ≈4–5 muestras (0.8–1.0 s). (2) El sistema sigue siendo tipo 0: valor final $0.793$ ($e_{ss}=0.207$); el enunciado no pide corregirlo.

**Comparación con el profesor:** a, b y c coinciden ($\zeta=0.8467$, $\omega_n=5.9055$ vs. $5.9050$ aquí —diferencia de redondeo en el 4.º decimal—, $t_p=1$ s, $z=0.2976\pm j0.2162$, PD). En d el cero coincide ($0.3152$) y la ganancia difiere en el tercer dígito: profesor $11.5032$, aquí $11.4953$ (diferencia de 0.07 %, atribuible a redondeo de valores intermedios; con los valores del profesor los polos quedan en $0.2977\pm j0.2166$, prácticamente el mismo punto).

---

## Ejercicio 8 ($T=0.1$ s, escalón unitario)

Planta: $G_p(z)=\dfrac{1/200}{z^2-z+0.16}=\dfrac{0.005}{(z-0.8)(z-0.2)}$

### a) Solo proporcional, $K_P=40$

$$G(z)=\frac{40(0.005)}{z^2-z+0.16}=\frac{0.2}{z^2-z+0.16}\Rightarrow P(z)=z^2-z+0.36=0$$
$$z=\frac{1\pm\sqrt{1-1.44}}{2}=0.5\pm j0.3317$$
$$|z|=\sqrt{0.36}=0.6,\qquad\angle z=\tan^{-1}\frac{0.3317}{0.5}=33.557°=0.5857\text{ rad}$$

- $\zeta\omega_n=-\dfrac{\ln|z|}{T}=\dfrac{0.5108}{0.1}=5.1083$; $\omega_d=\dfrac{\angle z}{T}=5.8569$ rad/s
- $\omega_n=\sqrt{5.1083^2+5.8569^2}=7.7716$ rad/s; $\zeta=\dfrac{5.1083}{7.7716}=0.6573$
- $\%OS=100\,e^{-\zeta\pi/\sqrt{1-\zeta^2}}=100\,e^{-\pi(5.1083/5.8569)}=100\,e^{-2.7400}=\boxed{6.457\,\%}$
- $t_s=\dfrac{4}{\zeta\omega_n}=\dfrac{4}{5.1083}=\boxed{0.783\ \text{s}}$
- Muestras por oscilación $=\dfrac{2\pi}{0.5857}=\boxed{10.73}$
- $K_p=\lim_{z\to1}G(z)=\dfrac{0.2}{1-1+0.16}=1.25\Rightarrow e_{ss}=\dfrac{1}{1+1.25}=\boxed{0.444}$

### b) PD con el mismo %OS y $t_s=0.5$ s

Mismo sobrenivel ⇒ mismo $\zeta=0.6573$.

- $\zeta\omega_n=\dfrac{4}{0.5}=8\Rightarrow\omega_n=\dfrac{8}{0.6573}=12.171$ rad/s
- $\omega_d=\omega_n\sqrt{1-\zeta^2}=8\cdot\dfrac{5.8569}{5.1083}=9.1724$ rad/s
- $|z|=e^{-0.1(8)}=e^{-0.8}=0.4493$; $\angle z=T\omega_d=0.9172\text{ rad}=52.554°$ (6.85 muestras por oscilación)

$$z_1=0.4493\angle52.554°=0.2732+j0.3567$$

| Factor | Valor | Ángulo | Magnitud |
|---|---|---|---|
| $z_1-0.8$ | $-0.5268+j0.3567$ | $145.90°$ | $0.63622$ |
| $z_1-0.2$ | $0.0732+j0.3567$ | $78.40°$ | $0.36417$ |

$$\angle G_p(z_1)=-145.90°-78.40°=-224.30°\Rightarrow\text{el PD debe aportar }\phi=+44.30°$$

Con $G_D=K\dfrac{z-a}{z}$:
$$\angle(z_1-a)=44.30°+52.55°=96.85°\Rightarrow a=0.2732-\frac{0.3567}{\tan96.85°}=0.2732+0.0429=0.3161$$
$$|G_p(z_1)|=\frac{0.005}{(0.63622)(0.36417)}=0.021581,\qquad|z_1-a|=|-0.0429+j0.3567|=0.35930$$
$$K=\frac{|z_1|}{|z_1-a|\,|G_p(z_1)|}=\frac{0.44933}{(0.35930)(0.021581)}=57.949$$

$$K_D=Ka=57.949(0.3161)=\boxed{18.316},\qquad K_P=K-K_D=\boxed{39.633},\qquad\boxed{K_I=0}$$

$$G_D(z)=39.633+18.316(1-z^{-1})=57.949\,\frac{z-0.3161}{z}$$

**Verificación numérica:** polos de lazo cerrado de $z(z-0.8)(z-0.2)+0.005K(z-a)=0$: $z=0.27320\pm j0.35673$ (exactamente los deseados: $\zeta=0.6573$, $t_s=0.500$ s) y un tercer polo real en $z=0.4536$.

### c) Error estacionario

$$K_p=\lim_{z\to1}G_D(z)G_p(z)=K_P\cdot\frac{0.005}{0.16}=\frac{39.633}{32}=1.2385\Rightarrow e_{ss}=\frac{1}{1+1.2385}=\boxed{0.4467}$$

(el término derivativo $K_D(1-z^{-1})$ vale cero en $z=1$, no ayuda al error estacionario; por eso $e_{ss}$ prácticamente no cambia respecto al literal a).

**Cómo mejorarlo (sin cálculos):** agregando acción integral ($K_I\ne0$, es decir un PI o PID). El integrador pone un polo en $z=1$, el sistema pasa a tipo 1, $K_p\to\infty$ y el error ante escalón se hace cero. (Solo subir la ganancia proporcional lo reduce pero no lo elimina y deteriora el transitorio.)

**Comparación con el profesor:** a coincide en todo ($6.4568\,\%$, $0.783$ s, $10.727$, $0.444$). En b y c hay una **diferencia pequeña (≈1 %)**: profesor $K_P=39.8958$, $K_D=18.1176$, $e_{ss}=0.4451$; aquí $K_P=39.633$, $K_D=18.316$, $e_{ss}=0.4467$. Se revisó el diseño: con los valores obtenidos aquí los polos de lazo cerrado caen exactamente en el punto de diseño ($|z|=e^{-0.8}=0.4493$, $\angle z=52.55°$). Con los valores del profesor los polos quedan en $0.2768\pm j0.3554$ ($|z|=0.4505$, $\angle z=52.09°$, es decir $t_s=0.5016$ s y $\%OS=6.36\,\%$): cumplen la especificación solo aproximadamente. La diferencia es compatible con redondeo en pasos intermedios del profesor (por ejemplo, usar $\zeta\approx0.66$ desplaza los resultados en esa dirección), pero no se pudo reproducir exactamente su número. Ambos resultados son equivalentes para efectos prácticos; el método es el mismo.

---

## Ejercicio 9 ($T=0.08$ s; se desea $\%OS=2.4\,\%$, $t_p=0.4$ s)

Planta: $G_p(z)=\dfrac{z+0.5}{4z^2-4.8z+1.28}=\dfrac{0.25(z+0.5)}{(z-0.8)(z-0.4)}$

Controlador: $G_D(z)=K_2+K_1(1-z^{-1})$ (ramas en paralelo que se suman).

### a) $K_1=0$, $K_2=0.38$

$$P(z)=4z^2-4.8z+1.28+0.38(z+0.5)=4z^2-4.42z+1.47=0$$
$$z=\frac{4.42\pm\sqrt{19.5364-23.52}}{8}=\frac{4.42\pm j1.9959}{8}=0.5525\pm j0.2495$$
$$|z|=\sqrt{1.47/4}=0.6062,\qquad\angle z=\tan^{-1}\frac{0.2495}{0.5525}=24.302°=0.4242\text{ rad}$$

- $\zeta\omega_n=-\dfrac{\ln0.6062}{0.08}=6.2564$; $\omega_d=\dfrac{0.4242}{0.08}=5.3019$ rad/s
- $\omega_n=8.2008$ rad/s; $\zeta=0.7629$
- $\%OS=100\,e^{-\pi(6.2564/5.3019)}=\boxed{2.4546\,\%}$
- $t_p=\dfrac{\pi}{\omega_d}=\dfrac{\pi}{5.3019}=\boxed{0.5925\ \text{s}}$

**No cumple.** El sobrenivel está prácticamente en el valor pedido ($2.45\,\%\approx2.4\,\%$, apenas por encima), pero el tiempo de pico ($0.5925$ s) es mayor que el requerido ($0.4$ s): el sistema es demasiado lento. Con solo ganancia proporcional no se puede aumentar $\omega_d$ manteniendo $\zeta$ (subir $K_2$ acelera pero aumenta el sobrenivel); hace falta un controlador que aporte adelanto de fase.

### b) Requerimientos de diseño

$$\zeta=\frac{-\ln(0.024)}{\sqrt{\pi^2+\ln^2(0.024)}}=\frac{3.7297}{\sqrt{9.8696+13.9107}}=\frac{3.7297}{4.8765}=\boxed{0.7648}$$
$$t_p=\frac{\pi}{\omega_d}=0.4\Rightarrow\omega_d=7.8540\text{ rad/s}\Rightarrow\omega_n=\frac{\omega_d}{\sqrt{1-\zeta^2}}=\frac{7.8540}{0.6442}=\boxed{12.191\ \text{rad/s}}$$
$$\angle z=T\omega_d=0.08(7.8540)=0.6283\text{ rad}=36°\Rightarrow\text{muestras por oscilación}=\frac{2\pi}{0.6283}=\boxed{10}$$
$$|z|=e^{-T\zeta\omega_n}=e^{-0.08(9.3243)}=e^{-0.7459}=0.4743$$
$$\boxed{z_1=0.4743\angle\pm36°=0.3837\pm j0.2788}$$

### c) Cálculo de $K_1$ y $K_2$

$$G_D(z)=K_2+K_1(1-z^{-1})=\frac{(K_1+K_2)z-K_1}{z}=K\,\frac{z-a}{z},\qquad K=K_1+K_2,\ a=\frac{K_1}{K_1+K_2}$$

En $z_1=0.3837+j0.2788$:

| Factor | Valor | Ángulo | Magnitud |
|---|---|---|---|
| $z_1+0.5$ | $0.8837+j0.2788$ | $17.51°$ | $0.92664$ |
| $z_1-0.8$ | $-0.4163+j0.2788$ | $146.19°$ | $0.50102$ |
| $z_1-0.4$ | $-0.0163+j0.2788$ | $93.34°$ | $0.27926$ |

$$\angle G_p(z_1)=17.51°-146.19°-93.34°=-222.03°\Rightarrow\phi=+42.03°$$

**Ángulo:** $\angle(z_1-a)=42.03°+36°=78.03°\Rightarrow a=0.3837-\dfrac{0.2788}{\tan78.03°}=0.3837-0.0591=0.3246$

**Magnitud:**
$$|G_p(z_1)|=\frac{0.25(0.92664)}{(0.50102)(0.27926)}=1.65576,\qquad|z_1-a|=|0.0591+j0.2788|=0.28498$$
$$K=\frac{0.47429}{(0.28498)(1.65576)}=1.00516$$

$$K_1=Ka=1.00516(0.3246)=\boxed{0.3263},\qquad K_2=K-K_1=\boxed{0.6789}$$

**Tipo de controlador:** es un **PD** ($K_2=K_P$ proporcional y $K_1=K_D$ derivativo: $K_1(1-z^{-1})$). Ayudó a mejorar la **velocidad de respuesta**: redujo el tiempo de pico de $0.5925$ s a $0.4$ s (y el tiempo de estabilización de $0.64$ s a $0.43$ s) manteniendo el sobrenivel en $2.4\,\%$. (De paso, por la mayor ganancia proporcional, el error estacionario baja de $0.457$ a $0.320$, pero sigue siendo tipo 0.)

**Verificación numérica:** polos de lazo cerrado de $z(4z^2-4.8z+1.28)+K(z-a)(z+0.5)=0$: $z=0.38371\pm j0.27878$ (los deseados) y un tercer polo en $z=0.1813$ (más rápido, los complejos sí dominan).

**Comparación con el profesor:** coincide en todo (a: $2.4548\,\%$ vs. $2.4546\,\%$ aquí, diferencia en el 4.º decimal por redondeo; $0.5925$ s; no cumple. b: $0.7648$, $12.1906$, $10$, $0.3837\pm j0.2788$. c: $K_1=0.3263$, $K_2=0.679$, PD mejora velocidad).

---

## Ejercicio 10 ($T=0.1$ s; $e_{ss}=0$, $t_s=0.5$ s, $\ge8$ muestras por oscilación)

Lazo abierto sin controlador: $\dfrac{1}{100(z-1)}\cdot\dfrac{z+3}{z^2+0.5z-0.06}=\dfrac{z+3}{100(z-1)(z+0.6)(z-0.1)}$

### a) $\zeta$ y $\omega_n$

- $t_s=\dfrac{4}{\zeta\omega_n}=0.5\Rightarrow\zeta\omega_n=8$
- 8 muestras por oscilación (límite): $\angle z=\dfrac{2\pi}{8}=0.7854\text{ rad}=45°\Rightarrow\omega_d=\dfrac{0.7854}{0.1}=7.8540$ rad/s
- $\omega_n=\sqrt{8^2+7.8540^2}=\sqrt{64+61.685}=\boxed{11.211\ \text{rad/s}}$
- $\zeta=\dfrac{8}{11.211}=\boxed{0.7136}$

### b) Polos deseados y prueba con solo ganancia

$$|z|=e^{-0.1(8)}=e^{-0.8}=0.4493,\quad\angle z=45°\Rightarrow\boxed{z_1=0.3177\pm j0.3177}$$

| Factor | Valor | Ángulo | Magnitud |
|---|---|---|---|
| $z_1+3$ | $3.3177+j0.3177$ | $5.47°$ | $3.33290$ |
| $z_1-1$ | $-0.6823+j0.3177$ | $155.03°$ | $0.75263$ |
| $z_1+0.6$ | $0.9177+j0.3177$ | $19.10°$ | $0.97117$ |
| $z_1-0.1$ | $0.2177+j0.3177$ | $55.58°$ | $0.38516$ |

$$\angle G(z_1)=5.47°-155.03°-19.10°-55.58°=-224.23°\ne\pm180°$$

**No se cumple la condición de ángulo: no se cumplen los requerimientos con ajuste simple de ganancia.** (Por ejemplo, con $K=10$ los polos complejos están en $0.6255\pm j0.2969$ y con $K=20$ en $0.6732\pm j0.5714$: el lugar nunca pasa cerca de $0.3177\pm j0.3177$.)

### c) ¿PD o PI?

**Se selecciona un control PD.** Justificación:

1. El requisito de error estacionario nulo ante escalón **ya está cubierto** por el bloque "Integrador" $\dfrac{1}{100(z-1)}$ del diagrama: el lazo es tipo 1, $K_p=\infty$, $e_{ss}=0$. No hace falta la acción integral de un PI.
2. Lo que falta es ángulo: el controlador debe aportar $\phi=-180°+224.23°=+44.23°$ (adelanto) para llevar los polos al punto deseado, que está más cerca del origen (respuesta más rápida). Un PD $K\dfrac{z-a}{z}$ aporta ángulo positivo.
3. Un PI $K\dfrac{z-a}{z-1}$ solo aporta ángulo negativo (p. ej. $-23.4°$ con $a=0.6$; $-3.7°$ con $a=0.9$), añadiría un segundo polo en $z=1$ y haría el sistema más lento/menos estable: no puede cumplir $t_s$.

### d) Diseño del PD

$G_D(z)=K\dfrac{z-a}{z}$.

**Ángulo:** $\angle(z_1-a)=44.23°+45°=89.23°\Rightarrow a=0.3177-\dfrac{0.3177}{\tan89.23°}=0.3177-0.0042=\boxed{0.3135}$

**Magnitud:**
$$|G(z_1)|=\frac{3.33290}{100(0.75263)(0.97117)(0.38516)}=0.118386,\qquad|z_1-a|=|0.0042+j0.3177|=0.31775$$
$$K=\frac{|z_1|}{|z_1-a|\,|G(z_1)|}=\frac{0.44933}{(0.31775)(0.118386)}=\boxed{11.945}$$

$$\boxed{G_D(z)=11.945\,\frac{z-0.3135}{z}}\qquad K_D=Ka=\boxed{3.744},\qquad K_P=K-K_D=\boxed{8.200}$$

**Verificación numérica:** polos de lazo cerrado de $100z(z-1)(z+0.6)(z-0.1)+K(z-a)(z+3)=0$: $z=0.31772\pm j0.31772$ (los deseados), $z=0.6813$ y $z=-0.8167$; todos dentro del círculo unitario (estable). La respuesta simulada al escalón tiende a $1.0000$ ($e_{ss}=0$ ✓).

Observación: los otros dos polos de lazo cerrado ($0.681$ y $-0.817$) tienen mayor magnitud que el par diseñado, así que el par complejo no es estrictamente dominante y el transitorio real es más lento que el $t_s=0.5$ s nominal; el diseño por ubicación de polos pedido solo garantiza la posición del par complejo.

**Comparación con el profesor:** coincide (a: $0.7136$, $11.2109$; b: $0.3177\pm j0.3177$, no se cumple; c: PD; d: profesor $11.9426\dfrac{z-0.3135}{z}$, $K_P=8.1986$, $K_D=3.744$; aquí $11.9447$, $0.3135$, $K_P=8.2003$, $K_D=3.7444$ — diferencias de 0.02 % por redondeo: usando el polo redondeado $0.3177+j0.3177$ se obtiene $K=11.9436$, $K_P=8.1996$).

---

## Tabla resumen de respuestas finales

| Ej. | Respuesta final | ¿Coincide con el profesor? |
|---|---|---|
| 1 | $\dfrac{C}{R}=\dfrac{0.1K(z+1)}{z^3-0.2z^2+(0.1K-0.03)z+0.1K}$; $b_2=0.01K^2-1$, $b_1=0.01K^2-0.003K+0.2$, $b_0=0.03-0.12K$; cond.: $0<K<10$, $K>0$, $-1.17<0$, $\lvert0.01K^2-1\rvert>\lvert0.03-0.12K\rvert$; $K=1$ estable; $K=10$ inestable | Sí |
| 2 | $\dfrac{C}{R}=\dfrac{Kz}{z^3-0.3z^2-0.1z+K}$; fila 3: $K^2-1$, $-0.1K+0.3$, $-0.3K+0.1$; estable para $0<K<0.9095$ | Sí (errata menor del profesor en c.4: $-0.8015$ debe ser $-0.8105$) |
| 3 | $\dfrac{C}{R}=\dfrac{0.5(z-0.2)}{z^3-1.2z^2+0.44z+0.5M-0.048}$; cond. 4: $0<M<0.8143\lor M>3.9793$; estable para $0<M<0.8143$ | Sí en el resultado final (errata del profesor en d: $3.3309$ debe ser $3.9793$) |
| 4 | $\dfrac{C}{R}=\dfrac{2K(z+0.1)}{z^3+0.2z^2+(0.09+2K)z+0.2K-0.072}$; cond. 4: $0<K<0.4567\lor K>50.2667$; estable para $0<K<0.4567$ | Sí, salvo el numerador (errata del profesor: $0.2K$ debe ser $2K$) |
| 5 i | $K_p=\infty$; $K_v=0.5333/T$; $e_{ss}$ escalón $=0$; $e_{ss}$ rampa $=1.875T$ | Sin respuesta del profesor |
| 5 ii | $K_p=3.3333$; $K_v=0$; $e_{ss}$ escalón $=0.2308$; $e_{ss}$ rampa $=\infty$ | Sin respuesta del profesor |
| 6 | Rupturas $z=0.7925$ ($K=0.0215$) y $z=-2.7925$ ($K=7.1915$); circunferencia centro $-1$, radio $1.7925$; $K_{cr}=0.3935$ (corte en $0.6065\pm j0.7951$); $\zeta=0.5$: $K=0.0647$, polos $0.7709\pm j0.2773$, $\omega_d=3.453$ rad/s, $18.2$ muestras/ciclo | Sin respuesta del profesor |
| 7 | $\zeta=0.8467$, $\omega_n=5.905$ rad/s, $t_p=1$ s; $z=0.2976\pm j0.2162$; solo ganancia no cumple; PD; $G_D=11.495\dfrac{z-0.3152}{z}$ ($K_P=7.872$, $K_D=3.624$) | Sí (ganancia $11.495$ vs. $11.5032$: redondeo, 0.07 %) |
| 8 | a) $\%OS=6.457\,\%$, $t_s=0.783$ s, $10.73$ muestras, $e_{ss}=0.444$; b) $K_P=39.633$, $K_I=0$, $K_D=18.316$; c) $e_{ss}=0.4467$; se mejora con acción integral | a) Sí; b) y c) difieren ≈1 % ($39.8958$, $18.1176$, $0.4451$) |
| 9 | a) $\%OS=2.4546\,\%$, $t_p=0.5925$ s, no cumple; b) $\zeta=0.7648$, $\omega_n=12.191$, 10 muestras, $z=0.3837\pm j0.2788$; c) $K_1=0.3263$, $K_2=0.6789$, PD, mejora la velocidad | Sí |
| 10 | $\zeta=0.7136$, $\omega_n=11.211$; $z=0.3177\pm j0.3177$; solo ganancia no cumple; PD; $G_D=11.945\dfrac{z-0.3135}{z}$, $K_P=8.200$, $K_D=3.744$ | Sí (redondeo, 0.02 %) |

## Discrepancias con el solucionario del profesor

1. **Ej. 4.a (errata segura):** numerador $0.2K(z+0.1)$ → debe ser $2K(z+0.1)$.
2. **Ej. 3.d (errata segura):** segundo tramo "$M>3.3309$" → debe ser $M>3.9793$. No cambia la respuesta final.
3. **Ej. 2.c.4 (errata segura, dígitos transpuestos):** "$-0.8015$" → debe ser $-0.8105$. No cambia la respuesta final.
4. **Ej. 8.b y 8.c (diferencia ≈1 %, origen no determinado):** aquí $K_P=39.633$, $K_D=18.316$, $e_{ss}=0.4467$; profesor $39.8958$, $18.1176$, $0.4451$. Los valores de este documento ubican los polos exactamente en el punto de diseño; los del profesor, muy cerca. Probable redondeo intermedio del profesor.
5. **Ej. 7.d y 10.d:** diferencias en el tercer/cuarto dígito de la ganancia, por redondeo.

## Scripts de verificación

En `/tmp/claude-0/-home-user-nose/466a75a5-1a05-5569-8d0a-98b6bad5e656/scratchpad/solver/`: `jury.py` (ej. 1–4: álgebra de bloques simbólica, arreglo de Jury, intervalos y barrido de raíces), `diseno.py` (ej. 5–10: límites, valor final, simulación, LGR, condición de ángulo/magnitud, polos de lazo cerrado), `ej6_tabla.py` (tabla de tanteo del ej. 6) y `comparar_prof.py` (polos de lazo cerrado con los valores del profesor).
