# JURYK: rango de K, P=P0+K*P1
from math import sqrt
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
def PK(c):
  s=""
  for i in range(len(c)):
    if abs(c[i])>1e-12:
      t=F(c[i])
      if i:
        if abs(abs(c[i])-1)<1e-12: t=t[:-1]
        t+="K"
      if i>1: t+="^"+str(i)
      if s and c[i]>0: s+="+"
      s+=t
  return s or "0"
def SB(a,b,g):
  n=max(len(a),len(b))
  a=a+[0.0]*(n-len(a))
  b=b+[0.0]*(n-len(b))
  return [a[i]+g*b[i] for i in range(n)]
def LN(c):
  if abs(c[1])<1e-12:
    P(" siempre" if c[0]>0 else " nunca")
  else:
    P(" K"+(">" if c[1]>0 else "<")+F(-c[0]/c[1]))
def QR(c):
  while len(c)>1 and abs(c[-1])<1e-12: c=c[:-1]
  if len(c)==2: return [-c[0]/c[1]]
  if len(c)==3:
    d=c[1]*c[1]-4*c[2]*c[0]
    if d>=0:
      d=sqrt(d)
      return [(-c[1]-d)/(2*c[2]),(-c[1]+d)/(2*c[2])]
  return []
def G(K):
  R=[A[i]+K*B[i] for i in range(n+1)]
  if R[n]<0: R=[-v for v in R]
  s=0.0
  t=0.0
  for i in range(n+1):
    s+=R[i]
    t+=R[i]*(1-2*(i%2))
  g=[R[n]-abs(R[0]),s,t*(1-2*(n%2))]
  while len(R)>3:
    m=len(R)-1
    R=[R[0]*R[j]-R[m]*R[m-j] for j in range(m)]
    g.append(abs(R[0])-abs(R[m-1]))
  g.append(min(g))
  return g
def BS(i,a,b):
  t=G(a)[i]>0
  for k in range(34):
    m=(a+b)/2
    if (G(m)[i]>0)==t: a=m
    else: b=m
  return (a+b)/2
def IV(i):
  r=[]
  a=None
  for k in range(NS+1):
    v=W[k][i]>0
    if v and a is None:
      a=K1
      if k: a=BS(i,K1+(k-1)*h,K1+k*h)
    if a is not None and not v:
      r.append(F(a)+"<K<"+F(BS(i,K1+(k-1)*h,K1+k*h)))
      a=None
  if a is not None: r.append(F(a)+"<K<"+F(K2))
  if not r: return " ninguno"
  return " "+" o ".join(r)
P("JURY K: P=P0+K*P1")
p0=RL("P0 (sin K)? ")
p1=RL("P1 (x K)? ")
n=max(len(p0),len(p1))-1
A=[0.0]*(n+1)
B=[0.0]*(n+1)
for i in range(len(p0)): A[i]=p0[len(p0)-1-i]
for i in range(len(p1)): B[i]=p1[len(p1)-1-i]
K1=RN("K min busq? ")
K2=RN("K max busq? ")
R=[[A[i],B[i]] for i in range(n+1)]
P("P(z), n="+str(n)+":")
for i in range(n,-1,-1):
  P(" z^"+str(i)+": "+PK(R[i]))
P("1) |a0|<an")
P(" a0="+PK(R[0]))
P(" an="+PK(R[n]))
if abs(B[n])<1e-12 and abs(B[0])>1e-12 and A[n]>0:
  u=(-A[n]-A[0])/B[0]
  v=(A[n]-A[0])/B[0]
  P(" "+F(min(u,v))+"<K<"+F(max(u,v)))
s=[0.0,0.0]
t=[0.0,0.0]
for i in range(n+1):
  s=SB(s,R[i],1)
  t=SB(t,R[i],(1-2*(i%2))*(1-2*(n%2)))
P("2) P(1)>0")
P(" P(1)="+PK(s))
LN(s)
P("3) (-1)^n P(-1)>0")
P(" ="+PK(t))
LN(t)
if n>2:
  P("Arreglo z^0..z^"+str(n))
  P(" F1: a0..an")
  P(" F2: an..a0")
L="bcdefgh"
q=0
while len(R)>3:
  m=len(R)-1
  N=[SB(PM(R[0],R[j]),PM(R[m],R[m-j]),-1) for j in range(m)]
  P("Fila "+str(2*q+3)+":")
  for j in range(m):
    P(L[q]+str(m-1-j)+"="+PK(N[j]))
  P(str(q+4)+") |"+L[q]+str(m-1)+"|>|"+L[q]+"0|")
  z=QR(SB(N[0],N[m-1],-1))+QR(SB(N[0],N[m-1],1))
  if z:
    z.sort()
    P(" K criticos:")
    P(" "+LS(z))
  R=N
  q+=1
NS=200
h=(K2-K1)/NS
P("Barriendo K...")
W=[G(K1+k*h) for k in range(NS+1)]
P("Cumple (en busqueda)")
for i in range(len(W[0])-1):
  P("C"+str(i+1)+":"+IV(i))
P("=> ESTABLE si:")
P(IV(len(W[0])-1))
