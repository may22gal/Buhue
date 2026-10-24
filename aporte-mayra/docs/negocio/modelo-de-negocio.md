# Modelo de negocio: plataforma mexicana para sábanas y antenas

Oct 24, 2026

## A. Recomendación ejecutiva

Recomendamos vender una plataforma mexicana y configurable que convierte sábanas telefónicas en fichas verificables. Se entra con un piloto pagado de 12 semanas en una unidad de análisis de la Fiscalía de Chihuahua y después se pasa a una licencia anual por unidad. El primer año no es rentable: necesita entre 1.4 y 2.2 millones de pesos de financiamiento, y el negocio se sostiene a partir de unas 5 unidades contratadas, a las que el escenario base llega hacia el mes 20 con unos 2.5 millones de financiamiento total.

| Pregunta | Respuesta |
| --- | --- |
| Qué vendemos | Una plataforma que importa sábanas de los operadores, valida y normaliza, ordena por cronología, calcula frecuencias de números y antenas, ubica antenas cuando hay catálogo autorizado y arma la ficha institucional. Cada cifra queda ligada a su renglón original. Se personaliza por configuración (formato de operador, plantilla de ficha, catálogos, roles), sin reprogramar. |
| A quién | Usuario: analistas que procesan sábanas. Comprador: Fiscalía General del Estado de Chihuahua, por su área administrativa, con visto bueno de tecnología y de protección de datos. Primer segmento: una sola unidad de análisis en una zona, por confirmar con el mentor. |
| Por qué compraría | Según lo que explicó el equipo de Fiscalía, la preparación es manual y se repite con cada archivo nuevo. La plataforma reduce esa talacha, muestra errores y faltantes, y produce fichas defendibles porque cada dato se rastrea a su origen. Geomatrix localiza teléfonos; no encontramos evidencia pública de que prepare sábanas ni fichas. |
| Cómo cobramos | Piloto pagado de 12 semanas: $380,000. Implementación de producción: $280,000. Licencia anual por unidad: $960,000, con hasta 10 usuarios, entorno dedicado en México y soporte con niveles definidos. Extras con precio de lista. Cifras ilustrativas, sin IVA. Nunca se cobra por persona, por consulta ni por resultado. |
| Cómo financiamos el inicio | Las personas fundadoras aportan trabajo hasta firmar el piloto, registrado como aportación de socios y no como ingreso. El piloto pagado financia la versión institucional. La brecha restante se cubre con incubación, aliado tecnológico o capital semilla. El premio del evento no sostiene la operación. |
| Qué lo haría rentable | Con un equipo de 4 personas, cuyo costo completo ronda $3.6 millones al año, el equilibrio operativo llega con unas 5 unidades a $960,000. Una sola fiscalía quizá no alcanza, así que el mismo núcleo debe venderse en 2 o 3 estados. Eso funciona si los formatos de los operadores son iguales en todo el país, dato por validar. |
| Mayor riesgo | Que la Fiscalía no tenga presupuesto ni ruta de compra para un proveedor nuevo en 2027, año de elección de gubernatura en Chihuahua. Segundo riesgo: que no exista un catálogo autorizado de antenas y el mapa quede como función secundaria. |

