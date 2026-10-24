import csv, sys, re, openpyxl
from datetime import datetime, timedelta
from collections import Counter
D=sys.argv[1]
cat={r["id_celda"] for r in csv.DictReader(open(f"{D}/catalogo_antenas_sintetico.csv",encoding="utf-8"))}
def norm(n):
    d=re.sub(r"\D","",n or "")
    if d.startswith("52") and len(d)==12: d=d[2:]
    return d
R=[]
for i,r in enumerate(csv.DictReader(open(f"{D}/operador_A_sintetico.csv",encoding="utf-8")),start=2):
    try: t=datetime.strptime(r["FECHA"]+" "+r["HORA"],"%d/%m/%Y %H:%M:%S")
    except ValueError: t=None
    R.append(("A",i,t,norm(r["NUM_ORIGEN"]),norm(r["NUM_DESTINO"]),r["TIPO"],r["DURACION"],r["CELDA"],tuple(r.values())))
ws=openpyxl.load_workbook(f"{D}/operador_B_sintetico.xlsx").active
rows=list(ws.iter_rows(values_only=True))
for i,v in enumerate(rows[1:],start=2):
    v=["" if x is None else str(x) for x in v]
    try: t=datetime.strptime(v[0],"%Y-%m-%d %H:%M:%S")-timedelta(hours=6)
    except ValueError: t=None
    R.append(("B",i,t,norm(v[1]),norm(v[2]),v[3],v[4],v[5].replace("/","-"),tuple(v)))
T="6565550100"; P0,P1=datetime(2026,10,1),datetime(2026,10,11)
seen=set(); c=Counter(); valid=[]
for f,i,t,a,b,tp,du,ce,raw in R:
    if (f,raw) in seen: c["duplicado"]+=1; continue
    seen.add((f,raw))
    if t is None: c["fecha_invalida"]+=1; continue
    if not(P0<=t<P1): c["fuera_de_periodo"]+=1; continue
    if a!=T and len(a)!=10 or b and b!=T and len(b)!=10: c["numero_incompleto"]+=1; continue
    if tp in("VOZ SALIENTE","VOZ ENTRANTE","MOC","MTC") and (du=="" or int(du)<0): c["duracion_invalida"]+=1; continue
    if ce not in cat: c["celda_sin_catalogo"]+=1
    valid.append((t,a,b,tp,ce,f,i))
print("renglones",len(R),"| problemas",dict(c))
valid.sort()
for x,y in zip(valid,valid[1:]):
    if y[0]-x[0]>timedelta(hours=4): print("SILENCIO",x[0],"->",y[0],y[0]-x[0])
other=Counter((b if a==T else a) for t,a,b,tp,ce,f,i in valid if (b or a!=T))
print("top contactos",other.most_common(6))
print("top celdas",Counter(ce for *_,ce,f,i in [(v[0],v[1],v[2],v[3],v[4],v[5],v[6]) for v in valid]).most_common(5))
print("eventos válidos",len(valid),Counter(v[3] for v in valid))
