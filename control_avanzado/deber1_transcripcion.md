# Deber 1 – Control Avanzado (EYAG 1030) – Transcripción

**Fuente:** `39fad4fb-Deber_1_Control_Avanzado_removed.pdf` (4 páginas, numeradas 7, 8, 9 y 10 en el pie; es un extracto de un documento mayor).
**Encabezado de cada página:** ESPOL – Facultad de Ingeniería en Electricidad y Computación – "CONTROL AVANZADO EYAG 1030".

**Contenido:** solo enunciados (Ejercicios 11, 12 y 13) más una página de plantillas del plano z. **El documento NO contiene soluciones resueltas** (ni manuscritas ni tipografiadas); las tablas están vacías.

Convenciones de esta transcripción:
- Las figuras se describen con palabras. Los valores numéricos de las etiquetas son textuales (verificados contra la capa de texto del PDF).
- `[dudoso: ...]` marca interpretaciones geométricas de las figuras que no son 100 % seguras.
- `[nota del transcriptor: ...]` marca información que NO está en el documento.
- En todas las figuras del plano s: eje horizontal σ, eje vertical jω, rótulo "Plano s". Hay dos rectas horizontales exteriores (una arriba y otra abajo, simétricas) sin valor numérico; la inferior lleva una flecha con el rótulo "Frecuencia de Nyquist" (es decir, las rectas exteriores son ω = ±ω_N). Las regiones de interés están sombreadas en azul.
  [nota del transcriptor: el documento no da el valor numérico de ω_N; por definición ω_N = π/T, lo que daría 10.47, 15.71 y 31.42 rad/s para T = 0.3, 0.2 y 0.1 s.]

---

## Ejercicio 11 (pág. 7)

### a)
> Para las regiones en el plano-s mostradas, dibuje las regiones correspondientes en el plano-z, considerando T = 0.3 seg.

**Figura I)**
- Rectas verticales en σ = −2.31 y σ = 0.32 (esta última a la derecha del eje jω, semiplano derecho).
- Rectas horizontales en jω = j2.5 y en ±frecuencia de Nyquist.
- Una recta oblicua que pasa por el origen y entra al segundo cuadrante; el ángulo marcado es **126.87°**, medido desde el eje real positivo hasta la recta.
- Región sombreada (una sola, en el semiplano superior): limitada a la izquierda por σ = −2.31, a la derecha por σ = 0.32, arriba por la recta de Nyquist superior, abajo por jω = j2.5, y con la esquina inferior izquierda recortada por la recta oblicua (la región queda arriba/a la derecha de la oblicua). Es un pentágono: la oblicua corta a jω = j2.5 entre las dos verticales y corta a σ = −2.31 algo por encima de j2.5.

**Figura II)**
- Rectas verticales en σ = −5.41 y σ = −0.74.
- Rectas horizontales en jω = j2.62, jω = −j5.24 y ±frecuencia de Nyquist.
- Una recta oblicua desde el origen hacia el segundo cuadrante que pasa por la intersección de σ = −5.41 con jω = j2.62 [dudoso: en el dibujo coincide con esa esquina; no hay ángulo rotulado].
- Región sombreada (una sola, cruza el eje real): entre σ = −5.41 y σ = −0.74; límite inferior jω = −j5.24; límite superior la recta oblicua (vértice superior izquierdo en (−5.41, j2.62); en σ = −0.74 el límite superior queda apenas por encima del eje real).

### b)
> Si la función de transferencia de un sistema es B(z)/A(z), para cada caso dibuje sobre un plano z los pares de polos y marque con una o varias "X" la tabla adjunta especificando las características del sistema.

- i) A(z) = z² − 0.6z + 0.05
- ii) A(z) = z² + 1.21
- iii) A(z) = z² + 2z + 1
- iv) A(z) = z² + 0.8z + 1

Tabla (vacía en el documento):

| | i) | ii) | iii) | iv) |
|---|---|---|---|---|
| Estable | | | | |
| Inestable | | | | |
| Estabilidad crítica | | | | |
| Sobreamortiguado | | | | |
| Subamortiguado | | | | |
| No amortiguado | | | | |
| A la frecuencia ω_N | | | | |

---

## Ejercicio 12 (pág. 8)

### a)
> Para las regiones en el plano-s mostradas, dibuje las áreas correspondientes en el plano-z, considerando T = 0.2 seg.

**Figura I)**
- Rectas verticales en σ = −4.58 y σ = 0.91 (esta última en el semiplano derecho).
- Rectas horizontales en jω = j3.97, jω = −j11.78 y ±frecuencia de Nyquist.
- Una recta oblicua por el origen hacia el segundo cuadrante; el ángulo marcado es **17.46°**, dibujado entre la recta oblicua y la recta vertical σ = −4.58 (en su intersección, parte superior), es decir, medido respecto a la vertical [dudoso: el dibujo no está a escala — la oblicua se ve a ~45° —, pero el arco del ángulo está claramente entre la oblicua y la vertical].
- Dos regiones sombreadas:
  1. Semiplano superior: trapecio entre el eje real (ω = 0) y jω = j3.97, limitado a la izquierda por σ = −4.58 y a la derecha por la recta oblicua (termina en punta en el origen).
  2. Semiplano inferior: rectángulo entre σ = −4.58 y σ = 0.91, y entre jω = −j11.78 y la recta de Nyquist inferior (incluye una franja del semiplano derecho).

