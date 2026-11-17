# JURY: estabilidad P(z), K numerico
from math import sqrt,pi,cos,sin
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
ok=[1]
def V(t):
  if not t: ok[0]=0
  return " OK" if t else " NO"
P("JURY P(z)=0")
c=RL("P z^n..z^0? ")
n=len(c)-1
if c[0]<0:
  c=[-v for v in c]
  P("(P por -1: an>0)")
P("n="+str(n)+" P: "+LS(c))
R=[c[n-i] for i in range(n+1)]
P("1) |a0|<an")
P(" "+F(abs(R[0]))+"<"+F(R[n])+V(abs(R[0])<R[n]))
s=0.0
u=0.0
for i in range(n+1):
  s+=R[i]
  u+=R[i]*(1-2*(i%2))
P("2) P(1)>0")
P(" P(1)="+F(s)+V(s>0))
w=u*(1-2*(n%2))
P("3) (-1)^n P(-1)>0")
P(" P(-1)="+F(u))
P(" (-1)^n P(-1)="+F(w)+V(w>0))
if n>2:
  P("Arreglo z^0..z^"+str(n))
  P("F1: "+LS(R))
  P("F2: "+LS(c))
L="bcdefgh"
q=0
k=4
while len(R)>3:
  m=len(R)-1
  N=[]
  for j in range(m):
    v=R[0]*R[j]-R[m]*R[m-j]
    N.append(v)
    P(L[q]+str(m-1-j)+"=("+F(R[0])+")("+F(R[j])+")-("+F(R[m])+")("+F(R[m-j])+")")
    P(" ="+F(v))
  P("F"+str(2*q+3)+": "+LS(N))
  if m>3:
    P("F"+str(2*q+4)+": "+LS([N[m-1-j] for j in range(m)]))
  P(str(k)+") |"+L[q]+str(m-1)+"|>|"+L[q]+"0|")
  P(" "+F(abs(N[0]))+">"+F(abs(N[m-1]))+V(abs(N[0])>abs(N[m-1])))
  R=N
  q+=1
  k+=1
P("=> ESTABLE" if ok[0] else "=> INESTABLE")
P("Raices y modulo:")
for (x,y) in RT(c):
  P(CS(x,y))
  P(" |z|="+F(sqrt(x*x+y*y)))
