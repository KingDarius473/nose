# Deber 2 (Control Avanzado, dominio z) en la Casio fx-CG50 (modo Python)

Programas (cada uno es independiente, no necesita a los demas):

| Archivo | Para que sirve | Ejercicios |
|---|---|---|
| `JURY.py` | Criterio de Jury con K numerico: condiciones, arreglo (b_k, c_k), veredicto, raices y modulo | 1.d, 1.e, comprobar 2-4 |
| `JURYK.py` | Rango de K: P(z) = P0(z) + K*P1(z). Expresiones en K de cada condicion, b_k en funcion de K, K criticos e intervalo estable | 1, 2, 3, 4 |
| `LAZO.py` | Multiplicar polinomios, sumar/restar fracciones, lazo cerrado C/R = G/(1+GH), entrega P0 y P1 | 1-4, 8.a, 9.a |
| `ERRZ.py` | Kp, Kv, Ka, tipo del sistema y e_ss (escalon, rampa, parabola) | 5, 8.a |
| `ESPEC.py` | %OS, zeta, ts, tp, wn, wd, muestras/oscilacion <-> polo z | 7-10 |
| `DISENO.py` | Condicion de angulo y magnitud; controlador PD, PI o K1(1-z^-1)+K2 | 7-10 |
| `LGR.py` | Lugar de las raices: K critico, K para un zeta dado, polos para un K | 6 |
| `MENU.py` | Opcional: menu que lanza los anteriores con `import` | - |

(`TRANSZ*.py` de esta carpeta son de otro tema; no forman parte de este juego.)

## Como copiarlos a la calculadora

1. Conecta la fx-CG50 a la PC con el cable USB. En la calculadora aparece "Select Connection Mode": pulsa **F1 (USB Flash)**. La calculadora aparece en la PC como una unidad de disco.
2. Copia los `.py` a la unidad (en la raiz o en una carpeta; si usas `MENU.py`, todos en la misma carpeta).
3. Expulsa la unidad desde la PC ("quitar hardware con seguridad") y luego desconecta el cable.
4. En la calculadora: **MENU -> Python**. Selecciona el archivo con las flechas y pulsa **F1 (RUN)**.
5. Para repetir un programa: **EXIT** y de nuevo **F1 (RUN)**. Para cortar un programa: **AC/ON**.

Requiere que la calculadora tenga el modo Python (sistema operativo 3.20 o superior).

## Como se teclea

- Un polinomio se escribe como sus coeficientes separados por comas, **de la potencia mayor a la menor**: `z^2 - 1.2z + 0.27` es `1,-1.2,0.27`. Si falta una potencia se pone 0: `z^3 + 0.5` es `1,0,0,0.5`.
- Se pueden multiplicar factores con `*` (tecla de multiplicar): `(z+0.2)(z-0.5)z` es `1,0.2*1,-0.5*1,0`. Una constante suelta tambien vale: `0.02(z+0.7)` es `0.02*1,0.7`.
- Se aceptan fracciones simples: `1/200`.
- El signo menos puede ser la tecla `(-)` o la de restar.
- Cuando la pantalla se llena aparece `[EXE]`: pulsa **EXE** para seguir.
- Si tecleas algo mal aparece `? repita` y vuelve a preguntar.
- Los resultados salen redondeados a 4 decimales.

## Convencion del arreglo de Jury (la misma del profesor)

P(z) = an z^n + ... + a1 z + a0, con an > 0.

- Fila 1: a0, a1, ..., an (columnas z^0 ... z^n). Fila 2: la misma al reves.
- Fila 3: b_(n-1) ... b_0, donde el elemento j (contando desde 0) es `F1[0]*F1[j] - F1[n]*F1[n-j]`.
- Condiciones: 1) |a0| < an; 2) P(1) > 0; 3) (-1)^n P(-1) > 0; 4) |b_(n-1)| > |b_0|; (grado 4: 5) |c_2| > |c_0|).

---

# Que teclear en cada ejercicio

