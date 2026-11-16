# Deber # 2 — Control Avanzado (EYAG 1030) — Transcripción fiel

Fuente: `b4d23afa-Deber_2_Control_Avanzado.pdf` (9 páginas, generado con LaTeX; texto y figuras nítidos).

Encabezado de todas las páginas: logo **ESPOL — Facultad de Ingeniería en Electricidad y Computación**, y logo **CONTROL AVANZADO EYAG 1030**.

Título: **Deber # 2 — 2do PAO 2026**

## Indicaciones generales

El documento **no contiene** indicaciones generales (ni fecha de entrega, ni formato, ni método exigido aparte de lo que pide cada inciso). Lo único "general" es:

- El único puntaje indicado en todo el deber es "(7 puntos)" en el inciso 1.a.
- Al final hay una sección "Respuestas a problemas selectos" (ejercicios 1, 2, 3, 4, 7, 8, 9, 10; **no hay** respuestas para 5 ni 6) y un "FORMULARIO".
- Todos los diagramas están dibujados directamente en el dominio z (R(z), C(z), bloques en z). **En ningún diagrama aparecen muestreadores ni retenedores (ZOH)**; no hay ninguna G(s) en los enunciados. El ZOH solo aparece en el formulario.

Convención usada abajo para describir diagramas: "sumador" = círculo de suma; se indica el signo con que entra cada señal.

---

## Ejercicio 1

Para el sistema mostrado considere T = 0.1 seg y K > 0.

**Diagrama (lazo simple, realimentación unitaria negativa):**
R(z) entra con signo **+** a un sumador. La salida del sumador pasa, en cascada y en este orden, por:

1. una ganancia (triángulo) **K**,
2. un bloque **1 + z^{-1}**,
3. un bloque **0.1 / (z^2 − 0.2z − 0.03)**,

y la salida de este último es C(z). Desde C(z) (punto de toma a la salida) sale una realimentación directa (unitaria, sin bloque) que entra al sumador con signo **−**.

a) Encuentre la función de transferencia pulso del sistema C(z)/R(z), y su respectivo polinomio característico P(z) en términos de K. *(7 puntos)*
b) Construya el arreglo de Jury indicando claramente el valor de cada coeficiente.
c) Presente los intervalos resultantes de las TRES primeras condiciones según el criterio de Jury, y la inecuación derivada de la cuarta condición de Jury (NO LA RESUELVA).
d) Si K=1, determine si el sistema es estable o no.
e) Si K=10, determine si el sistema es estable o no.

## Ejercicio 2

Para el sistema mostrado considere T = 0.05 seg. y K > 0.

**Diagrama (lazo simple con bloque en la realimentación):**
R(z) entra con signo **+** a un sumador. La salida del sumador pasa en cascada por:

1. una ganancia (triángulo) **K**,
2. un bloque **1 / ((z + 0.2)(z − 0.5))**,

cuya salida es C(z). Desde C(z) se toma la señal que pasa por un bloque de realimentación **1/z** y entra al sumador con signo **−**.

a) Encuentre la función de transferencia pulso del sistema C(z)/R(z), y su respectivo polinomio característico P(z) en términos de K.
b) Construya el arreglo de Jury indicando claramente el valor de cada coeficiente.
c) Presente cada una de las inecuaciones derivadas del criterio de Jury. Encuentre los intervalos de K resultantes para cada condición.
d) ¿Cuál es el rango de valores de K para que el sistema sea estable?

## Ejercicio 3

Para el sistema mostrado considere T = 0.2 seg y M > 0.

**Diagrama (dos ramas en paralelo en el camino directo + realimentación con bloque):**
R(z) entra con signo **+** al primer sumador. La salida del primer sumador llega a un punto de bifurcación del que salen dos ramas en paralelo:

