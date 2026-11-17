# TRANSZ.py — Transformada Z paso a paso (Casio fx-CG50, modo Python)

Calcula la transformada Z de una función racional G(s) y muestra el proceso:
polos, fracciones parciales, par de la tabla aplicado a cada término, valores
de e^(-aT) y la G(z) final como cociente de polinomios (denominador mónico),
con sus polos y ceros en z.

Dos modos:

1. `Z{G(s)}` directa (muestreo por impulso).
2. Con retenedor de orden cero: `G(z) = (1 - z^-1) * Z{G(s)/s}`.

## Copiar a la calculadora

1. Conecta la fx-CG50 al PC con el cable USB y en la calculadora elige
   **F1 (USB Flash)**. Aparece en el PC como una unidad de almacenamiento.
2. Copia `TRANSZ.py` a la raíz de la unidad (o a una carpeta; el nombre debe
   quedar en formato 8.3, tal como está).
3. Expulsa la unidad desde el PC ("quitar hardware con seguridad") y desconecta.
4. En la calculadora: **MENU → Python**, selecciona `TRANSZ.py` y pulsa
   **F1 (RUN)**.
5. Para repetir sin salir, escribe `main()` en el shell y pulsa EXE.

Requiere el sistema operativo 3.20 o posterior (el que incluye el modo Python).

## Ingreso de datos

El programa pregunta, en orden:

| Pregunta | Qué escribir |
|---|---|
| `N(s) coef?` | Coeficientes del numerador, potencias descendentes, separados por comas. `1,3` es s+3. |
| `D(s) 1=coef 2=polos?` | `1` (o solo EXE) para dar coeficientes; `2` para dar los polos. |
| `D(s) coef?` | Coeficientes del denominador. `1,3,2` es s^2+3s+2. |
| `polo?` (si elegiste 2) | Un polo por línea como `re,im,mult`. `im` y `mult` son opcionales. EXE vacío para terminar. |
| `T?` | Periodo de muestreo (mayor que 0). |
| `1=Z{G(s)} 2=con ZOH?` | `1` (o EXE) directa; `2` con retenedor. |

Detalles útiles:

- **Producto de factores con `;`**: `1,1;1,2;1,3` es (s+1)(s+2)(s+3). Vale
  para numerador y denominador. Repite el factor para una potencia:
  `1,1;1,1` es (s+1)^2. La coma y el punto y coma están en el teclado/menú
  CHAR del modo Python.
- **Polos**: `-1` es un polo real en s=-1; `-1,0,2` es polo doble en s=-1;
  `-1,2` es el par complejo -1±2j (el conjugado se agrega solo); `0,0,2` es
  un polo doble en el origen. Con esta opción el denominador es mónico: la
  ganancia va en el numerador.
- Si el denominador no es mónico (por ejemplo `3,4,1`) no hay que normalizar.
- En modo ZOH **no** agregues tú el 1/s: el programa lo hace.
- La salida se detiene cada 6 líneas con `[EXE] sigue`; pulsa EXE.
- Las líneas de más de 21 caracteres continúan en la línea siguiente.

Notación de la salida: `E` = e^(-aT), `cw` = cos(wT), `sw` = sin(wT),
`A` = residuo del término, `(x2)` = multiplicidad 2, `p2,3=-1+/-2j` = par
complejo conjugado. Los términos se numeran T1, T2, ...

## Ejemplo 1: 1/(s(s+1)) con ZOH, T = 1

Entradas: `1` / `1` / `1,1,0` / `1` / `2`

```
== TRANSFORMADA Z ==
N(s) coef? 1
D(s) 1=coef 2=polos?1
D(s) coef? 1,1,0
T? 1
1=Z{G(s)} 2=con ZOH?2
N(s): 1
D(s): 1,1,0
T=1
ZOH: G(z)=(1-z^-1)*Z{
G(s)/s}
Se expande G(s)/s
[EXE] sigue
-- Polos en s --
p1=0 (x2)
p2=-1
-- Fracc. parciales y
 tabla Z --
Polo s=0
[EXE] sigue
T1: A/s, A=-1
->A*z/(z-1)
=(-z)/(z-1)
T2: A/s^2, A=1
->A*T*z/(z-1)^2
=(z)/(z-1)^2
[EXE] sigue
Polo s=-1: a=1
E=e^(-aT)=0.367879
T3: A/(s+1), A=1
->A*z/(z-E)
=(z)/(z-0.367879)
-- ZOH --
[EXE] sigue
G(z)=(z-1)/z*suma(Ti)
se simplifican z y (z
-1)
== G(z)=N(z)/D(z) ==
N(z):
 z^1: 0.367879
[EXE] sigue
 z^0: 0.264241
D(z):
 z^2: 1
 z^1: -1.36788
 z^0: 0.367879
G(z)=(0.367879z+0.264
[EXE] sigue
241)/(z^2-1.36788z+0.
367879)
-- Polos en z --
z1=1
z2=0.367879
-- Ceros en z --
[EXE] sigue
c1=-0.718282
FIN
```

Resultado: G(z) = (0.3679 z + 0.2642) / (z^2 - 1.3679 z + 0.3679), el clásico
de los libros (Ogata, Kuo).

## Ejemplo 2: (s+3)/((s+1)^2 (s^2+2s+5)) directa, T = 0.1, ingresando polos

Entradas: `1,3` / `2` / `-1,0,2` / `-1,2` / (EXE vacío) / `0.1` / `1`

