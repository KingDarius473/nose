# ZMOTOR.py - Motor de calculo de TRANSZ.py (fx-CG50).
# NO hace falta abrir ni modificar este archivo.
# Debe estar en la misma carpeta que TRANSZ.py.
from math import *
LN=[0]; Z0=(0.0,0.0)
def out(s):
  s=str(s)
  while 1:
    if LN[0]>=6: input("[EXE] sigue"); LN[0]=0
    print(s[:21]); LN[0]+=1; s=s[21:]
    if not s: break
def fd(x,d):
  s=str(int(x*10**d+0.5))
  if d>0:
    while len(s)<=d: s="0"+s
    s=s[:-d]+"."+s[-d:]
    while s[-1]=="0": s=s[:-1]
    if s[-1]==".": s=s[:-1]
  return s
def fm(x):
  if x<0: return "-"+fm(-x)
  if x<1e-13: return "0"
  e=int(floor(log10(x)))
  if e<-4 or e>6:
    s=fd(x/10.0**e,4)
    if s=="10": s="1"; e+=1
    return s+"e"+str(e)
  return fd(x,max(5-e,0))
def sg(x):
  if x<0: return "-"+fm(-x)
  return "+"+fm(x)
def fc(c):
  if abs(c[1])<1e-13: return fm(c[0])
  return fm(c[0])+sg(c[1])+"j"
def ps(p,v="z"):
  s=""; n=len(p)-1
  for i in range(n+1):
    c=p[i]
    if abs(c)<1e-13: continue
    t=fm(abs(c))
    if i<n:
      if t=="1": t=""
      t+=v
      if n-i>1: t+="^"+str(n-i)
    if c<0: s+="-"
    elif s: s+="+"
    s+=t
  return s or "0"
def pk(k):
  if k>1: return "^"+str(k)
  return ""