- rama superior: bloque **1 / (z − 0.4)**, cuya salida entra al segundo sumador con signo **−** (entra por arriba);
- rama inferior (línea principal): bloque **1 / (z − 0.6)**, cuya salida entra al segundo sumador con signo **+**.

La salida del segundo sumador pasa por una ganancia (triángulo) **2.5**, cuya salida es C(z). Desde C(z) se toma la señal que pasa por el bloque de realimentación **M / (z − 0.2)** y entra al primer sumador con signo **−**.

a) Encuentre la función de transferencia pulso del sistema C(z)/R(z), y su respectivo polinomio característico P(z) en términos de M.
b) Construya el arreglo de Jury indicando claramente el valor de cada coeficiente.
c) Presente los intervalos resultantes de las TRES primeras condiciones según el criterio de Jury.
d) Presente la inecuación derivada de la cuarta condición de Jury y el respectivo intervalo resultante.
e) Utilizando la información anterior, encuentre el intervalo de valores de M que permita que el sistema sea estable.

## Ejercicio 4

Para el sistema mostrado considere T = 0.01 seg y K > 0.

**Diagrama (lazo interno + lazo externo unitario):**
R(z) entra con signo **+** al primer sumador (externo). La salida del primer sumador entra con signo **+** al segundo sumador (interno). La salida del segundo sumador pasa por el bloque **G1(z) = 0.4 / (z + 0.4)**. A la salida de G1(z) hay un punto de toma (antes de K):

- **Lazo interno:** desde ese punto de toma la señal pasa por **H(z) = 0.5 / (z + 0.1)** y entra al segundo sumador con signo **−**.

Después del punto de toma, la señal sigue por una ganancia (triángulo) **K** y luego por el bloque **G2(z) = 5 / (z − 0.3)**, cuya salida es C(z).

- **Lazo externo:** desde C(z) sale una realimentación directa (unitaria, sin bloque) que entra al primer sumador con signo **−**.

a) Encuentre la función de transferencia pulso del sistema C(z)/R(z), y su respectivo polinomio característico P(z) en términos de K.
b) Construya el arreglo de Jury indicando claramente el valor de cada coeficiente.
c) Presente los intervalos resultantes de las TRES primeras condiciones según el criterio de Jury.
d) Presente la inecuación derivada de la cuarta condición de Jury y el respectivo intervalo resultante.
e) Utilizando la información anterior, encuentre el intervalo de valores de K que permita que el sistema sea estable.

## Ejercicio 5

Para los siguientes sistemas con realimentación unitaria y ganancia de lazo abierto:

i) G(z) = 0.4(z + 0.2) / ((z − 1)(z − 0.1))
ii) G(z) = 0.5(z + 0.2) / ((z − 0.1)(z − 0.8))

encuentre :

a) Las constante de error de posición
b) Las constante de error de velocidad
c) El error en estado estable para una entrada de escalón unitario
d) El error en estado estable para una entrada de rampa unitaria.

(No se indica periodo de muestreo T en este ejercicio. No hay diagrama.)

## Ejercicio 6

Considere el sistema de control digital mostrado. Trace los lugares geométricos de las raíces conforme se varia la ganancia K desde 0 hasta ∞. Determine el valor crítico de la ganancia K para estabilidad. El periodo de muestreo es de 0.1 seg. es decir T = 0.1. ¿Qué valor de la ganancia K dará un factor de amortiguamiento relativo de los polos en lazo cerrado igual a 0.5? Con la ganancia K definida para obtener ζ = 0.5, determine la frecuencia natural amortiguada ω_d y el número de muestras por ciclo de la oscilación senoidal amortiguada.

**Diagrama (lazo simple, realimentación unitaria negativa):**
R(z) entra a un sumador (sin signo dibujado en esa entrada; se entiende +). La salida del sumador pasa por un único bloque **K(z + 1) / ((z − 1)(z − 0.6065))**, cuya salida es C(z). Desde la salida sale una realimentación directa (unitaria) que entra al sumador con signo **−**.