## Ejercicio 1 (Jury, K en el lazo directo)

G(z) = K (1+z^-1) 0.1/(z^2-0.2z-0.03) = K 0.1(z+1) / (z (z^2-0.2z-0.03)), H = 1.

**a) `LAZO.py`**, opcion `3`:

```
num G? 0.1,0.1
den G? 1,0*1,-0.2,-0.03
num H? 1
den H? 1
K (1 si no hay)? 1
```

Salida: `num C/R = 0.1,0.1` (o sea 0.1K(z+1)), `P0 = 1,-0.2,-0.03,0`, `P1 = 0.1,0.1`.
Es decir P(z) = z^3 - 0.2z^2 - 0.03z + K(0.1z + 0.1) = z^3 - 0.2z^2 + (0.1K-0.03)z + 0.1K.

**b) y c) `JURYK.py`:**

```
P0 (sin K)? 1,-0.2,-0.03,0
P1 (x K)? 0.1,0.1
K min busq? 0
K max busq? 20
```

Salida esperada: `a0=0.1K`, `an=1` -> `-10<K<10` (con K>0: 0<K<10); `P(1)=0.77+0.2K` -> `K>-3.85` (con K>0: K>0); `(-1)^n P(-1) = 1.17` siempre (el profesor lo escribe como P(-1) = -1.17 < 0); `b2=-1+0.01K^2`, `b1=0.2-0.003K+0.01K^2`, `b0=0.03-0.12K`; condicion 4: |b2|>|b0|. (El enunciado pide no resolverla; el programa igual indica estable para 0<K<5.7898.)

**d) K=1: `JURY.py`** con `1,-0.2,0.07,0.1` -> b2=-0.99, b1=0.207, b0=-0.09, `=> ESTABLE`.

**e) K=10: `JURY.py`** con `1,-0.2,0.97,1` -> condicion 1 `1<1 NO`, b2=0, `=> INESTABLE` (raices 0.4271+-j1.1603, modulo 1.2364).

(Los coeficientes para un K dado salen de P0 + K*P1, o de `LAZO.py` opcion 3 poniendo ese K.)

## Ejercicio 2

G = K/((z+0.2)(z-0.5)), H = 1/z.

**a) `LAZO.py`**, opcion `3`: `num G? 1`, `den G? 1,0.2*1,-0.5`, `num H? 1`, `den H? 1,0`, `K? 1`.
Salida: `num C/R = 1,0` (K z), `P0 = 1,-0.3,-0.1,0`, `P1 = 1`. P(z) = z^3 - 0.3z^2 - 0.1z + K.

**b), c), d) `JURYK.py`:**

```
P0 (sin K)? 1,-0.3,-0.1,0
P1 (x K)? 1
K min busq? 0
K max busq? 3
```

Salida: `-1<K<1`; `P(1)=0.6+K` -> `K>-0.6`; `1.2-K` -> `K<1.2`; `b2=-1+K^2`, `b1=0.3-0.1K`, `b0=0.1-0.3K`; `K criticos: -1.2095,-0.8105,0.9095,1.1105`; `=> ESTABLE si: 0<K<0.9095`.

Para ver tambien los intervalos negativos de la condicion 4 usa `K min = -3`: sale `C4: -3<K<-1.2095 o -0.8105<K<0.9095 o 1.1105<K<3`.
Nota: el solucionario imprime -0.8015; el valor correcto de la raiz de K^2-0.3K-0.9 es -0.8105 (errata de digitos cambiados).

## Ejercicio 3

Camino directo: 2.5 (1/(z-0.6) - 1/(z-0.4)); H = M/(z-0.2).

