import os,json,urllib.request,zlib,base64,struct
D={2:(31,33,14,18,-31,-33,-14,-18),3:(15,17,-15,-17),4:(1,-1,16,-16),5:(1,-1,16,-16,15,17,-15,-17),6:(1,-1,16,-16,15,17,-15,-17)}
V=(0,100,320,335,500,950,20000)
B='c-mc2xo%TY5WU;G%Uf*c2^%G3At(hzLI}P9K}Cf`fkeR{@+DAEP*5ZiNRY)&Y{zfC`|!fjaGIkTY0jLPgU}y5t@80WTR-k37fMQFbWd5UyQ*mc>aMC{<djymXT&-x4Ehi6-oAeM>cyM)Po5ng?(RG~p5&YWk&?6My~jXkKq!Fcj3pdl|8MTYm-WT|XZ`Wy>Zr^PXn(n1-ameRG;>nzln+#9h~y)c`o{4@$y{&FEOy+iKDFLk*8bR>H`?3gviA^CppC|YOBIblQb<XnK|%>ZLXDW<49rp^g2Aj$>z-O$-)zX&Wqn0`EqgQGQ<u7&-r3qNAriG+mJ|Z##THKp5(5gA5FrswCuki_YwUH~xF$FqdJ}z&A@mkwf-tc*Ql4P&L(LgM-eHO<CEgN@Fvd<h6TA(2GM#K6u<^8*>>WHjEM`F!rJU`{#?m6+^4+Soz&vf{weB$r>xJ$dB;m9h4wQ6RJB%R!fiQ>;!Xe-YfN*p$&|m&tqk%E<_O=bt^>MK4qpQ$}@6D#O=9(bAJGy6v*hjl}cdJTkkbqq697G%qw!;oVRzAT@L<GG{bbWK-vaA^1lA1KnWX2PaDoxW&Sf2`&a_Z@A;5dLCT%Z_-{V_stwXq>uZNFtw|6F4}g3kN6+_)U;j%ID&*=kdp)df`7^Tqnyn0CI{=n7H)eW4lCB|l?TE>2c`Zw2WsQ9>$e5}Ao~HsdVIi(*pXo}_t^F{`~`D)C(%Dfj^GvZY{SJO2gaU2?J'
P=[x*2 for x in struct.unpack('768b',zlib.decompress(base64.b85decode(B)))]
M=[[]]+[list(P[i*64:(i+1)*64]) for i in range(0,12,2)]
E=[[]]+[list(P[i*64:(i+1)*64]) for i in range(1,12,2)]
def pa(f):
 a=f.split();b=[0]*128
 for r,w in enumerate(a[0].split('/')):
  x=0
  for c in w:
   if c.isdigit():x+=int(c)
   else:b[(7-r)*16+x]=' PNBRQK'.index(c.upper())*(1 if c.isupper() else -1);x+=1
 return b,1 if a[1]=='w' else -1,a[2],q(a[3]) if a[3]!='-' else -1,int(a[4])
def q(s):return ord(s[0])-97+(int(s[1])-1)*16
def uc(m):i,j,p=m;return chr(97+(i&7))+str((i>>4)+1)+chr(97+(j&7))+str((j>>4)+1)+(' pnbrqk'[p] if p else '')
def at(b,k,s):
 for d in(15,17):
  j=k-d*s
  if not j&136 and b[j]==s:return 1
 for d in D[2]:
  j=k+d
  if not j&136 and b[j]==2*s:return 1
 for d in D[6]:
  j=k+d;t=1
  while not j&136:
   p=b[j]
   if p:
    if p*s>0 and(abs(p)==5 or abs(p)==(4 if d in(1,-1,16,-16) else 3) or abs(p)==6 and t==1):return 1
    break
   j+=d;t+=1
 return 0
def mv(p):
 b,s,c,e,h=p
 for i,p_ in enumerate(b):
  if i&136 or p_*s<=0:continue
  t=abs(p_)
  if t==1:
   j=i+16*s
   if not b[j]:
    for r in((5,4,3,2)if j>>4 in(0,7)else(0,)):yield i,j,r
    k=j+16*s
    if i>>4==(1 if s==1 else 6)and not b[k]:yield i,k,0
   for d in(15,17):
    j=i+d*s
    if not j&136 and(b[j]*s<0 or j==e):
     for r in((5,4,3,2)if j>>4 in(0,7)else(0,)):yield i,j,r
  else:
   for d in D[t]:
    j=i+d
    while not j&136 and b[j]*s<=0:
     yield i,j,0
     if b[j] or t in(2,6):break
     j+=d
   if t==6 and not at(b,i,-s):
    for n,r in((1,'K'if s==1 else 'k'),(-1,'Q'if s==1 else 'q')):
     if r in c and not b[i+n] and not b[i+2*n]and(n==1 or not b[i-3])and not at(b,i+n,-s):yield i,i+2*n,0