(Sin incisos con letras; todo va en el párrafo.)

## Ejercicio 7

Para el sistema mostrado con entrada de escalón unitario, se desea diseñar un controlador discreto con tiempo de muestreo de T = 0.2 seg, que sea muestreado al menos 10 veces por oscilación, y que presente un tiempo de estabilización de 0.8 seg.

**Diagrama (lazo simple, realimentación unitaria negativa):**
R(z) entra con signo **+** a un sumador. La salida del sumador pasa en cascada por:

1. bloque **G_D(z)** (rotulado "Controlador"),
2. bloque **0.02(z + 0.7) / (z^2 − 1.2z + 0.27)**,

cuya salida es C(z). Desde C(z) sale una realimentación directa (unitaria) que entra al sumador con signo **−**.

a) Encuentre los valores de ζ, ω_n, y tiempo de pico requeridos.
b) Encuentre la localización deseada de los polos dominantes en el plano-z y verifique si con simple ajuste de ganancia (G_D(z) = K) se satisfacen los requerimientos.
c) Si se necesita un controlador, la prioridad es la reducción del tiempo de estabilización y debe escoger entre las estructuras PD o PI ¿Cuál estructura permite cumplir las condiciones requeridas? Justifique claramente su respuesta.
d) Con la estructura elegida en el literal anterior, encuentre la función de transferencia pulso del compensador G_D(z) que cumpla con los requerimientos.

## Ejercicio 8

Suponga que el sistema mostrado trabaja con T = 0.1 seg, y está sometido a una entrada de escalón unitario.

**Diagrama (lazo simple, realimentación unitaria negativa):**
R(z) entra con signo **+** a un sumador. La salida del sumador pasa en cascada por:

1. bloque **K_P + K_I / (1 − z^{-1}) + K_D (1 − z^{-1})** (rotulado "Control PID"),
2. bloque **(1/200) / (z^2 − z + 0.16)**,

cuya salida es C(z). Desde C(z) sale una realimentación directa (unitaria) que entra al sumador con signo **−**.

a) Considere que el control PID mostrado es solo proporcional con K_P = 40. Calcule el sobrenivel porcentual, tiempo de estabilización, número de muestras por oscilación y error en estado estacionario.
b) Si se desea mantener el mismo sobrenivel porcentual del literal anterior con un nuevo tiempo de estabilización de 0.5 seg, y usando únicamente control Proporcional Derivativo, Calcule los nuevos valores de las constantes K_P, K_I y K_D.
c) Encuentre el valor del error estacionario para el literal anterior. Sin hacer ningún cálculo, indique como se podría mejorar el error estacionario de este sistema.

## Ejercicio 9

Suponga que el sistema mostrado trabaja con T = 0.08 seg, y está sometido a una entrada de escalón unitario. Se desea que el sistema opere con un sobrenivel porcentual del 2.4 % y un tiempo de pico de 0.4 seg.

**Diagrama (controlador de dos ramas en paralelo + planta, realimentación unitaria negativa):**
R(z) entra con signo **+** al primer sumador. La salida del primer sumador (el error) llega a un punto de bifurcación del que salen dos ramas en paralelo:

- rama superior: bloque **K_1 (1 − z^{-1})**, cuya salida entra al segundo sumador con signo **+** (entra por arriba);
- rama inferior (línea principal): bloque **K_2**, cuya salida entra al segundo sumador con signo **+**.

La salida del segundo sumador pasa por el bloque de planta **(z + 0.5) / (4z^2 − 4.8z + 1.28)**, cuya salida es C(z). Desde C(z) sale una realimentación directa (unitaria) que entra al primer sumador con signo **−**.

