# LAZO: polinomios y lazo cerrado
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
def PA(a,b):
  n=max(len(a),len(b))
  a=[0.0]*(n-len(a))+a
  b=[0.0]*(n-len(b))+b
  return [a[i]+b[i] for i in range(n)]
P("LAZO CERRADO / POLIN.")
while 1:
  P("1 multiplicar polin.")
  P("2 N1/D1 +- N2/D2")
  P("3 C/R=G/(1+GH)")
  o=int(RN("opcion (0 fin)? "))
  if o==0: break
  if o==1:
    P("factores con *")
    P("ej: 1,0.2*1,-0.5")
    P(" ="+LS(RL("polin? ")))
  elif o==2:
    a=RL("N1? ")
    b=RL("D1? ")
    c=RL("N2? ")
    d=RL("D2? ")
    g=1
    if int(RN("1 suma 2 resta? "))==2: g=-1
    P("N=N1*D2 +- N2*D1")
    P(" ="+LS(PA(PM(a,d),[g*v for v in PM(c,b)])))
    P("D=D1*D2")
    P(" ="+LS(PM(b,d)))
  elif o==3:
    P("G directo, H realim.")
    P("(H=1: teclee 1)")
    a=RL("num G? ")
    b=RL("den G? ")
    c=RL("num H? ")
    d=RL("den H? ")
    K=RN("K (1 si no hay)? ")
    P("num C/R=K*nG*dH")
    P(" ="+LS([K*v for v in PM(a,d)]))
    p0=PM(b,d)
    p1=PM(a,c)
    P("P=dG*dH+K*nG*nH")
    P("P0=dG*dH:")
    P(" "+LS(p0))
    P("P1=nG*nH:")
    P(" "+LS(p1))
    P("P(z) con K="+F(K)+":")
    P(" "+LS(PA(p0,[K*v for v in p1])))