**Figura II)**
- Rectas verticales en σ = −11.51 y σ = −1.11.
- Rectas horizontales en jω = j13.09, jω = −j7.85 y ±frecuencia de Nyquist.
- Una recta oblicua por el origen hacia el tercer cuadrante; ángulo marcado **78.46°**, dibujado entre la oblicua y la recta horizontal jω = −j7.85 (lado izquierdo de la oblicua), es decir, medido respecto a la horizontal.
- Dos regiones sombreadas:
  1. Semiplano superior: rectángulo entre σ = −11.51 y σ = −1.11, y entre el eje real (ω = 0) y jω = j13.09.
  2. Semiplano inferior: cuadrilátero entre jω = −j7.85 (arriba) y la recta de Nyquist inferior (abajo), limitado a la derecha por σ = −1.11 y a la izquierda por la recta oblicua.

### b)
> Si la función de transferencia de un sistema es B(z)/A(z), para cada caso dibuje sobre un plano z los pares de polos y marque con una o varias "X" la tabla adjunta especificando las características del sistema.

- i) A(z) = z² + 2.2z + 1.46
- ii) A(z) = z² + 0.6z + 0.09
- iii) A(z) = z² + 1.732z + 1
- iv) A(z) = z² − 0.9z + 0.14

Tabla (vacía en el documento; nótese que las filas difieren de las del Ejercicio 11):

| | i) | ii) | iii) | iv) |
|---|---|---|---|---|
| Estable | | | | |
| Inestable | | | | |
| Estabilidad crítica / no amortiguado | | | | |
| Sobreamortiguado | | | | |
| Subamortiguado | | | | |
| Criticamente amortiguado | | | | |
| A la frecuencia ω_N | | | | |

---

## Ejercicio 13 (pág. 9)

### a)
> Para las regiones en el plano-s mostradas, dibuje las áreas correspondientes en el plano-z, considerando T = 0.1 seg.

**Figura I)**
- Rectas verticales en σ = −13.73 y σ = −5.11.
- Rectas horizontales en jω = j10.3 y ±frecuencia de Nyquist.
- Dos rectas oblicuas por el origen (sin ángulos rotulados):
  - una hacia el segundo cuadrante, que pasa por la intersección de σ = −13.73 con jω = j10.3;
  - otra hacia el tercer cuadrante, que pasa por la intersección de σ = −13.73 con la recta de Nyquist inferior [dudoso: en el dibujo coincide con esa esquina].
- Dos regiones sombreadas:
  1. Semiplano superior: triángulo con vértices en (−13.73, 0), (−13.73, j10.3) y el origen; es decir, entre el eje real y la oblicua superior, a la derecha de σ = −13.73 [dudoso: el sombreado parece llegar hasta el origen, sobrepasando la vertical σ = −5.11, que no actúa como límite de esta región].
  2. Semiplano inferior: triángulo limitado a la derecha por σ = −5.11, abajo por la recta de Nyquist inferior y arriba/izquierda por la oblicua inferior (vértices: cruce de la oblicua con σ = −5.11; (−5.11, −jω_N); (−13.73, −jω_N)).

**Figura II)**
- Rectas verticales en σ = −23.03, σ = −9.2 y σ = 2.62 (esta última en el semiplano derecho).
- Rectas horizontales en jω = j18 y ±frecuencia de Nyquist.
- Una recta oblicua por el origen hacia el tercer cuadrante que pasa por un punto marcado con un círculo negro sobre σ = −23.03; una línea punteada horizontal une ese punto con el eje jω, rotulada **−j23.49** (el punto es (−23.03, −j23.49)).
- Dos regiones sombreadas (contiguas a lo largo del eje real):
  1. Semiplano superior: rectángulo entre σ = −23.03 y σ = 2.62, y entre el eje real y jω = j18 (incluye la franja 0 < σ < 2.62 del semiplano derecho).
  2. Semiplano inferior: triángulo entre el eje real y la recta oblicua, limitado a la izquierda por σ = −9.2 (vértices: (−9.2, 0), el origen y el cruce de la oblicua con σ = −9.2).

### b)
> Si la función de transferencia de un sistema es B(z)/A(z), para cada caso llene en una hoja aparte la tabla adjunta especificando las características del sistema.

- i) A(z) = z² + 2z + 1
- ii) A(z) = z² + z + 1
- iii) A(z) = z² − 1.6z + 0.63
- iv) A(z) = z² − 2.2z + 1.21

Tabla (vacía en el documento):

| | EST | AMORT | ω_N | GRAF |
|---|---|---|---|---|
| i) | | | | |
| ii) | | | | |
| iii) | | | | |
| iv) | | | | |

> Llenar de la siguiente manera: EST (Estabilidad): sí, no o crítica. AMORT (Amortiguación): Sobre, sub, críticamente o no amortiguado. ω_N (A la frecuencia Nyquist): sí o no. GRAF (Respuesta al escalón): dibuje un grafico tentativo de la respuesta en tiempo al escalón unitario

---

## Página 10 – Plantillas "Plano z"

Dos gráficas idénticas en blanco, tituladas "Plano z", para dibujar las respuestas:
- Ejes real e imaginario de −1 a 1 (marcas cada 0.5 en el eje horizontal y cada 0.2 en el vertical).
- Círculo unitario en línea continua.
- Curvas punteadas de factor de amortiguamiento ζ constante, rotuladas 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 y 1 (la de ζ = 0 coincide con el círculo unitario; la de ζ = 1 con el eje real positivo); todas convergen en z = 1. Simétricas respecto al eje real.
- No hay curvas de ω_n constante ni nada dibujado encima.
