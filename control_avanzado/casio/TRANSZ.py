# ===================================================
# TRANSZ.py - TRANSFORMADA Z DE G(s), PASO A PASO
# Casio fx-CG50, menu Python. Necesita el archivo
# ZMOTOR.py en la MISMA carpeta (hace los calculos).
# ===================================================
# COMO SE USA: elige TRANSZ.py, pulsa Run (F1) y
# responde 4 preguntas:
#   1) NUMERADOR N(s), factor por factor
#   2) DENOMINADOR D(s), factor por factor
#      (EXE en blanco = ya no hay mas factores)
#   3) T = periodo de muestreo, en segundos
#   4) Metodo: 1 = Z{G(s)} directa
#              2 = con retenedor ZOH:
#                  G(z)=(1-z^-1)*Z{G(s)/s}
#
# COMO ESCRIBIR UN FACTOR (puedes usar s o x;
# la tecla [X,theta,T] escribe x de un toque):
#   10          una constante
#   s           polo en cero
#   s+2         (s+2)
#   2s+1        tambien 2*s+1
#   s^2+2s+5    el ^ y el ** sirven igual
#   (s+1)^2     factor repetido 2 veces
#   5(s+1)      constante por factor
#   1,2,5       o los coeficientes: s^2+2s+5
#
# EJEMPLO A:  G(s) = 10(s+3) / ( s(s+1)(s+2) )
#             T=0.1 con ZOH. Se teclea:
#   N1? 10
#   N2? s+3
#   N3? [EXE]        <- en blanco: fin de N(s)
#   D1? s
#   D2? s+1
#   D3? s+2
#   D4? [EXE]        <- en blanco: fin de D(s)
#   T? 0.1
#   Metodo? 2
#
# EJEMPLO B:  G(s) = 4/(s^2+2s+4), T=0.5, directa
#   N1? 4        N2? [EXE]
#   D1? s^2+2s+4 D2? [EXE]
#   T? 0.5       Metodo? 1
#
# EJEMPLO C:  G(s) = 1/(s+1)^2
#   N1? 1        N2? [EXE]
#   D1? (s+1)^2  D2? [EXE]
#
# LO QUE MUESTRA: polos de G(s), fracciones
# parciales con cada residuo, el par de la tabla
# de transformadas usado en cada termino, y al
# final G(z) = N(z)/D(z) con sus polos y ceros.
# Cuando la pantalla se llena: [EXE] para seguir.
# ===================================================
from ZMOTOR import *

def num(t):
  # "" o "+" -> 1 ; "-" -> -1 ; "2.5" -> 2.5
  if t in ("", "+"): return 1.0
  if t == "-": return -1.0
  return float(t)

def terminos(t):
  # "s^2+2s+5" -> [1, 2, 5]
  partes = []; w = ""
  for ch in t:
    if ch in "+-" and w and w[-1] not in "e^":
      partes.append(w); w = ""
    w += ch
  partes.append(w)
  c = {}
  for w in partes:
    if "s" in w:
      i = w.find("s"); a = num(w[:i])
      e = w[i+1:].replace("^", "")
      if e: e = int(e)
      else: e = 1
    else:
      a = float(w); e = 0
    c[e] = c.get(e, 0.0) + a
  n = max(c)
  return [c.get(n-i, 0.0) for i in range(n+1)]

def leer(t):
  # texto de UN factor -> lista de coeficientes
  t = t.replace(" ", "").replace("**", "^").replace("*", "")
  for v in "SxX": t = t.replace(v, "s")
  if "s" not in t:
    return [float(v) for v in t.split(",")]
  a = 1.0; k = 1
  if "(" in t:
    i = t.find("("); j = t.rfind(")")
    a = num(t[:i])
    r = t[j+1:].replace("^", "")
    if r: k = int(r)
    t = t[i+1:j]
  p = terminos(t); r = [a]
  for i in range(k): r = pm(r, p)
  return r

def factores(letra, ej):
  P = [1.0]; i = 1
  while 1:
    t = input(letra + str(i) + "? ")
    if t == "":
      if i > 1: return P
      print("Falta al menos uno"); continue
    try:
      f = st(leer(t))
      if f[0] == 0: raise ValueError
    except:
      print("No entendi eso."); print("Ej: " + ej); continue
    P = pm(P, f); i += 1
    print("  = " + ps(f, "s")[:17])

def titulo(s):
  print("---------------------"); print(s)

def pedir_T():
  while 1:
    try:
      T = float(input("T? "))
      if T > 0: return T
    except:
      pass
    print("T debe ser > 0")

def pedir_metodo():
  while 1:
    m = input("Metodo 1 o 2? ")
    if m in ("1", "2"): return int(m) - 1
    print("Escribe 1 o 2")

def ingresar():
  titulo("PASO 1/4: NUMERADOR")
  print("Factor por factor;")
  print("EXE vacio = fin.")
  print("Ej: 10  luego  s+3")
  N = factores("N", "10  o  s+3")
  titulo("PASO 2/4: DENOMINAD.")
  print("Factor por factor.")
  print("Ej: s   s+2   (s+1)^2")
  print("    s^2+2s+5")
  D = factores("D", "s+2  o  s^2+2s+5")
  titulo("PASO 3/4: PERIODO T")
  print("En segundos.")
  print("Ej: 0.1")
  T = pedir_T()
  titulo("PASO 4/4: METODO")
  print("1 = Z{G(s)} directa")
  print("2 = con ZOH:")
  print(" (1-z^-1)*Z{G(s)/s}")
  zo = pedir_metodo()
  return N, D, T, zo

def resumen(N, D, T, zo):
  LN[0] = 0
  titulo("REVISA TUS DATOS:")
  out("N(s)=" + ps(N, "s"))
  out("D(s)=" + ps(D, "s"))
  m = "directa"
  if zo: m = "con ZOH"
  out("T=" + fm(T) + "  " + m)

def ejemplo(N, D, T, zo, txt):
  titulo("EJEMPLO: se teclea")
  for s in txt: print(s)
  input("[EXE] calcular")
  resumen(N, D, T, zo); calc(N, D, T, zo)

def menu():
  while 1:
    titulo("== TRANSFORMADA Z ==")
    print("1) Ingresar G(s)")
    print("2) Ejemplo con ZOH")
    print("3) Ejemplo directo")
    print("0) Salir")
    op = input("Opcion? ")
    if op == "1":
      N, D, T, zo = ingresar()
      resumen(N, D, T, zo)
      if input("1=Calcular 2=Otra? ") != "2":
        calc(N, D, T, zo)
    elif op == "2":
      ejemplo([1.0], [1.0, 1.0, 0.0], 1.0, 1,
        ["G(s)=1/(s(s+1))", "N1? 1   N2? [EXE]",
         "D1? s   D2? s+1", "D3? [EXE]",
         "T? 1    Metodo? 2"])
    elif op == "3":
      ejemplo([4.0], [1.0, 2.0, 4.0], 0.5, 0,
        ["G(s)=4/(s^2+2s+4)", "N1? 4   N2? [EXE]",
         "D1? s^2+2s+4", "D2? [EXE]",
         "T? 0.5  Metodo? 1"])
    elif op == "0":
      return
    else:
      print("Opcion no valida"); continue
    input("[EXE] volver al menu")

menu()
