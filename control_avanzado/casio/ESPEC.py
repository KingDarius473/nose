# ESPEC: especificaciones <-> polo z
from math import sqrt,pi,cos,sin,exp,log,atan2
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
def ZO(os):
  l=log(os/100)
  z=-l/sqrt(pi*pi+l*l)
  P("L=ln(%OS/100)="+F(l))
  P("zeta=-L/sqrt(pi^2+L^2)")
  P(" ="+F(z))
  return z
P("1 ts,muestras/osc")
P("2 %OS,tp   3 %OS,ts")
P("4 zeta,wn  5 polo z")
P("6 P(z) lazo cerrado")
o=int(RN("opcion? "))
T=RN("T? ")
if o==1:
  ts=RN("ts? ")
  N=RN("muestras/osc? ")
  s=4/ts
  P("zeta*wn=4/ts="+F(s))
  th=2*pi/N
  P("ang z=2pi/N="+F(th))
  wd=th/T
  P("wd=ang/T="+F(wd))
  wn=sqrt(s*s+wd*wd)
  P("wn=sqrt(s^2+wd^2)")
  z=s/wn
elif o==2:
  z=ZO(RN("%OS? "))
  tp=RN("tp? ")
  wd=pi/tp
  P("wd=pi/tp="+F(wd))
  wn=wd/sqrt(1-z*z)
  P("wn=wd/sqrt(1-zeta^2)")
elif o==3:
  z=ZO(RN("%OS? "))
  ts=RN("ts? ")
  wn=4/(z*ts)
  P("wn=4/(zeta*ts)")
elif o==4:
  z=RN("zeta? ")
  wn=RN("wn? ")
else:
  if o==5:
    x=RN("Re z? ")
    y=RN("Im z? ")
  else:
    x=0.0
    y=0.0
    b=-1.0
    P("Polos:")
    for (u,v) in RT(RL("P z^n..z^0? ")):
      P(" "+CS(u,v))
      m=u*u+v*v
      if v>0: m+=1e6
      if v>=0 and m>b:
        b=m
        x=u
        y=v
    P("Dominante:")
    P(" "+CS(x,y))
  r=sqrt(x*x+y*y)
  th=atan2(abs(y),x)
  P("|z|="+F(r))
  P("ang z="+F(th)+" rad")
  s=-log(r)/T
  P("zeta*wn=-ln|z|/T")
  P(" ="+F(s))
  wd=th/T
  P("wd=ang/T="+F(wd))
  wn=sqrt(s*s+wd*wd)
  P("wn=sqrt(s^2+wd^2)")
  z=s/wn
  P("zeta=(zeta*wn)/wn")
P("zeta="+F(z))
P("wn="+F(wn)+" rad/s")
s=z*wn
P("ts=4/(zeta*wn)")
if s>0: P(" ="+F(4/s))
else: P(" inestable")
if abs(z)<1:
  wd=wn*sqrt(1-z*z)
  P("wd=wn*sqrt(1-zeta^2)")
  P(" ="+F(wd))
  P("tp=pi/wd="+F(pi/wd))
  P("%OS=100e^(-zeta*pi/sqrt(1-zeta^2))")
  P(" ="+F(100*exp(-pi*s/wd)))
else:
  wd=0.0
  P("zeta>=1: sin oscilar")
r=exp(-T*s)
th=T*wd
P("|z|=e^(-T*zeta*wn)")
P(" ="+F(r))
P("ang z=T*wd="+F(th))
P(" ="+F(th*180/pi,2)+" grados")
if th>0:
  P("muestras/osc=2pi/ang")
  P(" ="+F(2*pi/th))
P("z=|z|cos +-j|z|sin")
P("Re="+F(r*cos(th)))
P("Im=+-"+F(r*sin(th)))