def cm(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cdv(a,b):
  d=b[0]*b[0]+b[1]*b[1]
  if d==0: d=1e-300
  return ((a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d)
def cab(a): return sqrt(a[0]*a[0]+a[1]*a[1])
def pm(a,b):
  r=[0.0]*(len(a)+len(b)-1)
  for i in range(len(a)):
    for j in range(len(b)): r[i+j]+=a[i]*b[j]
  return r
def pw(b,q,m):
  # b(z)*(z-q)^m, coef. complejos descendentes
  for k in range(m):
    r=b+[Z0]
    for i in range(len(b)):
      t=cm(b[i],q); r[i+1]=(r[i+1][0]-t[0],r[i+1][1]-t[1])
    b=r
  return b
def padd(a,b):
  if len(a)<len(b): a,b=b,a
  r=a[:]; d=len(a)-len(b)
  for i in range(len(b)): r[i+d]=(a[i+d][0]+b[i][0],a[i+d][1]+b[i][1])
  return r
def pev(p,x):
  r=Z0
  for c in p: r=cm(r,x); r=(r[0]+c[0],r[1]+c[1])
  return r
def der(p):
  n=len(p)-1; return [(p[i][0]*(n-i),p[i][1]*(n-i)) for i in range(n)]
def st(p):
  while len(p)>1 and p[0]==0: p=p[1:]
  return p
def roots(P):
  # raices de P real (Durand-Kerner): [[re,im,mult],..], im>0 = par conj.
  P=P[:]; R=[]; m=0
  while len(P)>1 and P[-1]==0: P.pop(); m+=1
  if m: R.append([0.0,0.0,m])
  n=len(P)-1
  if n<1: return R,1
  c=[(x/P[0],0.0) for x in P]; r=abs(c[n][0])**(1.0/n)
  z=[(r*cos(2*pi*k/n+0.4),r*sin(2*pi*k/n+0.4)) for k in range(n)]
  for it in range(120):
    dm=0
    for i in range(n):
      d=(1.0,0.0)
      for j in range(n):
        if j!=i: d=cm(d,(z[i][0]-z[j][0],z[i][1]-z[j][1]))
      s=cdv(pev(c,z[i]),d); z[i]=(z[i][0]-s[0],z[i][1]-s[1])
      dm=max(dm,cab(s))
    if dm<1e-13*r: break
  for tl in (0.003,1e-4,0):
    Rg,ok=grp(z,c,P,r,tl)
    if ok: break
  return R+Rg,ok
def grp(z,c,P,r,tl):
  # agrupa repetidas (tol. tl), pule (Newton en derivada) y verifica
  G=[]; R=[]
  for x in z:
    f=0
    for g in G:
      if cab((x[0]-g[0]/g[2],x[1]-g[1]/g[2]))<tl*(r+cab(x)):
        g[0]+=x[0]; g[1]+=x[1]; g[2]+=1; f=1
        break
    if not f: G.append([x[0],x[1],1])
  B=[P[0]]
  for g in G:
    x=(g[0]/g[2],g[1]/g[2]); d=c
    for i in range(g[2]-1): d=der(d)
    e=der(d)
    for i in range(8): s=cdv(pev(d,x),pev(e,x)); x=(x[0]-s[0],x[1]-s[1])
    a=x[0]; w=x[1]
    if abs(w)<1e-8*(r+abs(a)): w=0.0
    if w>=0:
      R.append([a,w,g[2]]); f=[1.0,-a]
      if w: f=[1.0,-2*a,a*a+w*w]
      for i in range(g[2]): B=pm(B,f)
  ok=len(B)==len(P)
  if ok:
    e=0; s=0
    for i in range(len(P)): e=max(e,abs(B[i]-P[i])); s=max(s,abs(P[i]))
    ok=e<1e-9*s
  return R,ok
def res(p,m,PL,N,a0):
  # coef. de 1/(s-p)^k, k=1..m: serie de Taylor de N/Q en s=p
  Q=[(a0,0.0)]
  for r in PL:
    if r[0]!=p: Q=pw(Q,(r[0][0]-p[0],r[0][1]-p[1]),r[1])
  f=[]
  for i in range(m):
    x=Z0; q=[]
    for c in N: x=cm(x,p); x=(x[0]+c[0],x[1]+c[1]); q.append(x)
    if q: q.pop()
    N=q
    for j in range(1,min(i,len(Q)-1)+1):
      t=cm(Q[-1-j],f[i-j]); x=(x[0]-t[0],x[1]-t[1])
    f.append(cdv(x,Q[-1]))
  f.reverse(); return f
def zt(c,q,k,T):
  # numerador de Z{c/(s-p)^k}; denominador (z-q)^k, q=e^(pT)
  if k==1: return [c,Z0]
  n=k-1; f=T**n; e=[1]
  for m in range(2,n+1):
    f/=m; e=[0]+e+[0]; e=[(m-j)*e[j]+(j+1)*e[j+1] for j in range(m)]
  r=[]; w=(c[0]*f,c[1]*f)
  for j in range(n): w=cm(w,q); r.append((w[0]*e[j],w[1]*e[j]))
  r.append(Z0); return r
def lst(p):
  s=""
  for x in p:
    if s: s+=","
    s+=fm(x)
  return s
def prt(R,nm):
  i=1
  for r in R:
    s=nm+str(i)+"="+fm(r[0]); i+=1
    if r[1]:
      s=nm+str(i-1)+","+str(i)+"="+fm(r[0])+"+/-"+fm(abs(r[1]))+"j"
      i+=1
    if r[2]>1: s+=" (x"+str(r[2])+")"
    out(s)
def calc(N,D,T,zo,R=None):
  # N,D: coef. de N(s),D(s) (potencias descendentes); zo=1 con ZOH
  LN[0]=0
  if len(N)>=len(D)+zo:
    out("Grado de N(s) muy");out("alto: G(s) no es");out("propia. Revisa datos"); return
  ok=1
  if R is None: R,ok=roots(D)
  if zo:
    out("ZOH: G(z)=(1-z^-1)*Z{G(s)/s}"); out("Se expande G(s)/s"); f=0
    for r in R:
      if r[0]==0 and r[1]==0: r[2]+=1; f=1
    if not f: R=[[0.0,0.0,1]]+R
  out("-- Polos en s --"); prt(R,"p")
  if not ok: out("AVISO: polos dudosos")
  # PL: [polo s, mult, polo z=e^(pT), mult en G(z)] con conjugados
  PL=[]
  for r in R:
    e=exp(r[0]*T); x=e*cos(r[1]*T); y=e*sin(r[1]*T); m=r[2]
    if zo and r[0]==0 and r[1]==0: m-=1
    PL.append([(r[0],r[1]),r[2],(x,y),m])
    if r[1]: PL.append([(r[0],-r[1]),r[2],(x,-y),m])
  out("-- Fracc. parciales y tabla Z --"); Nc=[(x,0.0) for x in N]
  NZ=[Z0]; mx=0; tn=0
  for r in R:
    p=(r[0],r[1]); m=r[2]; a=-r[0]; w=r[1]
    C=res(p,m,PL,Nc,D[0]); E=exp(-a*T); q=(E*cos(w*T),E*sin(w*T))
    if w: out("Par s="+fm(-a)+"+/-"+fm(w)+"j"); out("a="+fm(a)+" w="+fm(w))
    elif a: out("Polo s="+fm(-a)+": a="+fm(a))
    else: out("Polo s=0")
    if a: out("E=e^(-aT)="+fm(E))
    if w: out("cw=cos(wT)="+fm(cos(w*T))); out("sw=sin(wT)="+fm(sin(w*T)))
    for k in range(1,m+1):
      tn+=1; c=C[k-1]; t=zt(c,q,k,T); h="T"+str(tn)+": "
      if w:
        if m==1:
          out(h+"(B(s+a)+C*w)/((s+a)^2+w^2)")
          out("B="+fm(2*c[0])+" C="+fm(-2*c[1]))
          out("g(t)=e^(-at)*(B*cos(wt)+C*sin(wt))")
          out("->z(B(z-E*cw)+C*E*sw)/(z^2-2E*cw*z+E^2)")
        else:
          out(h+"R/(s-p)^"+str(k)+" + conj."); out("R="+fc(c))
          out("->tabla t^n*e^(pt)/n!, n="+str(k-1))
        t=pw(t,(q[0],-q[1]),k)
        out("=("+ps([2*x[0] for x in t])+")/("+ps([1.0,-2*q[0],E*E])+")"+pk(k))
      else:
        sd="s"; es="1"; em=""
        if a: sd="(s"+sg(a)+")"; es="E"; em="E*"
        out(h+"A/"+sd+pk(k)+", A="+fm(c[0]))
        if k==1: out("->A*z/(z-"+es+")")
        elif k==2: out("->A*T*"+em+"z/(z-"+es+")^2")
        elif k==3: out("->A*T^2*"+em+"z(z+"+es+")/(2(z-"+es+")^3)")
        else: out("->A*T^n*"+em+"P(z)/(n!(z-"+es+")^"+str(k)+"), n="+str(k-1))
        out("=("+ps([x[0] for x in t])+")/(z"+sg(-E)+")"+pk(k))
    # suma al numerador comun (el polo y su conjugado)
    for sn in range(1+(w>0)):
      S=[Z0]
      for k in range(1,m+1):
        c=C[k-1]
        if sn: c=(c[0],-c[1])
        S=padd(S,pw(zt(c,q,k,T),q,m-k))
      for r2 in PL:
        if r2[0]!=p: S=pw(S,r2[2],r2[1])
      for x in S: mx=max(mx,abs(x[0]))
      NZ=padd(NZ,S); p=(p[0],-p[1]); q=(q[0],-q[1])
  DZ=[(1.0,0.0)]
  for r in PL: DZ=pw(DZ,r[2],r[3])
  if zo:
    out("-- ZOH --"); out("G(z)=(z-1)/z*suma(Ti)")
    out("se simplifican z y (z-1)"); NZ.pop()
  nz=[]; e=0
  for x in NZ:
    v=x[0]
    if abs(v)<1e-11*mx: v=0.0
    e=max(e,abs(v)); nz.append(v)
  nz=st(nz); dz=[x[0] for x in DZ]
  if e<1e-7*mx: out("AVISO: cancelacion fuerte, poca precision")
  out("== G(z)=N(z)/D(z) ==")
  for nm,p in (("N(z):",nz),("D(z):",dz)):
    out(nm)
    for i in range(len(p)): out(" z^"+str(len(p)-1-i)+": "+fm(p[i]))
  out("G(z)=("+ps(nz)+")/("+ps(dz)+")"); out("-- Polos en z --")
  prt([[r[2][0],r[2][1],r[3]] for r in PL if r[0][1]>=0 and r[3]>0],"z")
  out("-- Ceros en z --")
  if len(nz)>1:
    Zr,ok=roots(nz); prt(Zr,"c")
    if not ok: out("AVISO: ceros dudosos")
  else: out("ninguno")
  out("FIN"); return nz,dz
