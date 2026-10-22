# Método y guion de reproducción

## Base de las clases
La clase 11 aporta la unidad entrevista como documento, fragmento como unidad de sentido, código con reglas y memo analítico. La clase 09 conecta actores, procesos y necesidades de información con historias de usuario accionables, archivos intermedios y trazabilidad. La clase 13 pide explicitar causas y efectos y profundizar la problematización. Se aplica codificación temática inicial con orientación inductiva; no se afirma haber completado teoría fundamentada ni alcanzado saturación.

## Fases realizadas
1. Conservar el PDF original y extraer su texto por página sin corregir silenciosamente errores de transcripción. Leer las 16 páginas. Fecha exacta de la sesión y tiempos de audio no constan de forma verificable; el nombre del archivo no se usa como prueba suficiente de fecha.
2. Separar contexto, situación actual, requisitos, propuestas condicionales, incertidumbre y procesos futuros. Las preguntas de los estudiantes no se tratan como evidencia de una necesidad institucional.
3. Definir el libro de códigos con inclusión, exclusión y fragmento de ejemplo. Se permite más de un código por fragmento cuando contiene ideas diferentes.
4. Asignar códigos a 48 fragmentos sustantivos y conservar los matices negativos y condicionales. Las conversaciones logísticas de apertura no se codifican como necesidades; quedan en la fuente completa.
5. Agrupar códigos por afinidad y producir siete hallazgos; reconstruir actores, proceso y necesidades sin atribuir emociones no expresadas.
6. Derivar nueve historias: seis de producto, dos de soporte al desarrollo y una ampliación condicional. Establecer criterios de aceptación propuestos, requisitos, tipos de datos y orden de construcción.
7. Preparar objetos con identificador interno estable, esquema, versión, metadatos, procedencia y huellas de integridad. Dejar explícitamente pendiente el registro de un PID resoluble y de los tipos y perfiles FDO.
8. Verificar coincidencia de fragmentos, referencias y archivos. Dejar una hoja para revisión humana. La revisión estructural no sustituye el juicio cualitativo de una segunda persona.

## Guion para repetir el análisis con un LLM
Estas instrucciones permiten reproducir las fases; no son una transcripción de llamadas internas del modelo ni un registro de una ejecución de software externo.

Fase 1. Usa exclusivamente E1. Enumera participantes y distingue hechos narrados, expectativas, incertidumbres y fases futuras. Conserva las negativas. No uses otras entrevistas para llenar vacíos.

Fase 2. Propón un libro de códigos inductivo. Para cada código define significado, inclusión, exclusión y ejemplo con página. No confundas otros tableros con requisitos del Carto-Visor.

Fase 3. Segmenta por unidad de sentido y asigna códigos. Devuelve ID, página, fragmento literal, atribución de hablante, códigos, estatus y memo. La atribución inferida debe indicarse. No inventes marcas de tiempo.

Fase 4. Obtén actores, procesos, necesidades y hallazgos a partir de esos IDs. Declara qué no se puede concluir. No cuentes frecuencias de fragmentos como personas independientes ni uses reiteración como prioridad automática.

Fase 5. Redacta historias con rol, acción y beneficio, evidencia y criterios verificables. Distingue perfil provisional, requisito expresado y decisión técnica derivada. No añadas analítica o datos de Fiscalía a esta entrega.

Fase 6. Produce un blueprint con módulos, contratos, reglas de datos, permisos, prioridades, dependencias y preguntas por validar. Cada requisito debe remitir a historias y segmentos.

Fase 7. Empaqueta codebook, corpus, hallazgos, historias y blueprint como objetos tipados con metadatos, procedencia, versión e integridad. No inventes DOI ni afirme registro FDO o publicación en Zenodo. Registra lo pendiente.

## Revisión humana prevista
Una segunda persona revisa los 48 fragmentos y especialmente negativos, propuestas y atribuciones ambiguas. Registra desacuerdos en registro_revision.csv y, si cambia una regla, recodifica los fragmentos afectados y genera una nueva versión. Una medida de concordancia solo se calcula después de dos codificaciones independientes del mismo conjunto y reglas explícitas; no existe aún una medición.