a) Si la ganancias en el diagrama son K_1 = 0 y K_2 = 0.38, calcule el sobrenivel porcentual y el tiempo de pico del sistema en lazo cerrado. ¿Cumple lo especificado? Comente su respuesta.
b) Para las condiciones de diseño requeridas obtenga los valores de ζ, ω_n, número de muestras por oscilación, y la localización deseada de los polos de lazo cerrado en el plano-z.
c) Encuentre los valores de K_1 y K_2 que permitan cumplir los requerimientos de diseño. ¿Qué tipo de controlador es el implementado y qué característica de desempeño ayudó a mejorar?

## Ejercicio 10

El sistema mostrado trabaja con T = 0.1 seg, y está sometido a una entrada de escalón unitario. Se desea que el sistema no tenga error en estado estacionario, opere con un tiempo de estabilización de 0.5 seg, y presente al menos 8 muestras por oscilación.

**Diagrama (lazo simple, realimentación unitaria negativa):**
R(z) entra con signo **+** a un sumador. La salida del sumador pasa en cascada, en este orden, por:

1. bloque **G_D(z)** (rotulado "Control Digital"),
2. bloque **1 / (100(z − 1))** (rotulado "Integrador"),
3. bloque **(z + 3) / (z^2 + 0.5z − 0.06)** (rotulado "Planta"),

cuya salida es C(z). Desde C(z) sale una realimentación directa (unitaria) que entra al sumador con signo **−**.

a) A partir de los requerimientos, encuentre los valores de ζ, y ω_n.
b) Encuentre la localización deseada de los polos de lazo cerrado en el plano-z, y determine si se cumplen los requerimientos con un ajuste simple de ganancia (G_D(z) = K).
c) Si se necesita un controlador, y considerando los requerimientos de diseño y los bloques presentes en el diagrama, ¿Cuál estructura de control (PD o PI) usaría para este sistema? Justifique claramente su respuesta.
d) Con la estructura de control seleccionada, presente la función de transferencia pulso G_D(z) y las correspondientes ganancias del controlador K_P y (K_D o K_I) según corresponda.

---

## Respuestas a problemas selectos (transcritas tal cual del PDF)

**1.**
a. C(z)/R(z) = 0.1K(z+1) / (z^3 − 0.2z^2 + (0.1K − 0.03)z + 0.1K)
   P(z) : z^3 − 0.2z^2 + (0.1K − 0.03)z + 0.1K = 0.
b.

| Fila | z^0 | z^1 | z^2 | z^3 |
|---|---|---|---|---|
| 1 | 0.1K | 0.1K − 0.03 | −0.2 | 1 |
| 2 | 1 | −0.2 | 0.1K − 0.03 | 0.1K |
| 3 | b_2 | b_1 | b_0 | |

   b_2 = 0.01K^2 − 1
   b_1 = 0.01K^2 − 0.003K + 0.2
   b_0 = 0.03 − 0.12K
c. 1) 0 < K < 10
   2) K > 0
   3) −1.17 < 0
   4) |0.01K^2 − 1| > |0.03 − 0.12K|
d. Si es estable.
e. No es estable.

**2.**
a. C(z)/R(z = zK / (z^3 − 0.3z^2 − 0.1z + K)   [sic: falta el paréntesis de cierre en "R(z" en el original]
   P(z) : z^3 − 0.3z^2 − 0.1z + K = 0
b. Arreglo (matriz, sin encabezados):

| | | | |
|---|---|---|---|
| K | −0.1 | −0.3 | 1 |
| 1 | −0.3 | −0.1 | K |
| K^2 − 1 | −0.1K + 0.3 | −0.3K + 0.1 | |

c. 1) |K| < 1,   0 < K < 1
   2) K > −0.6,   K > 0
   3) K < 1.2,   0 < K < 1.2
   4) |K^2 − 1| > |0.1 − 0.3K|,   K < −1.2095 ∨ −0.8015 < K < 0.9095 ∨ K > 1.1105
d. 0 < K < 0.9095