```
== TRANSFORMADA Z ==
N(s) coef? 1,3
D(s) 1=coef 2=polos?2
Polo: re,im,mult
(vacio = fin)
polo? -1,0,2
polo? -1,2
polo?
T? 0.1
1=Z{G(s)} 2=con ZOH?1
N(s): 1,3
D(s): 1,4,10,12,5
T=0.1
-- Polos en s --
p1=-1 (x2)
p2,3=-1+/-2j
[EXE] sigue
-- Fracc. parciales y
 tabla Z --
Polo s=-1: a=1
E=e^(-aT)=0.904837
T1: A/(s+1), A=0.25
->A*z/(z-E)
[EXE] sigue
=(0.25z)/(z-0.904837)
T2: A/(s+1)^2, A=0.5
->A*T*E*z/(z-E)^2
=(0.0452419z)/(z-0.90
4837)^2
Par s=-1+/-2j
[EXE] sigue
a=1 w=2
E=e^(-aT)=0.904837
cw=cos(wT)=0.980067
sw=sin(wT)=0.198669
T3: (B(s+a)+C*w)/((s+
a)^2+w^2)
[EXE] sigue
B=-0.25 C=-0.25
g(t)=e^(-at)*(B*cos(w
t)+C*sin(wt))
->z(B(z-E*cw)+C*E*sw)
/(z^2-2E*cw*z+E^2)
=(-0.25z^2+0.176759z)
[EXE] sigue
/(z^2-1.7736z+0.81873
1)
== G(z)=N(z)/D(z) ==
N(z):
 z^3: 0.00481014
 z^2: 0.00108728
[EXE] sigue
 z^1: -0.00344531
 z^0: 0
D(z):
 z^4: 1
 z^3: -3.58328
 z^2: 4.8471
[EXE] sigue
 z^1: -2.93374
 z^0: 0.67032
G(z)=(0.00481014z^3+0
.00108728z^2-0.003445
31z)/(z^4-3.58328z^3+
4.8471z^2-2.93374z+0.
[EXE] sigue
67032)
-- Polos en z --
z1=0.904837 (x2)
z2,3=0.886801+/-0.179
763j
-- Ceros en z --
[EXE] sigue
c1=0
c2=0.740816
c3=-0.966855
FIN
```

Ingresando el denominador como coeficientes (`1` y luego `1,4,10,12,5`) el
resultado es el mismo; el programa encuentra los polos por sí solo.

## Qué hace por dentro

- Polos: Durand-Kerner con aritmética compleja hecha a mano; las raíces
  repetidas se agrupan por tolerancia y se pulen con Newton sobre la derivada
  de orden (multiplicidad - 1). Los polos en s=0 se extraen exactos.
- Residuos (también de polos múltiples): serie de Taylor de N(s)/Q(s)
  alrededor del polo, con Q(s) = D(s)/(s-p)^m.
- Tabla: A/(s-p)^k  ->  A T^(k-1)/(k-1)! * Z{n^(k-1) q^n}, con q = e^(pT).
  Para k = 1, 2, 3 se muestra la fórmula conocida; para k >= 4 solo el
  resultado numérico del término.
- ZOH: se expande G(s)/s y se multiplica por (z-1)/z; el factor z y un (z-1)
  se simplifican exactamente.

## Limitaciones

- **No se ha ejecutado en una fx-CG50 física.** Se probó en MicroPython 1.9.4
  (port unix, la misma versión base que usa Casio), MicroPython 1.22 y
  CPython 3. Si la calculadora da un error, anota el mensaje y la línea.
- Modo 1 exige grado(N) < grado(D); modo 2 admite grado(N) <= grado(D).
  No hay retardo de transporte (e^(-Ls)) ni transformada Z modificada.
- Modo 1 usa la convención de la tabla: g(0) = g(0+). Si el grado relativo
  es 1 (por ejemplo 1/(s+a)), algunos textos toman g(0) = g(0+)/2 y obtienen
  otro numerador.
- Se muestran 6 cifras significativas. Valores menores que 1e-13 en valor
  absoluto se muestran como 0.
- Polos muy cercanos pero distintos (separación relativa menor que ~1e-4)
  pueden tratarse como un polo repetido. Si la reconstrucción del polinomio
  no coincide, se imprime `AVISO: polos dudosos`: en ese caso no confíes en
  el resultado e ingresa los polos a mano (opción 2).
- Con T muy pequeño frente a las constantes de tiempo los polos en z quedan
  casi iguales y el numerador pierde precisión por cancelación. El programa
  imprime `AVISO: cancelacion fuerte, poca precision`. Con tres polos y
  T = 0.001 el numerador salió con unas 6 cifras correctas.
- Pares complejos repetidos: se muestran los residuos complejos R y el
  resultado numérico del término, no la forma en senos y cosenos.
- No se cancelan factores comunes entre N(s) y D(s): el residuo sale 0 y el
  polo sigue apareciendo en D(z) junto con un cero igual.
- Las entradas son números (`0.5`, `-2`, `1e-3`), no expresiones como `1/3`
  o `2*pi`.
- Órdenes altos (más de 8 a 10) tardan en la calculadora; con polos múltiples
  la búsqueda de raíces llega al tope de 120 iteraciones.
- El archivo tiene 299 líneas porque el editor de la calculadora admite 300
  como máximo. Si lo editas, no lo alargues.