**a) `LAZO.py`**, opcion `2` (resta de las dos ramas): `N1? 1`, `D1? 1,-0.6`, `N2? 1`, `D2? 1,-0.4`, `2` (resta) -> `N = 0,0.2`, `D = 1,-1,0.24`. Entonces G = 2.5*0.2/(z^2-z+0.24) = 0.5/((z-0.6)(z-0.4)).
Luego opcion `3`: `num G? 0.5`, `den G? 1,-1,0.24`, `num H? 1`, `den H? 1,-0.2`, `K? 1` -> `num C/R = 0.5,-0.1` (0.5(z-0.2)), `P0 = 1,-1.2,0.44,-0.048`, `P1 = 0.5`.

**b)-e) `JURYK.py`** (aqui "K" es M):

```
P0 (sin K)? 1,-1.2,0.44,-0.048
P1 (x K)? 0.5
K min busq? 0
K max busq? 6
```

Salida: `-1.904<K<2.096` (con M>0: 0<M<2.096); `P(1)=0.192+0.5K` -> `K>-0.384` (M>0); `2.688-0.5K` -> `K<5.376`; `b2=-0.9977-0.048K+0.25K^2`, `b1=1.1789+0.22K`, `b0=-0.3824-0.6K`; `K criticos: -3.0223,-1.3873,0.8143,3.9793`; `C4: 0<K<0.8143 o 3.9793<K<6`; `=> ESTABLE si: 0<K<0.8143`.

Nota: el solucionario pone "M > 3.3309" en la condicion 4; resolviendo la inecuacion sale M > 3.9793 (no afecta la respuesta final 0<M<0.8143).

## Ejercicio 4

**a) `LAZO.py`**, opcion `3` dos veces.
Lazo interno: `num G? 0.4`, `den G? 1,0.4`, `num H? 0.5`, `den H? 1,0.1`, `K? 1` -> num `0.4,0.04`, P(z) con K=1 `1,0.5,0.24`. (Lazo interno = 0.4(z+0.1)/(z^2+0.5z+0.24).)
Lazo externo: `num G? 0.4,0.04*5`, `den G? 1,0.5,0.24*1,-0.3`, `num H? 1`, `den H? 1`, `K? 1` -> `num C/R = 2,0.2` (o sea 2K(z+0.1); el solucionario imprime 0.2K(z+0.1), errata), `P0 = 1,0.2,0.09,-0.072`, `P1 = 2,0.2`.

**b)-e) `JURYK.py`:**

```
P0 (sin K)? 1,0.2,0.09,-0.072
P1 (x K)? 2,0.2
K min busq? 0
K max busq? 60
```

Salida: `a0=-0.072+0.2K` -> `-4.64<K<5.36`; `P(1)=1.218+2.2K` -> `K>-0.5536`; `0.962+1.8K` -> `K>-0.5344`; `b2=-0.9948-0.0288K+0.04K^2`, `b1=-0.2065-0.126K+0.4K^2`, `b0=-0.1044-1.96K`; `K criticos: -48.7367,-0.5467,0.4567,50.2667`; `C4: 0<K<0.4567 o 50.2667<K<60`; `=> ESTABLE si: 0<K<0.4567`.

## Ejercicio 5 (`ERRZ.py`)

No se da T: teclea `1` (entonces el Kv mostrado es Kv*T; divide para tu T si lo necesitas).

i) `num G? 0.4*1,0.2`, `den G? 1,-1*1,-0.1`, `T? 1` -> tipo 1, `Kp=inf`, `Kv=0.5333` (= 0.48/(0.9 T)), ess escalon `0`, ess rampa `1.875` (= 1.875 T).

ii) `num G? 0.5*1,0.2`, `den G? 1,-0.1*1,-0.8`, `T? 1` -> tipo 0, `Kp=3.3333`, `Kv=0`, ess escalon `0.2308`, ess rampa `inf`.

## Ejercicio 6 (`LGR.py`)

```
num G? 1,1
den G? 1,-1*1,-0.6065
T? 0.1
```

