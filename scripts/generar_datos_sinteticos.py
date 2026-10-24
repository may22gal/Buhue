import random, csv, sys, os
from datetime import datetime, timedelta
import openpyxl
random.seed(20261024)
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
T = "6565550100"
def fmt(n): return f"{n[:3]}-{n[3:6]}-{n[6:]}"
# Catálogo sintético: A usa LAC 4120, B usa LAC 5011
CAT = [
 ("4120-10011","Celda Sintética Norte 01","Ciudad Juárez",31.7402,-106.4451),
 ("4120-10012","Celda Sintética Norte 02","Ciudad Juárez",31.7288,-106.4610),
 ("4120-10023","Celda Sintética Centro 01","Ciudad Juárez",31.7391,-106.4862),
 ("4120-10034","Celda Sintética Oriente 01","Ciudad Juárez",31.6945,-106.3870),
 ("4120-10045","Celda Sintética Sur 01","Ciudad Juárez",31.6511,-106.4302),
 ("4120-10056","Celda Sintética Poniente 01","Ciudad Juárez",31.7590,-106.5205),
 ("5011-20031","Celda Sintética Norte 03","Ciudad Juárez",31.7351,-106.4499),
 ("5011-20032","Celda Sintética Centro 02","Ciudad Juárez",31.7420,-106.4790),
 ("5011-20047","Celda Sintética Oriente 02","Ciudad Juárez",31.6880,-106.3952),
 ("5011-20058","Celda Sintética Sur 02","Ciudad Juárez",31.6603,-106.4188),
]
ORPH_A = ["4120-10099","4120-10102","4120-10140"]; ORPH_B = ["5011-20090","5011-20111"]
A_HOME,A_WORK,A_OTH = "4120-10011","4120-10034",["4120-10012","4120-10023","4120-10045","4120-10056"]
B_HOME,B_WORK,B_OTH = "5011-20031","5011-20047",["5011-20032","5011-20058"]
FREQ = [("6565550142",45),("6565550117",30),("6565550163",22),("6145550203",15),("6565550188",12)]
OCC = [f"656555{n:04d}" for n in range(101,200) if n not in (142,117,163,188,100)]
OCC = random.sample(OCC, 20)
contacts = [c for c,w in FREQ for _ in range(w)] + [c for c in OCC for _ in range(random.randint(1,3))] + ["8005550190"]*2
random.shuffle(contacts)
start = datetime(2026,10,1,0,0); switch = datetime(2026,10,6,12,0); end = datetime(2026,10,10,23,59)
SIL = [(datetime(2026,10,4,0,50),datetime(2026,10,4,7,20)),(datetime(2026,10,7,19,30),datetime(2026,10,8,9,30))]
def silent(t): return any(a<=t<b for a,b in SIL)
def cell(t):
    home,work,oth = (A_HOME,A_WORK,A_OTH) if t<switch else (B_HOME,B_WORK,B_OTH)
    if t.hour<7 or t.hour>=22: return home
    if t.weekday()<5 and 9<=t.hour<18: return work if random.random()<.75 else random.choice(oth)
    return random.choice([home]+oth)
ev=[]
# datos: sesión cada 55-110 min, sin silencios
t=start
while t<=end:
    if not silent(t): ev.append(dict(t=t,a=T,b="",tipo="DATOS",dur=random.randint(30,900)))
    t+=timedelta(minutes=random.randint(55,110))
