# ERRZ: constantes de error (realim. unitaria)
_c=[0]
def P(s):
  s=str(s)
  k=(len(s)+20)//21
  if _c[0]+k>6:
    input("[EXE]")
    _c[0]=1
  _c[0]+=k
  print(s)
def F(x,d=4):
  if x!=x: return "nan"
  if abs(x)>1e12: return "inf"
  if abs(x)>=1e5: return str(x)
  if d==4 and 0<abs(x)<0.01: d=7
  m=10**d
  n=int(abs(x)*m+0.5)
  s=str(n//m)
  r=n%m
  if r:
    t=str(r)
    t="0"*(d-len(t))+t
    while t[-1]=="0": t=t[:-1]
    s+="."+t
  if x<0 and n: s="-"+s
  return s
def LS(c):
  return ",".join([F(v) for v in c])
def NU(t):
  if "/" in t:
    a=t.split("/")
    return float(a[0])/float(a[1])
  return float(t)
def RN(q):
  while 1:
    try:
      v=NU(input(q))
      _c[0]=1
      return v
    except (ValueError,ZeroDivisionError):
      print("? repita")
def PM(a,b):
  r=[0.0]*(len(a)+len(b)-1)
  for i in range(len(a)):
    for j in range(len(b)):
      r[i+j]+=a[i]*b[j]
  return r
def RL(q):
  while 1:
    try:
      r=[1.0]
      for g in input(q).replace(";","*").split("*"):
        r=PM(r,[NU(t) for t in g.split(",")])
      while len(r)>1 and r[0]==0: r=r[1:]
      _c[0]=1
      return r
    except (ValueError,ZeroDivisionError):
      print("? repita")
def E1(c):
  s=0.0
  for v in c: s+=v
  return s
P("ERRORES e_ss")
P("G(z) lazo abierto")
a=RL("num G? ")
b=RL("den G? ")
T=RN("T (1 si no hay)? ")
N=0
while len(b)>1 and abs(E1(b))<1e-9:
  r=[b[0]]
  for i in range(1,len(b)-1): r.append(r[-1]+b[i])
  b=r
  N+=1
P("Polos en z=1: "+str(N))
P("=> sistema tipo "+str(N))
n1=E1(a)
d1=E1(b)
if N:
  P("den sin (z-1)^"+str(N)+":")
  P(" "+LS(b))
P("num(1)="+F(n1))
P("den'(1)="+F(d1))
g=n1/d1
I=1e99
P("Kp=lim G(z), z->1")
if N==0:
  kp=g
  P(" ="+F(n1)+"/"+F(d1))
else: kp=I
P(" Kp="+F(kp))
P("Kv=lim (z-1)G(z)/T")
if N==0: kv=0.0
elif N==1:
  kv=g/T
  P(" ="+F(n1)+"/("+F(d1)+"*"+F(T)+")")
else: kv=I
P(" Kv="+F(kv))
P("Ka=lim (z-1)^2 G/T^2")
if N<2: ka=0.0
elif N==2: ka=g/T/T
else: ka=I
P(" Ka="+F(ka))
def EE(k):
  if k==0: return "inf"
  if k>1e90: return "0"
  return F(1/k)
P("Escalon: 1/(1+Kp)")
if kp>1e90: P(" ess=0")
else: P(" ess="+F(1/(1+kp)))
P("Rampa: 1/Kv")
P(" ess="+EE(kv))
P("Parabola: 1/Ka")
P(" ess="+EE(ka))
P("(valido si el lazo cerrado es estable)")