**3.**
a. C(z)/R(z) = 0.5(z − 0.2) / (z^3 − 1.2z^2 + 0.44z + 0.5M − 0.048)
   P(z) : z^3 − 1.2z^2 + 0.44z + 0.5M − 0.048 = 0
b. Arreglo:

| | | | |
|---|---|---|---|
| 0.5M − 0.048 | 0.44 | −1.2 | 1 |
| 1 | −1.2 | 0.44 | 0.5M − 0.048 |
| 0.25M^2 − 0.048M − 0.9977 | 0.22M + 1.1789 | −0.6M − 0.3824 | |

c. 1) 0 < M < 2.096
   2) M > 0
   3) M < 5.376
d. |0.25M^2 − 0.048M − 0.9977| > |−0.6M − 0.3824|;   0 < M < 0.8143 ∨ M > 3.3309
e. 0 < M < 0.8143

**4.**
a. C(z)/R(z) = 0.2K(z + 0.1) / (z^3 + 0.2z^2 + (0.09 + 2K)z + 0.2K − 0.072)
   P(z) : z^3 + 0.2z^2 + (0.09 + 2K)z + 0.2K − 0.072 = 0
b. Arreglo:

| | | | |
|---|---|---|---|
| 0.2K − 0.072 | 0.09 + 2K | 0.2 | 1 |
| 1 | 0.2 | 0.09 + 2K | 0.2K − 0.072 |
| 0.04K^2 − 0.0288K − 0.9948 | 0.4K^2 − 0.126K − 0.20648 | −1.96K − 0.1044 | |

c. 1) 0 < K < 5.36
   2) K > 0
   3) K > 0
d. |0.04K^2 − 0.0288K − 0.9948| > |−1.96K − 0.1044|;   0 ≤ K < 0.4567 ∨ K > 50.2667
e. 0 < K < 0.4567

(No hay respuestas para los ejercicios 5 y 6.)

**7.**
a. ζ = 0.8467,   ω_n = 5.9055 rad/seg,   t_p = 1 seg
b. z = 0.2976 ± j0.2162
c. Se debe usar un control PD.
d. G_D(z) = 11.5032 (z − 0.3152)/z

**8.**
a. %OS = 6.4568%,   T_s = 0.783 seg.   nmo = 10.727,   e_ss = 0.444
b. K_P = 39.8958,   K_I = 0,   K_D = 18.1176
c. e_ss = 0.4451

**9.**
a. %OS = 2.4548%   T_p = 0.5925 seg.   No cumple.
b. ζ = 0.7648   ω_n = 12.1906 rad/seg   nmo = 10   z = 0.3837 ± j0.2788
c. K_1 = 0.3263   K_2 = 0.679   Contro PD mejora velocidad.   [sic: "Contro"]

**10.**
a. ζ = 0.7136   ω_n = 11.2109 rad/seg
b. z = 0.3177 ± j0.3177   No se cumplen requerimientos con ajuste simple
c. Se selecciona un control PD.
d. G_D(z) = 11.9426 (z − 0.3135)/z   K_P = 8.1986, K_D = 3.744

("nmo" = número de muestras por oscilación; la abreviatura no se define en el PDF.)

---

## FORMULARIO (página 9, transcrito tal cual)

1. Retenedor de orden cero (ZOH)

   G_h(s) = (1 − e^{−Ts}) / s

2. Controlador PID digital en forma posicional

   G_D(z) = K_P + K_I / (1 − z^{-1}) + K_D (1 − z^{-1})

3. Indices de desempeño

   t_p = π / (ω_n √(1 − ζ^2))
   %OS = 100 e^{ −ζπ / √(1 − ζ^2) }
   ζ = − ln(%OS/100) / √( π^2 + ln^2(%OS/100) )
   t_s = 4 / (ζ ω_n)

4. Plano-s a plano-z

   |z| = e^{−T ζ ω_n}
   ∠z = T ω_n √(1 − ζ^2)
   ω_s / ω_d = 2π / ∠z

5. Tabla de transformadas z mas utilizadas

