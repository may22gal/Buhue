<p align="center">
  <img src="assets/logo-buhue.png" alt="Logo de Buhue: búho sobre un mapa con antena, ubicación, teléfono y contactos" width="320">
</p>

# Buhue

**BUHUÉ** significa **Base Unificada de Homologación y Ubicación de Estaciones**.

Plataforma mexicana para el análisis de registros telefónicos (sábanas) en instituciones de justicia.

Buhue importa las sábanas que entregan los operadores, las valida y normaliza, ordena los eventos por cronología, calcula frecuencias de números y antenas, ubica las antenas cuando existe un catálogo autorizado y arma la ficha institucional. Cada cifra de la ficha queda ligada al renglón original del que salió, para que el análisis sea verificable.

## Contexto

El proyecto nace en el **Rally de Innovación por la Justicia** (24 de octubre de 2026, CIITA-IPN, Ciudad Juárez), dentro del reto de mapeo de antenas y procesamiento geográfico de sábanas sin coordenadas.

Herramientas como Geomatrix se enfocan en localizar teléfonos. Buhue se posiciona como complemento: resuelve la preparación manual y repetitiva de las sábanas y produce fichas trazables, con la visión de convertirse en una solución local y configurable para fiscalías de México.

## Principios

- Supervisión humana: la plataforma prepara y ordena información; no determina culpabilidad, credibilidad ni decisiones judiciales.
- Trazabilidad: todo dato mostrado se puede rastrear a su fuente.
- Privacidad: el prototipo trabaja solo con datos sintéticos. Los datos institucionales requieren autorización escrita y un entorno aprobado.
- Configuración en lugar de reprogramación: formatos de operador, plantillas de ficha, catálogos y roles.

## Instrucciones para las IA del equipo

**Queremos que BUHUÉ sea lo más innovador posible, con utilidad real, seguridad y una demo que funcione.** Antes de proponer o implementar, lee [AGENTS.md](AGENTS.md). Ahí están el criterio de innovación, las ideas diferenciadoras, la priorización MoSCoW y los límites del MVP. Para Claude, consulta también [CLAUDE.md](CLAUDE.md).

## Documentación

- [Modelo de negocio](docs/modelo-de-negocio.md): propuesta de valor, modelo comercial, finanzas, financiamiento, piloto, riesgos y plan inmediato.
- [Costeo detallado](docs/modelo-de-negocio.md#l-anexo-costeo-detallado) (sección L del modelo): desarrollo por etapa, licencia anual por componente (sistema, datos, respaldo, mantenimiento, seguridad, actualizaciones, soporte y capacitación), personas, nube, equipo, piloto por semana, primer año mes por mes y costo por sábana.

## Precios propuestos

Ilustrativos y con IVA, por validar con la Fiscalía:

| Concepto | Precio |
| --- | --- |
| Piloto de 8 semanas con las 6 personas analistas | $116,000, una vez |
| Implementación y capacitación | $174,000, una vez |
| Licencia anual, con una versión nueva cada 6 meses | $696,000 al año, unos $58,000 al mes |

Nunca se cobra por consulta, por persona investigada ni por resultado.

## Estado

Prototipo de hackatón. Las cifras del modelo de negocio son ilustrativas y están por validar.
