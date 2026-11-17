# LGR: lugar de raices 1+K*G(z)=0
from math import sqrt,pi,cos,sin,log,atan2
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
def PV(c,x,y):
  a=0.0
  b=0.0
  for k in c:
    a,b=a*x-b*y+k,a*y+b*x
  return a,b
def RT(c):
  while len(c)>1 and c[0]==0: c=c[1:]
  n=len(c)-1
  if n<1: return []
  c=[k/c[0] for k in c]
  if n==1: return [(-c[1],0.0)]
  if n==2:
    d=c[1]*c[1]-4*c[2]
    h=-c[1]/2
    if d<0:
      g=sqrt(-d)/2
      return [(h,g),(h,-g)]
    g=sqrt(d)/2
    return [(h+g,0.0),(h-g,0.0)]
  m=0.0
  for k in c: m=max(m,abs(k))
  R=[]
  for k in range(n):
    t=0.4+2*pi*k/n
    R.append((m*cos(t),m*sin(t)))
  for q in range(300):
    d=0.0
    for i in range(n):
      x,y=R[i]
      a,b=PV(c,x,y)
      u=1.0
      v=0.0
      for j in range(n):
        if j!=i:
          e=x-R[j][0]
          g=y-R[j][1]
          u,v=u*e-v*g,u*g+v*e
      w=u*u+v*v
      if w==0: w=1e-30
      e=(a*u+b*v)/w
      g=(b*u-a*v)/w
      R[i]=(x-e,y-g)
      d+=abs(e)+abs(g)
    if d<1e-12: break
  for i in range(n):
    if abs(R[i][1])<1e-7: R[i]=(R[i][0],0.0)
  return R
def CS(u,v):
  if v==0: return F(u)
  return F(u)+("+j" if v>0 else "-j")+F(abs(v))
def CL(K):
  return RT(PA(dg,[K*v for v in ng]))
def MX(K):
  m=0.0
  for (u,v) in CL(K): m=max(m,u*u+v*v)
  return 1-1e-9-sqrt(m)
def DM(K):
  b=-1.0
  x=0.0
  y=0.0
  for (u,v) in CL(K):
    m=u*u+v*v
    if v>0: m+=1e6
    if v>=0 and m>b:
      b=m
      x=u
      y=v
  return x,y
def ZT(K):
  x,y=DM(K)
  r=sqrt(x*x+y*y)
  if r==0: return 1.0
  s=-log(r)
  t=atan2(y,x)
  if s==0 and t==0: return 0.0
  return s/sqrt(s*s+t*t)
def BS(f,a,b):
  t=f(a)>0
  for k in range(34):
    m=(a+b)/2
    if (f(m)>0)==t: a=m
    else: b=m
  return (a+b)/2
def SW(f,km):
  r=[]
  h=km/50
  a=f(h)>0
  for k in range(2,51):
    b=f(k*h)>0
    if a!=b: r.append(BS(f,(k-1)*h,k*h))
    a=b
  return r
def SH(K):
  for (u,v) in CL(K):
    P(" "+CS(u,v))
    P("  |z|="+F(sqrt(u*u+v*v)))
def FZ(K):
  return ZT(K)-z0
P("LGR 1+K*G(z)=0")
ng=RL("num G? ")
dg=RL("den G? ")
T=RN("T? ")
while 1:
  P("1 K critico")
  P("2 K para un zeta")
  P("3 polos para un K")
  o=int(RN("opcion (0 fin)? "))
  if o==0: break
  if o==3:
    K=RN("K? ")
    SH(K)
    P("zeta dom.="+F(ZT(K)))
    continue
  if o==2: z0=RN("zeta? ")
  km=RN("K max busq? ")
  P("Barriendo K...")
  if o==1:
    r=SW(MX,km)
    if not r: P("Sin cruce |z|=1")
    for K in r:
      P("K critico="+F(K))
      SH(K)
      x,y=DM(K)
      t=atan2(y,x)
      P(" ang="+F(t)+" rad")
      P(" w=ang/T="+F(t/T))
    P("Estable en K="+F(km/50)+"? "+("SI" if MX(km/50)>0 else "NO"))
  else:
    r=SW(FZ,km)
    if not r: P("No hay ese zeta")
    for K in r:
      P("K="+F(K))
      x,y=DM(K)
      P("z="+CS(x,y))
      P(" +- conjugado")
      m=sqrt(x*x+y*y)
      t=atan2(y,x)
      P("|z|="+F(m))
      P("ang="+F(t)+" rad")
      P(" ="+F(t*180/pi,2)+" grados")
      s=-log(m)/T
      wd=t/T
      P("zeta*wn=-ln|z|/T")
      P(" ="+F(s))
      P("wd=ang/T="+F(wd))
      P("wn="+F(sqrt(s*s+wd*wd)))
      P("muestras/ciclo=2pi/ang")
      P(" ="+F(2*pi/t))
