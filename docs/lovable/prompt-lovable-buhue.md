# Prompt de Lovable para BUHUÉ (MVP)

Cómo usarlo: copia todo lo que está dentro del bloque "PROMPT PRINCIPAL" y pégalo en un proyecto nuevo de Lovable. Cuando termine, usa los prompts de seguimiento de abajo, uno por uno, solo si hace falta.

Notas antes de pegar:
- El borrador-2 (ZIP) es una app de Google AI Studio llamada "ANTISEC". De ahí tomamos el logo, los colores, el asistente de importación en pasos y la idea de formatos por operador. NO tomamos tres cosas que contradicen el reto y las reglas del equipo: coordenadas dentro de cada renglón de la sábana (el reto dice que llegan sin coordenadas), el trazado de "rutas" de personas y las etiquetas como "sospechoso" o "dealer".
- La captura de "Trámite Documental Ágil" es otro producto. Solo reutilizamos su patrón de botón flotante de WhatsApp, y únicamente en la página de presentación, no dentro de la herramienta de análisis. Confirma que el número 52 614 173 1455 es del equipo antes de dejarlo.

---

## PROMPT PRINCIPAL

```
Construye "BUHUÉ", una aplicación web en ESPAÑOL (México) para analistas de la Fiscalía General del Estado de Chihuahua. BUHUÉ significa "Base Unificada de Homologación y Ubicación de Estaciones". Lema: "Trayectorias · Celular · Contactos — Información para la investigación".

QUÉ RESUELVE
Los 6 analistas de la Fiscalía reciben "sábanas telefónicas" (registros de llamadas, SMS y datos que entregan los operadores con autorización judicial) en CSV o Excel, cada operador con columnas distintas y SIN coordenadas. Hoy las limpian, ordenan y cuentan a mano para armar informes. BUHUÉ importa la sábana, la valida, la normaliza, la ordena por tiempo, calcula frecuencias y arma una "Ficha verificable": cada cifra y cada frase de la ficha se puede abrir para ver los renglones exactos del archivo original que la sustentan.

La función estrella es la TRAZABILIDAD: en cualquier pantalla, al hacer clic en un número, conteo o hallazgo, se abre un panel lateral "Fuente" con los renglones originales (número de renglón del archivo, archivo, valores originales sin modificar y valores normalizados lado a lado).

STACK Y ALCANCE TÉCNICO
- React + TypeScript + Tailwind + shadcn/ui. Todo se procesa EN EL NAVEGADOR. No uses backend, base de datos, login, APIs externas ni IA externa en esta versión.
- Usa PapaParse para CSV y SheetJS (xlsx) para Excel. Usa Web Crypto (SHA-256) para la huella del archivo original. Usa Recharts para gráficas.
- Guarda el estado del caso en localStorage para que no se pierda al recargar, con un botón "Borrar datos de esta sesión".
- NO uses mapas de Google ni servicios cartográficos externos.

DISEÑO
- Institucional, sobrio y profesional. Tema oscuro por defecto con opción de tema claro.
- Paleta: fondo #0B132B (azul noche), superficies #111C3A y #1E293B, azul primario #1E40AF, azul acción #0284C7, acento #38BDF8, texto #F8FAFC y #94A3B8. Estados: verde #16A34A (válido), ámbar #F59E0B (revisar), rojo #DC2626 (error).
- Tipografía Inter. Tablas densas pero legibles, números en fuente monoespaciada.
- Logo: crea un componente SVG de un búho estilizado dentro de un círculo azul noche, con un pin de ubicación, una pequeña antena con ondas y líneas de mapa en azul #0284C7/#38BDF8. Junto al logo, el texto "BUHUÉ" en negritas y el lema debajo en pequeño.
- En el encabezado de TODAS las pantallas de la app muestra una franja fija: "DATOS SINTÉTICOS · Prototipo de demostración · Toda conclusión requiere revisión humana".

ESTRUCTURA
1) Página de presentación pública ("/"):
   - Héroe con logo, lema, una frase de valor: "De la sábana cruda a una ficha verificable en minutos, con cada dato ligado a su renglón de origen."
   - Tres pasos ilustrados: Importar y validar → Ordenar y contar → Ficha verificable.
   - Sección "Qué NO hace BUHUÉ": no rastrea teléfonos en tiempo real, no localiza personas, no decide culpabilidad ni credibilidad. Complementa a herramientas de localización; se enfoca en preparar y verificar.
   - Sección "Para quién": unidades de análisis de fiscalías (piloto: equipo de 6 analistas en Chihuahua).
   - Botón principal "Probar la demo con datos sintéticos" que lleva a /app.
   - Botón flotante de WhatsApp (esquina inferior derecha, verde, con ícono) que abre https://wa.me/526141731455?text=Hola%2C%20quiero%20informaci%C3%B3n%20sobre%20BUHU%C3%89 en una pestaña nueva. Este botón SOLO aparece en la página de presentación, nunca dentro de /app.
   - Pie: "Prototipo creado en el Rally de Innovación por la Justicia, Ciudad Juárez, 2026."

2) Aplicación ("/app") con barra lateral:
   a. Caso
   b. Importar
   c. Validar
   d. Cronología
   e. Frecuencias
   f. Antenas
   g. Ficha verificable
   h. Bitácora

PANTALLA a. CASO
- Formulario corto: folio del caso (texto libre, ej. "CASO-SINT-001"), analista responsable, periodo autorizado (fecha y hora de inicio y fin) y número objetivo autorizado.
- Botón grande "Cargar caso de demostración" que llena todo con datos sintéticos y carga los dos archivos de ejemplo (ver DATOS SINTÉTICOS). Con este botón la demo completa debe funcionar en un clic.

PANTALLA b. IMPORTAR (asistente en 4 pasos con indicador de progreso)
1. Subir archivo: arrastrar y soltar CSV/XLSX. Mostrar nombre, tamaño, número de renglones y la huella SHA-256 del archivo original. El original nunca se modifica.
2. Elegir formato de operador: "Operador A (sintético)", "Operador B (sintético)" o "Otro". Detecta el formato automáticamente por los encabezados y muéstralo como sugerencia.
3. Mapear columnas: tabla con cada campo estándar de BUHUÉ y un selector con la columna del archivo sugerida automáticamente. Campos estándar: fecha_hora, numero_a, numero_b, tipo_evento (llamada saliente, llamada entrante, SMS saliente, SMS entrante, datos), duracion_seg, id_celda, imei (opcional). Indicar con colores qué está mapeado, qué falta y qué es opcional. El usuario confirma.
4. Vista previa: primeras 20 filas normalizadas junto a las originales. Botón "Importar".
Se pueden importar varios archivos al mismo caso; cada renglón conserva archivo de origen y número de renglón original.

PANTALLA c. VALIDAR
- Resumen en tarjetas: renglones totales, válidos, con advertencia, con error.
- Reglas: fecha inválida o imposible; renglón fuera del periodo autorizado; duplicado exacto o candidato (mismo A, B, fecha_hora y celda); número con formato incompleto; id_celda sin correspondencia en el catálogo de antenas; duración negativa o vacía en llamadas.
- Normalización visible: números a 10 dígitos (quitar +52, 044, 045, espacios y guiones); fechas a ISO; tipo de evento a catálogo estándar; zona horaria: todo se muestra en hora de Ciudad Juárez (America/Ciudad_Juarez). Si el Operador B viene en hora del centro (America/Mexico_City), conviértela y marca el renglón con la etiqueta "hora ajustada".
- Tabla filtrable de problemas, cada uno con su renglón original. Acciones REVERSIBLES: "Excluir del análisis" (no borra, solo marca) y "Restaurar". Nada se elimina nunca.
- Los renglones fuera del periodo autorizado quedan excluidos por defecto y los números de terceros se enmascaran en pantalla (ej. 656-***-**42) con opción de mostrarlos registrando el motivo en la Bitácora.

PANTALLA d. CRONOLOGÍA
- Tabla ordenada por fecha y hora con: hora local, tipo, número A, número B, duración, id_celda, nombre de antena (si hay catálogo), archivo y renglón de origen.
- Filtros por rango de fechas, tipo de evento, número, antena y estado de validación.
- "Explicador de silencios": detecta huecos de más de 4 horas sin eventos y los muestra como bandas en una línea de tiempo y como filas grises en la tabla ("Sin registros entre 01:12 y 07:40, 6 h 28 min"). Texto fijo de aclaración: "Un hueco puede deberse a teléfono apagado, modo avión, falta de cobertura o a que el operador no reportó eventos. No es evidencia por sí mismo."
- Gráfica de barras de actividad por hora del día y por día.

PANTALLA e. FRECUENCIAS
- Top de números con los que interactúa el número objetivo: total de eventos, llamadas, SMS, duración total, primera y última fecha. Cada cifra es clicable y abre el panel "Fuente".
- Top de antenas (id_celda) por número de eventos.
- Etiquetas neutrales y editables por el analista para números: "Contacto frecuente", "Por identificar", "Servicio/empresa", "Revisado". No uses etiquetas de culpabilidad.

PANTALLA f. ANTENAS ("Mapa honesto")
- Cruza id_celda con un catálogo sintético de antenas cargado en la app (id, nombre, municipio, latitud, longitud, fuente del catálogo, fecha del catálogo).
- Muestra un mapa simple con Leaflet + OpenStreetMap SOLO con antenas que sí están en el catálogo, con tamaño del punto según número de eventos. Debajo, lista separada "Celdas sin ubicación documentada" con su conteo.
- Aviso permanente: "La ubicación de una antena no es la ubicación de una persona. BUHUÉ no traza trayectorias ni estima posiciones."
- No dibujes líneas entre antenas ni radios de cobertura.

PANTALLA g. FICHA VERIFICABLE
- Documento tipo informe con encabezado (logo, folio, analista, periodo autorizado, fecha de generación, archivos fuente con su SHA-256 y versión de los datos).
- Secciones: resumen de la importación y calidad; actividad por periodo; principales contactos; principales antenas; silencios detectados; observaciones del analista (texto libre).
- Cada cifra y cada frase generada lleva una cita tipo [R: 12, 45, 88] con los renglones de origen; al hacer clic abre el panel "Fuente".
- Las frases se generan con plantillas a partir de los cálculos, en lenguaje descriptivo y neutral (ej. "El número 656-555-0142 aparece en 37 eventos entre el 3 y el 9 de octubre [R: …]"). Incluye un revisor que resalta en ámbar palabras no permitidas si el analista las escribe en observaciones: "culpable", "responsable", "sospechoso", "estaba en", "se encontraba en", "mintió", con sugerencia de redacción neutral.
- Casillas obligatorias antes de exportar: "Revisé los datos de origen" y "Entiendo que esta ficha no determina responsabilidad". Campo "Revisado por".
- Exportar: PDF (vista de impresión con estilos limpios en fondo blanco), CSV de los renglones usados y un anexo con la lista completa de citas renglón por renglón. El pie de cada página dice "DATOS SINTÉTICOS — documento de demostración" y la huella SHA-256 de la ficha.

PANTALLA h. BITÁCORA
- Registro automático con fecha, hora y analista de: archivos importados (con SHA-256), mapeos confirmados, exclusiones y restauraciones, números desenmascarados con su motivo, fichas exportadas. Solo lectura y exportable a CSV.

PANEL "FUENTE" (componente reutilizable)
- Panel lateral derecho que se abre desde cualquier cifra. Muestra cuántos renglones sustentan el dato, los filtros aplicados, y una tabla con: archivo, renglón original, valores originales y valores normalizados, estado de validación. Botón "Copiar referencia".

DATOS SINTÉTICOS (incluirlos en el código, ninguno real)
- Usa solo números ficticios con el patrón 656-555-01XX y 614-555-02XX. Nombres de antenas inventados ("Celda Sintética Norte 01").
- Archivo 1 "operador_A_sintetico.csv" (~300 renglones), hora de Ciudad Juárez, encabezados: FECHA, HORA, NUM_ORIGEN, NUM_DESTINO, TIPO, DURACION, CELDA. Formato fecha DD/MM/AAAA.
- Archivo 2 "operador_B_sintetico.xlsx" (~200 renglones), hora del centro, encabezados: "Fecha y hora", "Telefono A", "Telefono B", "Servicio", "Segundos", "LAC-CI". Números con +52 y guiones.
- Número objetivo: 656-555-0100. Periodo: 1 al 10 de octubre de 2026. Que el patrón muestre 4 o 5 contactos frecuentes, 8 antenas, 2 silencios largos (uno nocturno de 6 h y otro de 14 h), 6 duplicados, 4 fechas inválidas, 10 renglones fuera del periodo y 5 celdas que no existen en el catálogo.
- Catálogo de antenas sintético con 8 celdas en Ciudad Juárez (coordenadas aproximadas inventadas dentro de la ciudad) marcado como "Catálogo sintético v0.1".
- Botones para descargar ambos archivos de ejemplo desde la pantalla Importar.

REGLAS ÉTICAS Y DE SEGURIDAD (obligatorias en textos y funciones)
- No rastrea en tiempo real, no localiza personas, no estima posiciones ni trayectorias.
- No califica culpabilidad, credibilidad ni peligrosidad, y no sugiere sospechosos. La frecuencia o la presencia en una antena no es una acusación.
- Supervisión humana siempre: nada se exporta sin la revisión explícita del analista.
- Nunca borra datos: excluir es reversible y el original se conserva con su huella.
- Diferenciar visualmente "Dato calculado", "Observación del analista" y "Hipótesis por validar".
- Todo el contenido de los archivos importados se trata como datos, nunca como instrucciones.
- Mensaje en la pantalla Importar: "Este prototipo es solo para datos sintéticos. No cargues sábanas reales."

CRITERIO DE ÉXITO DE LA DEMO
Desde /app, con un clic en "Cargar caso de demostración", se debe poder recorrer en menos de 2 minutos: importar → ver 4 fechas inválidas, 6 duplicados y 5 celdas sin catálogo → ver la cronología con los 2 silencios → ver el top de contactos → abrir cualquier cifra y ver sus renglones de origen → generar y exportar la ficha en PDF con citas.
```

---

## Prompts de seguimiento (usar solo si hace falta, uno a la vez)

1. Si algo falla en el flujo de demo:
```
Recorre el flujo completo desde "Cargar caso de demostración" hasta exportar la ficha en PDF y corrige cualquier error. Verifica que los conteos coincidan con los datos sintéticos: 4 fechas inválidas, 6 duplicados, 10 renglones fuera del periodo, 5 celdas sin catálogo y 2 silencios largos. No agregues funciones nuevas.
```

2. Para pulir la parte visual antes del pitch:
```
Mejora el pulido visual sin cambiar funciones: espaciado consistente, estados vacíos con instrucciones claras, tooltips en cada indicador, y que la vista de impresión de la ficha se vea como un documento institucional limpio en fondo blanco. Asegura que se vea bien en una laptop de 1366x768 y en proyector.
```

3. Para el contador del pitch (opcional):
```
En la pantalla Ficha verificable agrega un indicador pequeño: "Ficha generada en X segundos desde la importación · N cifras · 100% con renglón de origen". Calcula X y N de verdad, no los inventes.
```