| X(s) | x(t) | x(k) o x(kT) | X(z) |
|---|---|---|---|
| – | – | δ(k) | 1 |
| – | – | δ(k − n) | z^{−n} |
| 1/s | u(t) | u(k) | 1 / (1 − z^{-1}) |
| 1/(s + a) | e^{−at} | e^{−akT} | 1 / (1 − e^{−aT} z^{-1}) |
| 1/s^2 | t | kT | T z^{-1} / (1 − z^{-1})^2 |
| 2/s^3 | t^2 | (kT)^2 | T^2 z^{-1} (1 + z^{-1}) / (1 − z^{-1})^3 |
| ω/(s^2 + ω^2) | sin(ωt) | sin(ωkT) | z^{-1} sin ωT / (1 − 2 z^{-1} cos ωT + z^{-2}) |
| s/(s^2 + ω^2) | cos(ωt) | cos(ωkT) | (1 − z^{-1} cos ωT) / (1 − 2 z^{-1} cos ωT + z^{-2}) |
| ω/((s + a)^2 + ω^2) | e^{−at} sin(ωt) | e^{−akT} sin(ωkT) | e^{−aT} z^{-1} sin ωT / (1 − 2 e^{−aT} z^{-1} cos ωT + e^{−2aT} z^{-2}) |
| (s + a)/((s + a)^2 + ω^2) | e^{−at} cos(ωt) | e^{−akT} cos(ωkT) | (1 − e^{−aT} z^{-1} cos ωT) / (1 − 2 e^{−aT} z^{-1} cos ωT + e^{−2aT} z^{-2}) |
| – | – | a^k | 1 / (1 − a z^{-1}) |
| – | – | k a^{k−1} | z^{-1} / (1 − a z^{-1})^2 |
| – | – | k^2 a^{k−1} | z^{-1} (1 + a z^{-1}) / (1 − a z^{-1})^3 |

---

## Puntos dudosos / observaciones del transcriptor

Nada es ilegible: el PDF es vectorial y todas las cifras se verificaron contra la capa de texto y/o contra recortes ampliados de las figuras (los diagramas de los ejercicios 3, 4, 9 y 10 son imágenes sin capa de texto y se leyeron ampliados). Observaciones, sin corregir el original:

1. **Ej. 4, respuesta a.:** el numerador impreso es "0.2K(z+0.1)". [dudoso: parece inconsistente con el propio denominador impreso, cuyo término dependiente de K es 2Kz + 0.2K = 2K(z+0.1); posible errata del solucionario. El denominador/P(z) sí es coherente con el diagrama.] Se transcribió tal como aparece.
2. **Ej. 6, diagrama:** la entrada R(z) al sumador no lleva signo dibujado (solo aparece el "−" de la realimentación); se asume "+".
3. **Ej. 5:** no se da periodo de muestreo T (hace falta para la constante de error de velocidad); el enunciado no lo especifica.
4. **Ej. 1 a 4 y 6 a 10:** se da T pero los diagramas ya están en z, sin muestreadores ni ZOH.
5. **Ej. 2, respuesta a.:** "C(z)/R(z" sin paréntesis de cierre (errata tipográfica del original).
6. **Ej. 9, respuesta c.:** "Contro PD" (errata del original por "Control PD").
7. **Ej. 4, respuesta d.:** el intervalo aparece como "0 ≤ K < 0.4567" (con ≤), mientras que en e. aparece "0 < K < 0.4567"; así está en el original.
8. **Ej. 1, respuesta c.3:** aparece literalmente "−1.17 < 0" (una desigualdad numérica, no un intervalo de K); así está en el original.
9. **Ej. 8, inciso b):** pide "únicamente control Proporcional Derivativo" pero solicita K_P, K_I y K_D; así está en el original (la respuesta da K_I = 0).
10. No hay indicaciones de entrega, fecha ni formato en el PDF.