# llamadas y SMS distribuidos en horario de actividad
ci=0
days=[start+timedelta(days=d) for d in range(10)]
per_day=[len(contacts)//10+(1 if i<len(contacts)%10 else 0) for i in range(10)]
for d,n in zip(days,per_day):
    for _ in range(n):
        while True:
            tt=d+timedelta(hours=random.randint(8,22),minutes=random.randint(0,59),seconds=random.randint(0,59))
            if not silent(tt) and tt<=end: break
        c=contacts[ci]; ci+=1
        k=random.choices(["LS","LE","SS","SE"],[35,30,20,15])[0]
        if k=="LS": ev.append(dict(t=tt,a=T,b=c,tipo="LS",dur=random.randint(12,420)))
        elif k=="LE": ev.append(dict(t=tt,a=c,b=T,tipo="LE",dur=random.randint(12,600)))
        elif k=="SS": ev.append(dict(t=tt,a=T,b=c,tipo="SS",dur=0))
        else: ev.append(dict(t=tt,a=c,b=T,tipo="SE",dur=0))
ev.sort(key=lambda e:e["t"])
for e in ev: e["cell"]=cell(e["t"]); e["err"]=""
A=[e for e in ev if e["t"]<switch]; B=[e for e in ev if e["t"]>=switch]
# Celdas sin catálogo (5 celdas, 9 renglones) en eventos válidos de día
def pick(lst,k,cond=lambda e:True):
    c=[e for e in lst if not e["err"] and cond(e)]; return random.sample(c,k)
for i,e in enumerate(pick(A,6,lambda e:8<=e["t"].hour<22)): e["cell"]=ORPH_A[i%3]; e["err"]="celda_sin_catalogo"
for i,e in enumerate(pick(B,3,lambda e:8<=e["t"].hour<22)): e["cell"]=ORPH_B[i%2]; e["err"]="celda_sin_catalogo"
# Números incompletos (3) y duraciones inválidas (2) en llamadas
for e,bad in zip(pick(A,2,lambda e:e["tipo"] in("LS","SS")),["65655501","+52 656 555"]): e["b"]=bad; e["err"]="numero_incompleto"
for e,bad in zip(pick(B,1,lambda e:e["tipo"]=="LE"),["656555014"]): e["a"]=bad; e["err"]="numero_incompleto"
for e in pick(A,1,lambda e:e["tipo"]=="LS"): e["dur"]=-35; e["err"]="duracion_invalida"
for e in pick(B,1,lambda e:e["tipo"]=="LE"): e["dur"]=None; e["err"]="duracion_invalida"
# Fuera del periodo autorizado (10)
def extra(base,n,cells,tag):
    out=[]
    for i in range(n):
        tt=base+timedelta(hours=random.randint(9,20),minutes=random.randint(0,59))
        c=random.choice([x for x,_ in FREQ]); out.append(dict(t=tt,a=T,b=c,tipo="LS",dur=random.randint(20,200),cell=random.choice(cells),err="fuera_de_periodo"))
    return out
A+=extra(datetime(2026,9,30),5,[A_HOME]+A_OTH,"x"); B+=extra(datetime(2026,10,11),5,[B_HOME]+B_OTH,"x")
A.sort(key=lambda e:e["t"]); B.sort(key=lambda e:e["t"])
TIPO_A={"LS":"VOZ SALIENTE","LE":"VOZ ENTRANTE","SS":"SMS SALIENTE","SE":"SMS ENTRANTE","DATOS":"DATOS"}
TIPO_B={"LS":"MOC","LE":"MTC","SS":"SMS-MO","SE":"SMS-MT","DATOS":"GPRS"}
def b_num(n):
    if n and len(n)==10 and n.isdigit(): return "+52 "+fmt(n)
    return n
rowsA=[]
for e in A:
    rowsA.append(dict(FECHA=e["t"].strftime("%d/%m/%Y"),HORA=e["t"].strftime("%H:%M:%S"),NUM_ORIGEN=e["a"],NUM_DESTINO=e["b"],TIPO=TIPO_A[e["tipo"]],DURACION="" if e["dur"] is None else e["dur"],CELDA=e["cell"],_err=e["err"]))
rowsB=[]
for e in B:
    u=e["t"]+timedelta(hours=6)  # archivo B en UTC; Juárez = UTC-6 en octubre 2026
    lac,ci=e["cell"].split("-")
    rowsB.append({"Fecha y hora (UTC)":u.strftime("%Y-%m-%d %H:%M:%S"),"Telefono A":b_num(e["a"]),"Telefono B":b_num(e["b"]),"Servicio":TIPO_B[e["tipo"]],"Segundos":"" if e["dur"] is None else e["dur"],"LAC-CI":f"{lac}/{ci}","_err":e["err"]})
# Fechas inválidas (4): se corrompe la fecha de renglones válidos
for r,bad in zip(random.sample([r for r in rowsA if not r["_err"]],2),["31/09/2026","00/10/2026"]): r["FECHA"]=bad; r["_err"]="fecha_invalida"
for r,bad in zip(random.sample([r for r in rowsB if not r["_err"]],2),["2026-13-02 10:00:00","2026-10-08 25:14:00"]): r["Fecha y hora (UTC)"]=bad; r["_err"]="fecha_invalida"
# Duplicados exactos (6)
for rows in (rowsA,rowsB):
    for r in random.sample([r for r in rows if not r["_err"]],3):
        i=rows.index(r); d=dict(r); d["_err"]="duplicado"; rows.insert(i+1,d)
HA=["FECHA","HORA","NUM_ORIGEN","NUM_DESTINO","TIPO","DURACION","CELDA"]
HB=["Fecha y hora (UTC)","Telefono A","Telefono B","Servicio","Segundos","LAC-CI"]
with open(f"{OUT}/operador_A_sintetico.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(HA); [w.writerow([r[h] for h in HA]) for r in rowsA]
for name,rows,H in (("operador_B_sintetico.csv",rowsB,HB),):
    with open(f"{OUT}/{name}","w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(H); [w.writerow([r[h] for h in H]) for r in rows]
wb=openpyxl.Workbook(); ws=wb.active; ws.title="CDR"; ws.append(HB)
for r in rowsB: ws.append([r[h] for h in HB])
wb.save(f"{OUT}/operador_B_sintetico.xlsx")
with open(f"{OUT}/catalogo_antenas_sintetico.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["id_celda","nombre","municipio","latitud","longitud","fuente","fecha_catalogo"])
    for c in CAT: w.writerow(list(c)+["Catálogo sintético v0.1","2026-10-01"])
# respuestas esperadas (clave del generador)
from collections import Counter
print("A",len(rowsA),"B",len(rowsB)); print(Counter(r["_err"] for r in rowsA+rowsB))