- Opcion `1`, `K max busq? 5` -> `K critico=0.3935`, polos 0.6065+-j0.7951 (modulo 1), w = 9.1915 rad/s.
- Opcion `2`, `zeta? 0.5`, `K max busq? 0.39` -> `K=0.0647`, `z=0.7709+j0.2773`, |z|=0.8193, ang=0.3453 rad (19.78 grados), `wd=3.4529`, `wn=3.9871`, `muestras/ciclo=18.1969`.
- Opcion `3` da los polos de lazo cerrado para cualquier K (sirve para tabular puntos y dibujar el lugar: K=0 -> 1 y 0.6065; el lugar se separa del eje real entre los polos, es un circulo centrado en el cero z=-1, y vuelve al eje real a la izquierda de -1).

No hay respuesta del profesor para 5 y 6.

## Ejercicio 7

**a) y b) `ESPEC.py`**, opcion `1` ("al menos 10 muestras" se disena con 10):

```
opcion? 1
T? 0.2
ts? 0.8
muestras/osc? 10
```

Salida: `zeta=0.8467`, `wn=5.905`, `tp=1`, `|z|=0.3679`, ang 36 grados, `Re=0.2976`, `Im=+-0.2162`.

**b), c), d) `DISENO.py`:**

```
num G? 0.02*1,0.7
den G? 1,-1.2,0.27
z1: 1=Re,Im 2=zeta,wn? 2
zeta? 0.8467
wn? 5.905
T? 0.2
```

Salida: angulos (cero -0.7: 12.23; polo 0.9: 160.25; polo 0.3: 90.63), `ang G = 121.35`, `phi = 58.65` -> `NO basta solo K`.
Opcion `1` (PD): `a=0.3152`, `GD=11.496(z-0.3152)/z`, KP=7.8721, KD=3.6238; polos de lazo cerrado 0.2976+-j0.2163 y 0.3749.
Opcion `2` (PI): `No factible` (el polo en z=1 quita angulo; el cero tendria que aportar 221 grados). Por eso la estructura es PD.

## Ejercicio 8

**a)** Lazo cerrado con KP=40: `LAZO.py` opcion `3`: `num G? 40/200`, `den G? 1,-1,0.16`, H `1` y `1`, `K? 1` -> P(z) = `1,-1,0.36`.
`ESPEC.py`: `opcion? 6`, `T? 0.1`, `P z^n..z^0? 1,-1,0.36` -> polos 0.5+-j0.3317, `zeta=0.6573`, `ts=0.783`, `%OS=6.4567`, `muestras/osc=10.7279`.
`ERRZ.py`: `num G? 40/200`, `den G? 1,-1,0.16`, `T? 0.1` -> `Kp=1.25`, ess escalon `0.4444`.

**b)** `ESPEC.py`: `opcion? 3`, `T? 0.1`, `%OS? 6.4567`, `ts? 0.5` -> `zeta=0.6573`, `wn=12.171`, z = 0.2732+-j0.3567.
`DISENO.py`: `num G? 1/200`, `den G? 1,-1,0.16`, `2`, `zeta? 0.6573`, `wn? 12.171`, `T? 0.1`, opcion `1` (PD) -> `GD=57.9488(z-0.3161)/z`, `KP=39.6326`, `KD=18.3163` (KI=0).

**c)** El mismo `DISENO.py` muestra al final `Kp=1.2385`, `ess=0.4467`. (Mejora: agregar accion integral / subir el tipo del sistema.)

## Ejercicio 9

**a)** `LAZO.py` opcion `3`: `num G? 1,0.5`, `den G? 4,-4.8,1.28`, H `1`, `1`, `K? 0.38` -> P(z) = `4,-4.42,1.47`.
`ESPEC.py`: `opcion? 6`, `T? 0.08`, `P? 4,-4.42,1.47` -> `%OS=2.4546`, `tp=0.5925` (no cumple tp=0.4).

**b)** `ESPEC.py`: `opcion? 2`, `T? 0.08`, `%OS? 2.4`, `tp? 0.4` -> `zeta=0.7648`, `wn=12.1913`, `muestras/osc=10`, `Re=0.3837`, `Im=+-0.2788`.