**Propuesta de cambio sobre "ser un Geomatrix local".** Según [R3D](https://r3d.mx/2021/08/09/gobierno-de-puebla-adquirio-geomatrix-en-2019-y-2020/), [El País vía Xataka](https://www.xataka.com.mx/seguridad/fgr-compro-software-para-espionaje-telefonos-mexico-pais-geolocalizacion-analisis-datos-masivo-2019-2020) y [Animal Político vía R3D](https://r3d.mx/2024/07/29/la-fgr-uso-tecnologia-de-geolocalizacion-para-vigilar-personas-y-solo-justifico-el-0-24-de-los-casos/), Geomatrix es un sistema de localización de celulares en tiempo real que la FGR y Puebla compraron por millones de pesos, y que se usó casi siempre sin orden judicial. Recomendamos no copiar el rastreo. Conviene ser la plataforma mexicana de análisis trazable de registros obtenidos legalmente, que complementa a Geomatrix y que un juez puede revisar. Es más fácil de vender, de defender ante el jurado y de autorizar dentro de la Fiscalía.

## B. Propuesta de valor

**Del archivo del operador a una ficha institucional verificable, sin rehacer la preparación con cada archivo nuevo y con cada dato ligado a su registro de origen.**

La plataforma hace lo repetitivo con reglas reproducibles: reconocer columnas, normalizar, ordenar, contar y cruzar con el catálogo de antenas. La persona revisa excepciones, confirma y firma. El valor no es "tener IA", sino que el superior, el Ministerio Público o un juez puedan abrir cualquier cifra de la ficha y ver los renglones que la sostienen.

| Paso | Hoy, según lo que explicó Fiscalía | Con la plataforma |
| --- | --- | --- |
| Recepción | Se abre el archivo y se acomodan columnas a mano | Se elige la configuración guardada del operador y solo se confirman las columnas dudosas |
| Limpieza | Se borran filas sin registro de qué se quitó | Se excluyen filas con motivo; el original queda intacto |
| Cronología y frecuencias | Tablas manuales que se rehacen al llegar otro archivo | Conteos reproducibles que se recalculan con los mismos filtros |
| Antenas | Búsqueda manual, si hay catálogo | Cruce con el catálogo autorizado; sin catálogo se marca "sin ubicación" |
| Ficha | Copiar y pegar en la plantilla y revisar cifras a mano | Ficha prellenada con fuente, periodo, filtros y limitaciones; el analista revisa y firma |
| Revisión | Difícil comprobar de dónde sale cada número | Cada cifra abre sus renglones y la huella digital del archivo |

No prometemos un porcentaje de ahorro. El piloto lo mide con esta fórmula:

```latex
\text{Capacidad liberada (h/mes)} = \text{sábanas por mes} \times (\text{horas actuales por sábana} - \text{horas con la plataforma})
```

Datos que faltan y hay que pedir al mentor: sábanas por mes, horas promedio desde la carga hasta la ficha revisada, número de analistas y fichas que se regresan para corrección. Las horas liberadas son capacidad para más casos o entregas más rápidas; no equivalen a recortar plazas.

Límites que la ficha declara siempre: la ubicación de una antena no es la ubicación exacta de una persona, más registros en una antena no prueban más tiempo de permanencia, y una coincidencia no prueba relación ni culpabilidad.

## C. Business Model Canvas

El usuario, el comprador y el beneficiario son personas distintas, y el lienzo los separa.

| Bloque | Contenido |
| --- | --- |
| 1. Segmentos de clientes | Inicial: unidades de análisis de la Fiscalía de Chihuahua que procesan sábanas, empezando por una zona. Después: otras fiscalías estatales que reciben archivos de los mismos operadores. Adyacente, solo con acceso legítimo y el mismo núcleo: defensorías públicas que revisan sábanas entregadas como evidencia, y áreas periciales. |
| 2. Propuesta de valor | Ficha institucional verificable desde el archivo del operador. Menos preparación repetitiva, errores y faltantes visibles, configuraciones reutilizables, despliegue en nube mexicana o en servidores del cliente, y soporte en México y en pesos. |
| 3. Canales | Demo con datos sintéticos ante la unidad usuaria, vinculación del evento con Gobierno del Estado, piloto pagado, referencias entre fiscalías, e integrador local con registro de proveedor cuando la Fiscalía lo prefiera. |
| 4. Relación con clientes | Implementación acompañada, capacitación con material repetible, soporte con horario y niveles definidos, y revisión trimestral de mejoras con los usuarios. |
| 5. Fuentes de ingresos | Piloto pagado, implementación, licencia anual por unidad (recurrente) y extras con precio de lista: adaptadores, plantillas, usuarios, capacitación y horas especiales. |
| 6. Recursos clave | Núcleo de software, biblioteca de adaptadores por operador, plantillas de ficha validadas, conocimiento del flujo del analista, controles de seguridad documentados y referencias de clientes. |
| 7. Actividades clave | Mantener adaptadores al día, desarrollar el núcleo, operar seguridad y respaldos, implementar y capacitar, dar soporte y vender a instituciones. |
| 8. Socios clave | Nube con región en México o infraestructura del cliente, asesoría jurídica en datos personales y contratación pública, auditor externo de seguridad, proveedor de IA con contrato que prohíba entrenar con datos del cliente, y universidades locales para talento. |
| 9. Estructura de costos | Personal clasificado por función (entrega, producto, ventas, administración), nube por unidad, IA con tope, mapas, pruebas de seguridad, seguros, contador, abogado, viajes y una contingencia de 10 %. |

**Actores dentro de la institución (por confirmar con el mentor).** Usuario operativo: analista que procesa sábanas. Responsable del área: jefatura de la unidad de análisis. Patrocinador interno: titular de la fiscalía de zona o de la especializada. Tecnología: dirección de informática. Seguridad y datos personales: responsable de protección de datos y órgano interno de control. Comprador: dirección administrativa y comité de adquisiciones. Fuente presupuestal posible: presupuesto estatal o FASP, que para 2026 incluye equipamiento de unidades de investigación e inteligencia de procuración de justicia ([acuerdo 03/LII/2025](https://sidof.segob.gob.mx/notas/docFuente/5777197)). Beneficiario final: víctimas y ciudadanía, con investigaciones mejor sustentadas.

## D. Modelo comercial

Recomendamos un piloto pagado que, si cumple criterios, pasa a implementación más licencia anual por unidad (opciones B y luego A). La alternativa es la instalación local (D) cuando tecnología o protección de datos lo exijan. El contrato estatal por bandas (E) se ofrece desde la tercera unidad.

| Opción | Compra institucional | Recupera implementación | Margen y flujo | Riesgo principal |
| --- | --- | --- | --- | --- |
| A. Implementación + licencia anual + soporte definido | Fácil de presupuestar en dos partidas | Sí, se cobra al inicio | Bueno, con pago anual | Soporte sin límite que se come el margen |
| B. Piloto pagado y luego operación | Monto menor y decisión con evidencia | Parcial | Bajo en el piloto, alto después | Que el piloto se vuelva implementación regalada |
| C. Suscripción mensual por equipo | Difícil: el gobierno compra por ejercicio anual | No | Flujo parejo, pero con más trámites de pago | Retrasos de cobro cada mes |
| D. Instalación en infraestructura del cliente | Necesaria si se exige que los datos no salgan | Sí, con implementación mayor | Menos nube, más viajes y soporte | Versiones dispersas y actualizaciones lentas |
| E. Contrato estatal por bandas de unidades | Un solo contrato para toda la Fiscalía | Sí | El mejor a escala | Solo viable después de probar en una unidad |

### Qué incluye la licencia y qué se cobra aparte

Precios ilustrativos en pesos, sin IVA, por validar con el mercado.

| Concepto | Incluido en la licencia anual ($960,000) | Se cobra aparte |
| --- | --- | --- |
| Producto estándar | Importar, validar, normalizar, excluir con motivo, cronología, frecuencias, cruce con catálogo, ficha, bitácora y exportación | — |
| Configuración | Formato y plantilla hechos en el piloto o la implementación | Adaptador de operador nuevo $90,000; de la biblioteca $25,000; plantilla adicional $45,000 |
| Usuarios | Hasta 10 nombrados | Bloque de 5 usuarios: $120,000 al año |
| Capacitación | 12 horas en la implementación y material de consulta | Taller adicional de 4 horas: $16,000 |
| Soporte | Lunes a viernes de 9 a 18 h, hasta 20 horas al mes por unidad, respuesta en 4 horas hábiles a incidentes críticos | Hora adicional: $1,400; guardias fuera de horario por cotización |
| Integraciones | Exportación a CSV, Excel, PDF y Word | Inicio de sesión institucional u otros sistemas: por alcance, más 18 % anual de mantenimiento |
| Infraestructura | Nube dedicada en México con 500 GB y respaldos | Almacenamiento extra por bloque; en instalación local la pone el cliente |
| Fuera de alcance | — | Rastreo en vivo, conexión con Geomatrix u operadores sin documentación ni autorización, dictámenes periciales |

**Regla contra la consultoría a la medida.** Si una adaptación sirve a todos los clientes, entra al producto y solo se cobra su configuración. Si sirve a uno solo, se cotiza aparte. El código genérico queda con nosotros; los datos y configuraciones son del cliente. Esta cláusula requiere validación jurídica.

### Comparación con el modelo de Geomatrix

| Elemento | Geomatrix, según reportes públicos | Nuestra propuesta |
| --- | --- | --- |
| Qué hace | Localiza celulares en tiempo real por número o IMSI y permite geocercas ([R3D](https://r3d.mx/2021/08/09/gobierno-de-puebla-adquirio-geomatrix-en-2019-y-2020/)) | Analiza registros entregados por los operadores y produce fichas trazables |
| Cómo se vendió | Puebla 2019: $18.8 millones por licencia de 12 meses más dos equipos IMSI catcher. Puebla 2020: $1 millón por renovación con 960 consultas ([R3D](https://r3d.mx/2021/08/09/gobierno-de-puebla-adquirio-geomatrix-en-2019-y-2020/)). FGR: cerca de $142.9 millones en tres contratos de 2018 y 2019 ([Animal Político](https://grupoanimal.mx/seguridad/fiscalia-gertz-rastrear-celulares-uso-injustificado)); El País reportó US$5.6 millones en al menos cuatro contratos de 2019 y 2020 ([Xataka](https://www.xataka.com.mx/seguridad/fgr-compro-software-para-espionaje-telefonos-mexico-pais-geolocalizacion-analisis-datos-masivo-2019-2020)) | Lista de precios: piloto, implementación y licencia anual por unidad |
| Unidad de cobro | Licencia por periodo y paquetes de consultas; la renovación de Puebla equivale a unos $1,042 por consulta (cálculo propio) | Unidad de análisis con usuarios y almacenamiento; nunca por consulta ni por persona |
| Canal | Intermediario Neolinx de México | Venta directa o integrador local |
| Control legal | El País: 124 órdenes judiciales en 13,890 búsquedas de 2019; Animal Político: 0.24 % justificado en 135 mil usos | Periodo autorizado y número de oficio obligatorios antes de analizar, con bitácora de accesos |
| Salida del proveedor | Cotización y términos no públicos | Exportación completa de datos y configuraciones al terminar |

Las cifras de Geomatrix vienen de contratos obtenidos por transparencia y publicados por periodistas y organizaciones; no revisamos los contratos originales. La cotización actual de Geomatrix no es pública.

**Actualización con la investigación del equipo.** El [folleto comercial de GeoMatrix](https://www.pointtrading.com/wp-content/uploads/2020/07/GeoMatrix-Brochure-email.pdf) lo describe como un sistema de geolocalización basado en el protocolo SS7, con contacto de Rayzone en Tel Aviv. Ofrece dos modalidades: servicio con cobro por consulta usada o por paquete de consultas, e instalación en el cliente con operación sin conexión. También anuncia administración de usuarios, permisos y estadísticas de uso. Es material de venta, no una verificación independiente.

El equipo también reportó dos antecedentes que no pudimos abrir y deben verificarse antes de citarlos en el pitch:

- Un informe FASP de Chihuahua que registra "Consultas de geolocalización (Geomatrix)" con el expediente SH/ADE/181/2024. Si se confirma, prueba que el estado ya compra este tipo de tecnología con recursos de seguridad, pero no que haya presupuesto para nosotros.
- Un contrato de Morelos de 2017 por 1,217 consultas a $895,069.76 sin IVA, unos $735 por consulta. Es un paquete histórico, no el precio actual.

Nuestro modelo no cambia: seguimos sin cobrar por consulta, porque queremos que el analista revise y compruebe sin pagar cada vez.

## E. Modelo financiero

Con supuestos ilustrativos, el primer año tiene pérdida operativa de $0.9 a $2.2 millones y necesita de $1.4 a $2.2 millones de caja. El equilibrio llega con unas 5 unidades activas a $960,000 al año, y el escenario base lo alcanza hacia el mes 20 con una necesidad máxima de caja de $2.2 millones. Todo en pesos y sin IVA; el IVA cobrado se entrega al SAT y no es ingreso. Horizonte: noviembre de 2026 a octubre de 2027.

### Supuestos

Tipo: **S** = supuesto ilustrativo por validar, **R** = referencia con fuente, **C** = cálculo.

| Concepto | Valor | Tipo |
| --- | --- | --- |
| Cargas patronales y prestaciones sobre sueldo bruto (IMSS, Infonavit, SAR, impuesto sobre nómina, aguinaldo, vacaciones) | ×1.35 | S, validar con contador |
| Horas productivas por persona | 140 al mes | S |
| Costo completo por hora productiva (personal más gastos generales) | $535 | C |
| Costo variable por unidad: nube dedicada $12,000, IA con tope $2,500, mapa base $1,500 (Google Maps, sección I), monitoreo $1,500 | $17,500 al mes | S, cotizar |
| Gastos generales: contador, abogado, prueba de penetración prorrateada, seguro, oficina, viajes, herramientas, entornos de prueba, más 10 % de contingencia | $59,400 al mes | S |
| Precios: piloto, implementación, licencia anual por unidad | $380,000 / $280,000 / $960,000 | S |
| Retraso de cobro | 60 días base, 120 conservador | S |
| ISR de personas morales y PTU | 30 % y 10 %; PTU exenta el primer año de operaciones | Validar con contador |

### Sueldos clasificados por función

El tiempo de implementar, capacitar y dar soporte es costo directo. Construir el núcleo es desarrollo de producto, vender es gasto de ventas y administrar es gasto administrativo. Este reparto sirve para fijar precios; el tratamiento contable formal puede diferir. Las personas fundadoras trabajan sin sueldo hasta firmar el piloto, y ese trabajo se registra como aportación de socios, no como ahorro ni utilidad.

| Puesto | Sueldo bruto mensual | Costo completo mensual | Entrega | Producto | Ventas | Admin. |
| --- | --- | --- | --- | --- | --- | --- |
| Dirección comercial y operaciones (persona fundadora) | $45,000 | $60,750 | 20 % | — | 60 % | 20 % |
| Liderazgo técnico y seguridad (persona fundadora) | $65,000 | $87,750 | 25 % | 75 % | — | — |
| Desarrollo full-stack | $40,000 | $54,000 | 30 % | 70 % | — | — |
| Implementación y soporte | $28,000 | $37,800 | 90 % | 10 % | — | — |
| Total | $178,000 | $240,300 |  |  |  |  |

### Escenarios a 12 meses

Mes 1 es noviembre de 2026. Cifras en miles de pesos.

| Concepto | Conservador | Base | Favorable |
| --- | --- | --- | --- |
| Calendario | Piloto en marzo; 1 unidad desde agosto | Piloto en enero; unidades en mayo y agosto | Pilotos en diciembre y marzo; unidades en marzo, junio y agosto |
| Pilotos / implementaciones / unidades al cierre | 1 / 1 / 1 | 1 / 2 / 2 | 2 / 3 / 3 |
| Ingresos operativos | 900 | 1,660 | 2,880 |
| — recurrentes (licencias) | 240 | 720 | 1,280 |
| — no recurrentes (pilotos e implementaciones) | 660 | 940 | 1,600 |
| Costos directos | 746 | 1,019 | 1,244 |
| Utilidad bruta | 154 | 641 | 1,636 |
| Margen bruto | 17 % | 39 % | 57 % |
| Gastos operativos (producto, ventas, administración) | 2,399 | 2,490 | 2,532 |
| Resultado operativo, con el costo de las personas fundadoras | −2,245 | −1,849 | −896 |
| Trabajo fundador no pagado (aportación de socios) | 594 | 297 | 149 |
| Cobrado en el año | 380 | 1,340 | 2,400 |
| Por cobrar al cierre (capital de trabajo) | 520 | 320 | 480 |
| Necesidad máxima de efectivo | 2,171 | 1,872 | 1,416 |

No hay ISR ni PTU porque hay pérdida, y no se presenta utilidad neta. No hay intereses porque el modelo no usa deuda. Extendido a 24 meses, el escenario base con una unidad nueva cada tres meses toca su punto más bajo de caja en $2.2 millones en el mes 19. El conservador sigue perdiendo y llega a $4.1 millones, por eso necesita una regla de salida (sección F).

### Punto de equilibrio y precio

```latex
\text{Unidades de equilibrio} = \frac{\text{Costos fijos anuales}}{\text{Precio anual por unidad} - \text{Costo variable anual por unidad}} = \frac{3{,}596{,}400}{960{,}000 - 210{,}000} = 4.8
```

| Precio anual por unidad | Unidades para equilibrio |
| --- | --- |
| $720,000 | 7.1 |
| $840,000 | 5.7 |
| $960,000 | 4.8 |
| $1,200,000 | 3.6 |

**Precio mínimo sostenible: unos $810,000 al año por unidad.** Sale de repartir los costos fijos entre las 6 unidades que el equipo de 4 puede atender y sumar el costo variable. Si solo se llenan 5 unidades, el mínimo sube a $930,000.

**Precio objetivo ilustrativo: $960,000 al año por unidad.** Cubre costos con 5 unidades y queda en el rango alto de herramientas comparables en EE. UU., que en documentos públicos de cabildos van de unos US$18,000 a US$61,000 al año (sección H). Se justifica por el entorno dedicado en México, los formatos mexicanos y el soporte local, y debe validarse contra el valor medido en el piloto. Margen no es recargo: con costo variable de $210,000, el margen de contribución es 78 % del precio, aunque el recargo sobre ese costo sea 357 %.

### Año estable ilustrativo

Con 6 unidades, 2 implementaciones al año y un segundo analista de soporte (equipo de 5):

| Concepto | Miles de pesos |
| --- | --- |
| Ingresos operativos | 6,320 |
| Costos directos (nube por unidad y personal de entrega) | 2,680 |
| Utilidad bruta (58 %) | 3,640 |
| Gastos operativos | 2,701 |
| Utilidad operativa (15 %) | 939 |
| PTU 10 % | 94 |
| ISR 30 % | 253 |
| Utilidad neta aproximada (9 %) | 591 |

La base gravable se aproxima con la utilidad operativa; el cálculo fiscal real lo hace el contador.

### Sensibilidad sobre el escenario base

| Cambio | Resultado operativo 12 meses | Necesidad máxima de caja | Lectura |
| --- | --- | --- | --- |
| Base | −1,849 | 1,872 | — |
| Cobro a 90 días | −1,849 | 2,058 | La pérdida no cambia; falta caja |
| Cobro a 120 días | −1,849 | 2,392 | Hacen falta $520,000 más |
| Primer contrato 3 meses después | −1,949 | 1,646 | La caja parece menor solo porque las personas fundadoras trabajan más meses sin sueldo ($742,000) y el gasto se pasa al año 2 |
| Personalización tarda el doble (240 h extra por implementación) | −2,106 | 2,129 | Cobrar adaptaciones aparte |
| Doble soporte por cliente | −2,076 | 2,099 | El equilibrio sube a 5.4 unidades |
| Consumo de IA ×3 | −1,909 | 1,932 | El equilibrio sube a 5.2 unidades; poner topes |
| Instalación local exigida (licencia $840,000, implementación $400,000) | −1,561 | 1,544 | Conviene si la implementación mayor se cobra |

**Capacidad.** El equipo de 4 tiene unas 231 horas directas al mes. Con 20 horas de soporte por unidad, atiende unas 6 unidades y una implementación cada dos meses. Más allá hay que contratar antes de vender, no después.

Métricas como LTV, CAC o cancelación no se calculan porque no hay historial de clientes.

## F. Estrategia de financiamiento

En el escenario base hacen falta unos $2.5 millones fuera de ventas para llegar al equilibrio: el punto más bajo de caja ($2.2 millones) más un colchón de 15 %. A eso se suma el trabajo no pagado de las personas fundadoras. Recomendamos levantarlo en dos tramos ligados a hitos y usar ingresos de clientes como primera fuente.

| Etapa | Qué se financia | Monto aproximado | Resultado exigido | Fuente | Qué recibe la fuente | Condición para avanzar |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Prototipo del evento (hoy) | Tiempo del equipo y herramientas gratuitas | Menos de $1,000 de gasto nuevo | Demo con datos sintéticos, landing y pitch | Personas fundadoras | — | Interés explícito de la unidad usuaria |
| 2. Validación y preparación del piloto (nov. 2026 a ene. 2027) | Entrevistas con analistas, propuesta técnica y de seguridad, constitución de la empresa, contador | $180,000 en efectivo y unos $445,000 de trabajo fundador | Solicitud formal de piloto con alcance y criterios | Personas fundadoras e incubación; el premio queda fuera del escenario base | Participación en la empresa | La unidad, TI y protección de datos aceptan el alcance |
| 3. Piloto institucional (12 semanas) | Adaptador real, seguridad, entorno dedicado, capacitación | Unos $840,000 de costo; el piloto paga $380,000 | Criterios de aceptación cumplidos | Pago del piloto; anticipo si la normativa lo permite; tramo 1 de capital ($1 millón) | Servicio para la Fiscalía; participación para el inversionista | Criterios cumplidos y partida para la licencia |
| 4. Operación y crecimiento (hasta 6 unidades) | Equipo completo, segunda fiscalía, soporte | Tramo 2 de capital ($1.5 millones) | 5 a 6 unidades con licencia | Licencias; capital semilla; financiamiento contra contratos firmados | Participación o intereses | Unidades firmadas y cobranza al día |

| Fuente | Tipo | Cuándo usarla | Cuidado |
| --- | --- | --- | --- |
| Personas fundadoras | Capital propio | Etapas 1 y 2 | Se registra como aportación, no como venta |
| Premio del evento | No dilutivo | Gastos de validación | Son $6,000 al primer lugar y no entran al escenario base. No sostiene la operación ni es ingreso del producto |
| Piloto pagado | Ingreso de cliente | Etapa 3 | Alcance, precio y criterios por escrito |
| Anticipo contractual | Ingreso anticipado | Etapas 3 y 4 | Solo si la normativa y el contrato lo permiten; suele pedir garantía. Validar |
| Aliado tecnológico o integrador | Comercial | Si la Fiscalía prefiere un proveedor registrado | Comparte margen; no ceder el producto |
| Incubación o convocatoria pública | No dilutivo | Etapas 2 y 3 | No la consideramos abierta hasta verificar fechas y elegibilidad |
| Capital semilla privado | Dilutivo | Desde el piloto firmado | Inversionistas que acepten clientes de gobierno y ciclos largos |
| Financiamiento contra contratos (por ejemplo, descuento de facturas) | Deuda | Etapa 4, para cobros a 90 o 120 días | Nunca para cubrir pérdidas sin demanda validada |

El FASP no es financiamiento nuestro: es una posible fuente de presupuesto del cliente.

**Quién absorbe el riesgo del piloto.** La Fiscalía paga el costo directo del piloto y nosotros absorbemos el desarrollo del producto. Si no se cumplen los criterios, la Fiscalía conserva el informe y sus datos exportados, sin obligación de compra. Así no se regala una implementación: el piloto tiene precio, alcance y fecha de cierre.

**Regla de salida.** Si al mes 9 no hay licencia firmada ni partida identificada, se detienen las contrataciones y se decide entre otro estado, otro segmento o un cierre ordenado. El modelo no depende de premios ni subsidios para operar.

## G. Piloto pagado y ruta de adopción

Proponemos un piloto de 12 semanas por $380,000 más IVA en una unidad, con un formato de operador, una plantilla de ficha y criterios que la Fiscalía fija antes de empezar.

| Elemento | Propuesta |
| --- | --- |
| Área | Una unidad de análisis de una zona, por confirmar |
| Entrada y salida | Un formato de sábana de un operador y una plantilla de ficha institucional |
| Datos | Semanas 1 a 4 solo sintéticos. Después, datos institucionales solo con autorización escrita, convenio de confidencialidad y entorno aprobado por TI |
| Responsables | Jefatura de la unidad y un enlace de TI |
| Calendario | 2 semanas de configuración, 2 de capacitación y pruebas, 6 de operación acompañada y 2 de evaluación |
| Usuarios, capacitación y soporte | Hasta 8 usuarios, 12 horas de capacitación, soporte en horario hábil hasta 20 horas al mes |
| Entregables | Entorno configurado, adaptador, plantilla, manual, bitácora, informe de evaluación y exportación de datos |
| Límites | Sin integraciones; lo que salga del alcance se cotiza aparte |
| Cierre | Informe, exportación completa y borrado verificable si no continúa |
| Paso a operación | Criterios cumplidos, revisión de seguridad aprobada y partida presupuestal |

**Criterios de aceptación propuestos**, sin porcentajes prometidos:

- Importa todos los archivos de prueba del formato acordado, o reporta con motivo cada renglón no importado.
- Cada cifra de la ficha abre los renglones que la sostienen, comprobado por un revisor en una muestra acordada.
- Los conteos coinciden con un cálculo independiente en esa muestra.
- El archivo original no cambia: su huella digital es igual antes y después.
- La bitácora registra cada acceso y cada exclusión.
- El tiempo desde la carga hasta la ficha revisada se mide antes y durante el piloto; la meta de mejora la fija la Fiscalía.

**Qué se mide:** tiempo de carga a ficha revisada, errores detectados, fichas devueltas por corrección, cifras con soporte verificable, facilidad de uso con un cuestionario estándar, horas de capacitación y solicitudes de soporte.

**Ruta comercial**

1. Presentación: demo con datos sintéticos a la unidad usuaria y su jefatura.
2. Validación del problema: línea base con 2 o 3 analistas, en horas y pasos.
3. Revisión técnica y de seguridad: TI y protección de datos revisan arquitectura, despliegue y controles.
4. Piloto autorizado: pedido o contrato con alcance, precio y criterios, por la vía de compra que defina el área administrativa.
5. Evaluación conjunta contra los criterios.
6. Contratación de la licencia o cierre ordenado.

La vía de compra depende de la ley de adquisiciones del Estado de Chihuahua y, si se usan recursos federales como el FASP, de la normativa federal. No proponemos fraccionar compras ni evitar procedimientos. Esto requiere validación jurídica.

**Salida ordenada.** Al terminar, el cliente recibe sus datos en CSV o Excel, sus configuraciones en formato abierto y la bitácora, sin costo por exportaciones estándar. La permanencia debe venir del valor, no de retener la información.

## H. Diferenciación y competencia

Hay competencia madura en análisis de registros telefónicos, casi toda extranjera, con precios en dólares o no públicos. La diferencia que podemos construir es local: formatos mexicanos, fichas institucionales, despliegue en México, controles legales dentro del producto y soporte cercano. No somos los primeros ni los únicos.

| Producto | Qué hace, según la fuente | Modelo comercial | Precio público o referencia |
| --- | --- | --- | --- |
| [Geomatrix](https://r3d.mx/2021/08/09/gobierno-de-puebla-adquirio-geomatrix-en-2019-y-2020/) (vía Neolinx de México) | Localización de celulares en tiempo real y geocercas | Licencia por periodo y paquetes de consultas | Puebla: $18.8 millones en 2019 con dos IMSI catcher; $1 millón por 960 consultas en 2020. Cotización actual no pública |
| [PenLink PLX](https://agenda.savannahga.gov/publishing/may-25-2023-city-council-regular-meeting/1394_9407.html) | Software de análisis para investigación | Compra e implementación, más mantenimiento anual | US$57,371, Savannah, Georgia, 2023, proveedor único |
| [LexisNexis AVCC y TraX](https://agendadocs.downers.us/public/docs/agendas/2024/07-09-24/RES_2024-10416.pdf) | TraX procesa, analiza y geolocaliza registros de celulares | Suscripción con contrato de 3 años | US$55,306 por 3 años, Downers Grove, Illinois, 2024 |
| [Nighthawk](https://agenda.savannahga.gov/publishing/august-13-2026-city-council-regular-meeting/1588_12570.html) (Leads Online) | Une llamadas, mensajes, redes y extracciones en un mapa y una línea de tiempo | Licencia anual por usuarios | US$60,750 al año por 30 usuarios, Savannah, 2026, pagado con fondos de subvención |
| [Cellebrite](https://www.aap.com.au/aapreleases/cision20260211ae85170) | Plataforma de investigación digital | Suscripción: 89.8 % de sus ingresos de 2025; nube, local o híbrido | Cotización no pública. Ingresos 2025: US$475.7 millones, margen bruto 84.2 % |
| Hawk Analytics (CellHawk) | No verificado en el tiempo disponible | No verificado | Cotización no pública |
| Excel y proceso manual | Hoja de cálculo y plantillas | Ya pagado | Sin costo adicional, con costo en horas y retrabajo |

**Lecciones de modelo de negocio.** Los comparables cobran por suscripción o licencia anual con mantenimiento, y varios se compraron como proveedor único. Cellebrite muestra que este mercado se sostiene con ingresos recurrentes y márgenes altos, y que ofrecer nube, local o híbrido es normal. Geomatrix muestra el riesgo contrario: cobrar por consulta y operar sin control judicial termina en escándalo.

**Ventajas que todavía debemos demostrar:**

1. Biblioteca de adaptadores para sábanas de operadores mexicanos y plantillas de ficha validadas por fiscalías.
2. Trazabilidad de dato a renglón a archivo con huella digital, pensada para cadena de custodia (validación jurídica pendiente).
3. Despliegue en México, contrato en pesos y soporte presencial en Chihuahua.
4. Controles legales dentro del producto: periodo autorizado, número de oficio y enmascarado de terceros.
5. Confianza demostrada con un piloto de criterios públicos y salida ordenada.

No son ventajas defendibles: los algoritmos de conteo o cronología, que cualquiera replica, ni "tener IA".

**Límites de esta investigación.** Fue hecha en unos 25 minutos. No revisamos contratos originales; las cifras de Geomatrix vienen de periodistas y organizaciones. El equipo reportó un informe FASP de Chihuahua con consultas Geomatrix (expediente SH/ADE/181/2024), que no pudimos abrir. Los precios de EE. UU. son de documentos de cabildos, no de listas de precios. No investigamos i2 Analyst's Notebook ni proveedores mexicanos locales.

## I. Riesgos y objeciones

Las tres amenazas mayores son comerciales, no técnicas: presupuesto y ruta de compra en un año electoral, dependencia de un solo cliente y falta de catálogo de antenas.

| Objeción | Respuesta |
| --- | --- |
| "Ya tenemos Geomatrix" | Geomatrix localiza teléfonos. Nosotros preparamos y documentamos lo que llega de los operadores. Pueden convivir; no prometemos integración sin documentación ni autorización. |
| "Eso se puede hacer en Excel" | Sí, y así se hace hoy. Excel no registra qué se excluyó, no liga cada cifra a su renglón y se rehace con cada archivo. El piloto mide si la diferencia vale su costo. |
| "¿Por qué pagar por esto?" | Por capacidad liberada de analistas, menos retrabajo y fichas defendibles. Si el piloto no lo demuestra con los criterios de la Fiscalía, no hay contrato. |
| "¿Quién mantiene el sistema?" | Nosotros, con licencia que incluye actualizaciones, adaptadores y soporte con niveles definidos. En instalación local, TI opera la infraestructura y nosotros el software. |
| "¿Qué pasa si la IA se equivoca?" | La IA no cuenta ni decide: sugiere columnas, explica errores y redacta borradores. Los conteos y cruces son reglas reproducibles, todo pasa por revisión humana y cada cifra se verifica contra el original. |
| "¿Dónde estarán los datos?" | En un entorno dedicado en nube con región en México, o en servidores de la Fiscalía. Cifrados, con bitácora y con la política de conservación y borrado que defina la Fiscalía. |
| "¿Cuánto cuesta realmente?" | Piloto $380,000, implementación $280,000 y licencia $960,000 por unidad al año, más IVA. Extras con lista de precios y sin cobro por consulta. |
| "¿Cómo viven ustedes de esto?" | De licencias recurrentes. Con unas 5 unidades se cubren sueldos y costos; antes, la operación se financia con aportación de socios, el piloto y capital semilla. |
| "¿Qué pasa cuando se acaba el apoyo inicial?" | El modelo no depende de premios ni subsidios. Si al mes 9 no hay licencia firmada, se cierra ordenadamente y se entrega todo. |
| "¿Cómo evitamos depender del proveedor?" | Exportación completa en formatos abiertos, configuraciones documentadas, salida sin costo y, opcionalmente, código en depósito con un tercero. |

| Riesgo | Mitigación |
| --- | --- |
| 2027 es año de elección de gubernatura en Chihuahua y puede frenar compras | Buscar el piloto antes de mediados de 2027 y abrir una segunda fiscalía en paralelo |
| Un solo cliente | Meta de 2 o 3 estados; regla de salida al mes 9 |
| No hay catálogo autorizado de antenas | El producto aporta valor sin mapa; el mapa se activa cuando exista catálogo |
| Los formatos varían entre operadores o solicitudes | Adaptadores configurables y cobro por adaptador nuevo |
| Asociación con vigilancia indebida | Periodo autorizado, número de oficio y bitácora obligatorios; no ofrecer rastreo |
| Fuga de datos sensibles | Controles por etapa (abajo), pruebas externas y seguro |
| Capacidad del equipo | Contratar antes de pasar de 6 unidades |

### Seguridad por etapa

Nada de esto está implementado todavía. La primera columna es la meta para la demo de hoy.

| Control | Demo de hoy (meta) | Necesario para el piloto | Necesario para producción |
| --- | --- | --- | --- |
| Autenticación | Usuario de demostración | Cuentas nominales con doble factor | Inicio de sesión institucional con doble factor |
| Permisos | Roles simulados | Analista, revisor y administrador | Por caso y por unidad |
| Bitácora de accesos y cambios | Visible en la demo | Completa e inalterable | Revisada periódicamente |
| Conservación del original | Huella digital del archivo | Almacenamiento de solo lectura | Con respaldo |
| Secretos | Variables de entorno | Gestor de secretos | Rotación periódica |
| Cifrado | HTTPS | En tránsito y en reposo | Llaves administradas, opción de llaves del cliente |
| Respaldo y recuperación | No aplica | Diario, con prueba de restauración | Objetivos de recuperación acordados |
| Conservación y eliminación | Solo datos sintéticos | Política escrita con la Fiscalía | Automatizada y auditable |
| Proveedores externos | Revisión básica | Contratos que prohíban entrenar con datos | Evaluación anual |
| Instrucciones maliciosas en archivos cargados | El contenido de celdas se trata como dato, no como orden | Filtros y pruebas | Pruebas periódicas |
| Validación de resultados | Comparación manual | Muestra independiente | Pruebas automáticas por versión |
| Incidentes y actualizaciones | — | Procedimiento, contactos y calendario | Simulacros y ventanas de mantenimiento |

### Opciones de despliegue

|  | Nube compartida del proveedor | Entorno dedicado en nube con región en México | Infraestructura del cliente |
| --- | --- | --- | --- |
| Recomendación | No, para datos de investigación | Opción por defecto | Si TI o protección de datos lo exigen |
| Costo para nosotros | Bajo | $12,000 al mes por unidad (supuesto) | Viajes y soporte en sitio |
| Precio | — | Licencia $960,000 | Licencia $840,000 más implementación $400,000 |
| Actualizaciones | Inmediatas | Programadas | Lentas, con ventana del cliente |
| Riesgo principal | Mezcla de datos entre clientes | Dependencia del proveedor de nube | La seguridad depende del cliente; no elimina riesgos ni costos |

### Mapa base con Google Maps

Google Maps sirve como mapa base en el despliegue en nube y cuesta poco, siempre que solo entregue el mapa y nunca reciba registros, números ni el catálogo de antenas. En una instalación local sin internet se usa un mapa base propio.

| Capa | Qué es | Quién la provee | Dónde vive |
| --- | --- | --- | --- |
| Mapa base | Calles, colonias y referencias visuales | Google Maps, o un mapa propio con datos de OpenStreetMap | Servidores de Google, o el servidor de la Fiscalía |
| Catálogo de antenas | Identificador y coordenadas de cada sitio | La institución o el operador, con autorización | Solo en nuestro entorno dedicado o en el servidor de la Fiscalía |
| Registros del caso | Sábanas, números y fichas | La Fiscalía | Nunca salen hacia Google |

Sin catálogo autorizado no hay ubicación, aunque haya mapa.

**Costo.** Son precios de lista de Google en dólares, tomados de su [página de precios](https://developers.google.com/maps/billing/pricing), actualizada el 21 de octubre de 2026.

| Servicio | Gratis al mes | Precio después, por cada 1,000 |
| --- | --- | --- |
| Mapa dinámico (Maps JavaScript) | 10,000 cargas | US$7.00 |
| Mosaicos 2D (Map Tiles API) | 100,000 | US$0.60 |
| Mapa estático | 10,000 | US$2.00 |
| Geocodificación | 10,000 | US$5.00 |

Supuesto de uso: 10 analistas que abren el mapa 50 veces al día durante 22 días, unas 11,000 cargas al mes por unidad. Google suma el uso de todos los proyectos de una cuenta de facturación. Con 5 unidades serían unos US$315 al mes en total, cerca de $1,200 por unidad, así que el supuesto de $1,500 por unidad del modelo lo cubre.

**Condiciones.** Requiere internet, se paga en dólares y obliga a mostrar la atribución de Google. Los términos de Google Maps Platform limitan guardar su contenido y combinarlo con mapas de otros proveedores; hay que revisar la versión vigente antes de contratar. Su [política de uso aceptable](https://cloud.google.com/maps-platform/terms/other/universal-aup) excluye usos ilegales o invasivos, y aclara que el producto no está diseñado para depender de su precisión en "operational targeting". Por eso las coordenadas de antenas vienen del catálogo autorizado y Google solo aporta contexto visual.

**Privacidad.**

- Google recibe la zona y el zoom que se consultan, la IP del equipo y la clave del proyecto.
- Nunca debe recibir números, nombres, registros, texto de la ficha ni el catálogo de antenas.
- Los puntos se dibujan en el navegador con datos de nuestro servidor, y no se usa la geocodificación de Google con domicilios del caso.
- El mapa estático no se usa con marcadores, porque las coordenadas viajarían a Google dentro de la solicitud. La imagen para la ficha se genera en nuestro servidor.
- Riesgo que queda: el código de Google corre en el navegador, y la zona consultada puede revelar dónde se investiga. Lo debe aprobar el área de protección de datos de la Fiscalía.

**Alternativa local.** Para instalación en la Fiscalía o sin internet, se usa un mapa base propio con datos de OpenStreetMap servido desde su servidor. No hay pago por carga, solo horas de configuración y la atribución que pide su licencia.

## J. Presentación para el evento

El modelo de negocio cabe en 60 segundos y en una diapositiva.

**Explicación de 60 segundos**

> Cada vez que llega una sábana telefónica, un analista la prepara a mano hasta convertirla en ficha, y con el siguiente archivo vuelve a empezar. Geomatrix ayuda a localizar teléfonos, pero no resuelve esa preparación ni deja rastro de dónde sale cada cifra. Nuestra plataforma mexicana importa la sábana, muestra errores, calcula frecuencias reproducibles y arma la ficha con cada dato ligado a su renglón original. La vendemos como un piloto pagado de 12 semanas en una unidad, con criterios que fija la propia Fiscalía. Si los cumple, pasa a una licencia anual por unidad con soporte, en nube mexicana o en sus servidores. No cobramos por consulta ni por persona. Con unas cinco unidades cubrimos sueldos y costos, y el arranque se financia con aportación de socios, el piloto y capital semilla. Nuestra ventaja no es un algoritmo: es una biblioteca de formatos mexicanos, fichas validadas y confianza demostrada.

**Cinco mensajes para una diapositiva**

1. Problema: cada sábana se prepara a mano hasta la ficha, y se repite con cada archivo.
2. Solución: ficha verificable, donde cada cifra abre su renglón original.
3. Modelo: piloto pagado de 12 semanas y luego licencia anual por unidad; nunca por consulta.
4. Números: equilibrio con unas 5 unidades; llegar ahí requiere unos $2.5 millones de financiamiento.
5. Diferencia: hecho en México, con control legal y salida sin candados.

**Cierre:** "Geomatrix dice dónde está un teléfono. Nosotros mostramos de dónde sale cada dato de la ficha."

**Tres preguntas para el mentor**

1. ¿Cuántas sábanas procesa una unidad al mes y cuántas horas toma llegar a la ficha revisada? Define el valor y el precio.
2. ¿Quién decide y con qué partida se compra software de análisis en la Fiscalía, estatal o FASP? Define la ruta de compra.
3. ¿TI exige que los datos no salgan de servidores de la Fiscalía, y existe un catálogo autorizado de antenas? Define el despliegue y el mapa.

**Nombres propuestos:** Renglón ("cada dato a su origen"), Traza MX y Sábana Clara, que el equipo ya usa.

## K. Plan inmediato

En esta estación conviene cerrar cinco decisiones; lo demás puede esperar a después del evento.

**Decidir ahora**

- [ ] Posicionamiento: plataforma mexicana de análisis trazable que complementa a Geomatrix, sin rastreo.
- [ ] Modelo: piloto pagado y licencia anual por unidad; nunca por consulta.
- [ ] Precios ilustrativos para el pitch: $380,000, $280,000 y $960,000, sin IVA.
- [ ] Hacer las tres preguntas al mentor y anotar las respuestas.
- [ ] Elegir nombre y quién presenta la parte de negocio.

**Para el bloque de desarrollo de 165 minutos.** La demo debe probar el modelo: configuración guardada de un operador, exclusión con motivo, frecuencia que abre sus renglones, ficha con limitaciones y huella digital, y bitácora. El mapa solo entra si hay un catálogo sintético de antenas.

**Después del evento**

- [ ] Validar sueldos, cargas patronales e impuestos con un contador, y cotizar nube con región en México.
- [ ] Validación jurídica: adquisiciones estatales y federales, datos personales, propiedad intelectual y cláusula de salida.
- [ ] Medir la línea base con 2 o 3 analistas.
- [ ] Constituir la empresa y definir la participación de las personas fundadoras.
- [ ] Buscar incubación e inversionistas solo después de tener la solicitud formal de piloto.

## Fuentes consultadas y supuestos

Páginas abiertas el 24 de octubre de 2026:

- R3D, [Gobierno de Puebla adquirió Geomatrix en 2019 y 2020](https://r3d.mx/2021/08/09/gobierno-de-puebla-adquirio-geomatrix-en-2019-y-2020/) (2021).
- R3D, [La FGR usó tecnología de geolocalización y solo justificó el 0.24 % de los casos](https://r3d.mx/2024/07/29/la-fgr-uso-tecnologia-de-geolocalizacion-para-vigilar-personas-y-solo-justifico-el-0-24-de-los-casos/) (2024).
- Animal Político, [Fiscalía de Gertz gasta 142.9 mdp para rastrear celulares](https://grupoanimal.mx/seguridad/fiscalia-gertz-rastrear-celulares-uso-injustificado) (9 de julio de 2024). El 0.24 % es un escenario máximo según la propia nota.
- Priego Brito & Guzmán, [resumen de la nota de Animal Político](https://priegobrito.mx/blog/2024/07/gasta-fgr-142-9-mdp-en-rastreo-de-celulares/) (2024).
- Xataka México, [resumen de la investigación de El País sobre compras de la FGR](https://www.xataka.com.mx/seguridad/fgr-compro-software-para-espionaje-telefonos-mexico-pais-geolocalizacion-analisis-datos-masivo-2019-2020) (2021).
- Secretariado Ejecutivo del SNSP, [Acuerdos del Consejo Nacional de Seguridad Pública del 11 de diciembre de 2025](https://sidof.segob.gob.mx/notas/docFuente/5777197), incluido el acuerdo 03/LII/2025 sobre el FASP 2026.
- Cellebrite, [resultados del cuarto trimestre y año 2025](https://www.aap.com.au/aapreleases/cision20260211ae85170) (11 de febrero de 2026).
- Ciudad de Savannah, [cabildo del 25 de mayo de 2023, PenLink PLX](https://agenda.savannahga.gov/publishing/may-25-2023-city-council-regular-meeting/1394_9407.html).
- Ciudad de Savannah, [cabildo del 13 de agosto de 2026, Nighthawk](https://agenda.savannahga.gov/publishing/august-13-2026-city-council-regular-meeting/1588_12570.html).
- Village of Downers Grove, [resolución RES 2024-10416, AVCC y TraX](https://agendadocs.downers.us/public/docs/agendas/2024/07-09-24/RES_2024-10416.pdf).

Supuestos: sueldos, cargas, costos de nube, precios, calendarios y retrasos de cobro son ilustrativos y deben validarse. Para comparar precios en dólares se usó un tipo de cambio ilustrativo de 18.5 pesos por dólar. Faltan datos de la Fiscalía: sábanas por mes, horas por ficha, número de analistas, partida presupuestal y restricciones de TI.
