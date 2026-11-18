# TRANSZ.py: transformada Z paso a paso (Casio fx-CG50, modo Python)

Calcula la transformada Z de una función G(s) y muestra todo el proceso:
polos, fracciones parciales, el par de la tabla usado en cada término y la
G(z) final con sus polos y ceros.

Son **dos archivos** y los dos tienen que estar en la calculadora, en la
misma carpeta:

| Archivo | Qué es |
|---|---|
| `TRANSZ.py` | El programa que ejecutas. Al inicio tiene comentarios con ejemplos de cómo ingresar los datos. |
| `ZMOTOR.py` | Hace los cálculos. No hace falta abrirlo. |

## Copiar a la calculadora

1. Conecta la fx-CG50 al PC con el cable USB y en la calculadora pulsa
   **F1 (USB Flash)**. Aparece en el PC como una unidad nueva.
2. Copia `TRANSZ.py` y `ZMOTOR.py` a la raíz de esa unidad.
3. Expulsa la unidad desde Windows y desconecta el cable.
4. En la calculadora: **MENU → Python**, elige `TRANSZ.py` y pulsa **F1 (Run)**.

## Cómo se usa

Aparece un menú:

```
== TRANSFORMADA Z ==
1) Ingresar G(s)
2) Ejemplo con ZOH
3) Ejemplo directo
0) Salir
```

Las opciones 2 y 3 son ejemplos ya cargados: muestran lo que se teclearía y
calculan. Úsalas la primera vez para ver cómo funciona.

Con la opción **1** el programa hace 4 preguntas, y en cada una muestra un
ejemplo en pantalla:

| Paso | Pregunta | Qué escribir |
|---|---|---|
| 1 | `N1?`, `N2?`, … | El **numerador**, un factor en cada pregunta. EXE en blanco cuando no hay más. |
| 2 | `D1?`, `D2?`, … | El **denominador**, igual, factor por factor. |
| 3 | `T?` | El periodo de muestreo en segundos, por ejemplo `0.1`. |
| 4 | `Metodo 1 o 2?` | `1` = Z{G(s)} directa. `2` = con retenedor ZOH: G(z) = (1−z⁻¹)·Z{G(s)/s}. |

Después de cada factor el programa te muestra cómo lo entendió (`= s^2+2s+5`),
y antes de calcular te enseña N(s), D(s), T y el método para que confirmes.
Si algo está mal eliges `2=Otra` y vuelves a empezar.

### Cómo escribir un factor

Escríbelo como en el cuaderno. Puedes usar `s` o `x`; la tecla **[X,θ,T]**
escribe `x` de un solo toque, así no necesitas ALPHA.

| Escribes | Significa |
|---|---|
| `10` | la constante 10 |
| `s` | s (polo en cero) |
| `s+2` | (s+2) |
| `2s+1` o `2*s+1` | (2s+1) |
| `s^2+2s+5` o `s**2+2*s+5` | (s²+2s+5) |
| `(s+1)^2` | (s+1)², factor repetido |
| `5(s+1)` | 5(s+1) |
| `1,2,5` | también vale dar los coeficientes: s²+2s+5 |

En modo ZOH **no** agregues tú el 1/s: el programa lo hace.

## Ejemplos

**A)** G(s) = 10(s+3) / (s(s+1)(s+2)), T = 0.1, con ZOH:

```
N1? 10
N2? s+3
N3?            <- EXE en blanco
D1? s
D2? s+1
D3? s+2
D4?            <- EXE en blanco
T? 0.1
Metodo 1 o 2? 2
1=Calcular 2=Otra? 1
```

Salida (resumida; pulsa EXE cuando diga `[EXE] sigue`):

```
-- Polos en s --
p1=0 (x2)
p2=-2
p3=-1
-- Fracc. parciales y tabla Z --
T1: A/s, A=-17.5      ->A*z/(z-1)
T2: A/s^2, A=15       ->A*T*z/(z-1)^2
T3: A/(s+2), A=-2.5   ->A*z/(z-E)   E=0.818731
T4: A/(s+1), A=20     ->A*z/(z-E)   E=0.904837
== G(z)=N(z)/D(z) ==
G(z)=(0.0499215z^2+0.0129289z-0.0369753)/
     (z^3-2.72357z^2+2.46439z-0.740818)
-- Polos en z --  1, 0.818731, 0.904837
-- Ceros en z --  0.740817, -0.999802
```

**B)** G(s) = 4/(s²+2s+4), T = 0.5, directa:

```
N1? 4
N2?
D1? s^2+2s+4
D2?
T? 0.5
Metodo 1 o 2? 1
```

**C)** G(s) = (s+3)/((s+1)²(s²+2s+5)):

```
N1? s+3
N2?
D1? (s+1)^2
D2? s^2+2s+5
D3?
```

## Notación de la salida

- `E` = e^(−aT), `cw` = cos(wT), `sw` = sin(wT).
- `A` = residuo del término; los términos se numeran T1, T2, …
- `(x2)` = polo doble; `p2,3=-1+/-2j` = par complejo conjugado.
- Las líneas de más de 21 caracteres siguen en la línea de abajo.

## Verificación y limitaciones

- **No se ha ejecutado en una fx-CG50 física.** Se probó en MicroPython 1.9.4
  (la versión en que se basa el Python de Casio) y en Python de escritorio.
  Los cálculos son los mismos de la versión anterior, ya verificada contra
  referencias independientes. Con 8 funciones distintas, la nueva forma de
  ingresar datos da exactamente el mismo G(z).
- Si al abrir `TRANSZ.py` sale `ImportError: no module named 'ZMOTOR'`, falta
  copiar `ZMOTOR.py` o quedó en otra carpeta.
- Si sale `MemoryError`, la función es demasiado grande para la memoria de la
  calculadora.
- Modo 1 exige grado(N) < grado(D); modo 2 admite grado(N) ≤ grado(D).
- No hay retardo (e^(−Ls)) ni transformada Z modificada.
- Los números se escriben en decimal (`0.5`, `1e-3`), no como `1/3` ni `pi`.
- Con T muy pequeño, o con polos casi iguales pero distintos, se pierde
  precisión; en ese caso el programa imprime un `AVISO`.
- No se cancelan factores comunes entre N(s) y D(s).