**c)** `DISENO.py`: `num G? 1,0.5`, `den G? 4,-4.8,1.28`, `2`, `zeta? 0.7648`, `wn? 12.1913`, `T? 0.08`, opcion `3` -> `GD=1.0052(z-0.3246)/z`, `K1=0.3263`, `K2=0.6789` (es un PD: K1 = KD, K2 = KP).

## Ejercicio 10

**a) y b)** `ESPEC.py`: `opcion? 1`, `T? 0.1`, `ts? 0.5`, `muestras/osc? 8` -> `zeta=0.7136`, `wn=11.2109`, `Re=0.3177`, `Im=+-0.3177`.

**b), c), d)** `DISENO.py` (planta = integrador por planta):

```
num G? 1,3
den G? 100*1,-1*1,0.5,-0.06
z1: 1=Re,Im 2=zeta,wn? 2
zeta? 0.7136
wn? 11.2109
T? 0.1
```

Salida: `ang G = 135.76`, `phi = 44.24` -> `NO basta solo K`.
Opcion `1` (PD): `a=0.3135`, `GD=11.9446(z-0.3135)/z`, `KP=8.2003`, `KD=3.7443`, `Kp=inf, ess escalon=0` (el integrador ya da error cero, por eso no hace falta PI).
Opcion `2` (PI): `No factible`.

---

# Diferencias con el solucionario (para que no te asustes)

El programa trabaja con toda la precision; el profesor redondea pasos intermedios. Por eso algunos valores difieren en la 3ra-4ta cifra:

| Ej. | Profesor | Programa |
|---|---|---|
| 7 | wn=5.9055; GD=11.5032(z-0.3152)/z | wn=5.905 (sqrt(25+pi^2)=5.90505); GD=11.496(z-0.3152)/z |
| 8.a | %OS=6.4568; nmo=10.727 | 6.4567; 10.7279 |
| 8.b | KP=39.8958, KD=18.1176 | KP=39.6326, KD=18.3163 |
| 8.c | ess=0.4451 | 0.4467 |
| 9 | wn=12.1906; K2=0.679 | 12.1913; 0.6789 |
| 10 | GD=11.9426(z-0.3135)/z; KP=8.1986, KD=3.744 | 11.9446(z-0.3135)/z; 8.2003, 3.7443 |

En el 8.b la diferencia es de ~1 %: con las ganancias del profesor los polos de lazo cerrado quedan en 0.2768+-j0.3554 (ts=0.5016, %OS=6.36), no exactamente en el polo deseado 0.2732+-j0.3567; con las del programa quedan exactamente en el polo deseado (el programa lo muestra en "Polos lazo cerrado"). En el deber conviene escribir tu propio proceso con los numeros del programa y comentar que la diferencia es de redondeo.

Si prefieres teclear el polo redondeado como hace el profesor, en `DISENO.py` responde `1` a `z1:` y da `Re` e `Im`.

# Limitaciones

- `JURYK.py` busca los limites de estabilidad barriendo K en 200 pasos dentro del intervalo que tu das y afinando por biseccion: si un intervalo estable es mas angosto que (Kmax-Kmin)/200 puede no verlo; achica el intervalo de busqueda. Los extremos que coinciden con Kmin o Kmax son solo el limite de la busqueda.
- La lista "K criticos" de la condicion 4 solo sale cuando b_k es de grado <= 2 en K (sistemas de orden 3). Para orden 4 se usa solo el barrido.
- `JURYK.py` solo admite K entrando linealmente: P = P0 + K*P1.
- Igualdades exactas en una condicion de Jury (caso critico) se reportan como NO.
- `ERRZ.py` no verifica la estabilidad del lazo cerrado (los e_ss solo valen si es estable; compruebalo con `JURY.py`).
- `ESPEC.py`/`LGR.py` toman como polo dominante el par complejo de mayor modulo.
- `LGR.py` no dibuja; da K critico, K para un zeta y polos para cualquier K.
- Raices por Durand-Kerner: raices multiples salen con ~6 cifras buenas.
