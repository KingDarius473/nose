# DISENO: condicion de angulo y magnitud
from math import sqrt,pi,cos,sin,exp,atan2,tan
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
def AN(a,b):
  return atan2(b,a)*180/pi
def E1(c):
  s=0.0
  for v in c: s+=v
  return s
P("DISENO ang/magnitud")
P("G(z): planta sin GD")
ng=RL("num G? ")
dg=RL("den G? ")
if int(RN("z1: 1=Re,Im 2=zeta,wn? "))==2:
  z=RN("zeta? ")
  wn=RN("wn? ")
  T=RN("T? ")
  r=exp(-T*z*wn)
  t=T*wn*sqrt(1-z*z)
  x=r*cos(t)
  y=r*sin(t)
  P("z1="+CS(x,y))
else:
  x=RN("Re z1? ")
  y=abs(RN("Im z1? "))
P("Angulos hacia z1:")
for (u,v) in RT(ng):
  P("cero "+CS(u,v)+": "+F(AN(x-u,y-v),2))
for (u,v) in RT(dg):
  P("polo "+CS(u,v)+": "+F(AN(x-u,y-v),2))
a,b=PV(ng,x,y)
c,d=PV(dg,x,y)
mg=sqrt((a*a+b*b)/(c*c+d*d))
ag=(AN(a,b)-AN(c,d)+180)%360-180
P("ang G=ceros-polos")
P(" ="+F(ag,2)+" grados")
P("|G(z1)|="+F(mg))
ph=(360-ag)%360-180
P("Deficiencia:")
P("phi=180-ang G(+-360)")
P(" ="+F(ph,2)+" grados")
if abs(ph)<1:
  P("Basta ganancia K:")
  P("K=1/|G|="+F(1/mg))
else:
  P("NO basta solo K")
  P("(GD debe aportar phi)")
while 1:
  P("GD=K(z-a)/(z-p):")
  P("1 PD (p=0) 2 PI (p=1)")
  P("3 K1(1-z^-1)+K2")
  o=int(RN("opcion (0 fin)? "))
  if o==0: break
  p=0.0
  if o==2: p=1.0
  t=AN(x-p,y)
  be=(ph+t)%360
  P("ang(z1-a)=phi+ang(z1-p)")
  P(" ="+F(ph,2)+"+"+F(t,2))
  P(" ="+F(be,2)+" (mod 360)")
  if be<0.01 or be>179.99:
    P("No factible: el cero no puede dar ese angulo")
    continue
  a=x-y/tan(be*pi/180)
  P("a=Re-Im/tan(ang)")
  P(" ="+F(a))
  K=sqrt((x-p)*(x-p)+y*y)/(sqrt((x-a)*(x-a)+y*y)*mg)
  P("K=|z1-p|/(|z1-a||G|)")
  P(" ="+F(K))
  s="(z-"+F(a)+")"
  if a<0: s="(z+"+F(-a)+")"
  P("GD="+F(K)+s+("/z" if o!=2 else "/(z-1)"))
  if o==1:
    P("KP=K(1-a)="+F(K*(1-a)))
    P("KD=K*a="+F(K*a))
  elif o==2:
    P("KP=K*a="+F(K*a))
    P("KI=K(1-a)="+F(K*(1-a)))
  else:
    P("K1=K*a="+F(K*a))
    P("K2=K(1-a)="+F(K*(1-a)))
  if a<0 or a>1: P("OJO: ganancia negativa")
  P("Polos lazo cerrado:")
  nn=[K*v for v in PM(ng,[1.0,-a])]
  dd=PM(dg,[1.0,-p])
  for (u,v) in RT(PA(dd,nn)):
    P(" "+CS(u,v))
    P("  |z|="+F(sqrt(u*u+v*v)))
  d1=E1(dd)
  if abs(d1)<1e-9:
    P("Kp=inf, ess escalon=0")
  else:
    kp=E1(nn)/d1
    P("Kp=GD(1)G(1)="+F(kp))
    P("ess=1/(1+Kp)="+F(1/(1+kp)))