def pl(p,m):
 b,s,c,e,h=p;i,j,r=m;p_=b[i];q_=b[j];b=b.copy();b[j]=s*r if r else p_;b[i]=0
 if abs(p_)==1 and j==e:b[j-16*s]=0
 if abs(p_)==6:
  c=c.replace('K'if s==1 else 'k','').replace('Q'if s==1 else 'q','')
  if abs(j-i)==2:r_=i+3 if j>i else i-4;b[(i+j)//2]=b[r_];b[r_]=0
 for k,r in((0,'Q'),(7,'K'),(112,'q'),(119,'k')):
  if i==k or j==k:c=c.replace(r,'')
 return b,-s,c,(i+j)//2 if abs(p_)==1 and abs(j-i)==32 else -1,0 if q_ or abs(p_)==1 else h+1
def le(p):
 s=p[1]
 for m in mv(p):
  q_=pl(p,m)
  if not at(q_[0],q_[0].index(6*s),-s):yield m,q_
def ev(p):
 b,s,c,e,h=p;m=0;e_=0;f=0
 for i,p_ in enumerate(b):
  if not p_ or i&136:continue
  t=abs(p_);d=1 if p_>0 else -1;f+=(0,0,1,1,2,4,0)[t];r=i>>4 if d==1 else 7-(i>>4);x=(7-r)*8+(i&7);m+=d*((0,82,337,365,477,1025,20000)[t]+M[t][x]);e_+=d*((0,94,281,297,512,936,20000)[t]+E[t][x])
 f=min(24,f);return(((m*f)+(e_*(24-f)))//24)*s+10
def se(p,d,a,z,y,k):
 global n,tt,h,v
 n+=1
 if n>36000:raise StopIteration
 b,s,c,e,h_=p;ky=(tuple(b),s,c,e);ck=at(b,b.index(s*6),-s)
 if h_>=100 or ky in k:return -29000+y if ck and not any(le(p))else 0
 if y>24:return ev(p)
 et=tt.get(ky);bm=et[3]if et else None
 if et and et[0]>=d and y and(et[2]==0 or et[2]==1 and et[1]>=z or et[2]==-1 and et[1]<=a):return et[1]
 if d>=3 and y and not ck and ev(p)>=z and any(p_*s in(2,3,4,5)for p_ in b):
  if -se((b,-s,c,-1,h_+1),d-3,-z,1-z,y+1,k)>=z:return z
 if d<=0 and not ck:
  v_=ev(p)
  if v_>=z:return v_
  a=max(a,v_)
 else:v_=-30000+y
 def sm(m):
  if m==bm:return 1e6
  i,j,r=m;t=abs(b[j])
  if t:return 1e5+V[t]*10-V[abs(b[i])]+r*100
  return h.get((s,i,j),0)
 o=sorted(mv(p),key=sm,reverse=True);c_=0;w=None
 for m in o:
  i,j,r=m
  if d<=0 and not ck and not b[j]and j!=e and not r:continue
  q_=pl(p,m)
  if at(q_[0],q_[0].index(s*6),-s):continue
  c_+=1
  if c_>1 and d>=3 and not ck and not b[j]and not r:
   sr=-se(q_,d-2,-a-1,-a,y+1,k|{ky})
   if sr>a:sr=-se(q_,d-1,-z,-a,y+1,k|{ky})
  else:sr=-se(q_,d-1,-z,-a,y+1,k|{ky})
  if sr>v_:v_=sr;w=m
  if sr>a:
   a=sr
   if y==0:v=m
   if not b[j]:h[(s,i,j)]=h.get((s,i,j),0)+d*d
  if a>=z:break
 if c_==0 and(d>0 or ck):return -29000+y if ck else 0
 if d>0:tt[ky]=(d,v_,1 if v_>=z else 0,w)
 return v_
def ch(p):
 global n,tt,h,v
 n=0;tt={};h={};v=next(le(p))[0];bt=v
 for d in range(1,16):
  try:se(p,d,-30000,30000,0,set());bt=v
  except StopIteration:break
 return bt
def mn():
 u=os.environ['MAKEFUN_ENV_URL']
 ps=lambda r,d:json.load(urllib.request.urlopen(urllib.request.Request(u+r,json.dumps(d).encode(),{'Content-Type':'application/json'}),timeout=120))
 g=ps('/game',{})
 while g['status']!='done':
  if g['status']=='over':g=ps('/game',{});continue
  m=uc(ch(pa(g['fen'])))
  g=ps('/move',{'game':g['game'],'move':m if m in g['legal_moves'] else g['legal_moves'][0]})
if __name__=='__main__':mn()

parse=pa
uci=uc
legal=le
choose=ch
