# Prompts de reproducción por fases

Instrucciones usadas para el análisis asistido por LLM de cada entrevista. Se aplicaron por separado a cada transcripción (E1–E5), sin mezclar entrevistas. Fuente: `entrevistas/E1_ADIP/paquete/05_reproducibilidad/metodo_y_guion.md`; E2–E5 siguieron las mismas fases (ver `05_metadatos/metodo_y_alcance.json` de cada paquete).

Estas instrucciones permiten reproducir las fases; no son una transcripción de llamadas internas del modelo ni un registro de una ejecución de software externo.

**Fase 1.** Usa exclusivamente E1. Enumera participantes y distingue hechos narrados, expectativas, incertidumbres y fases futuras. Conserva las negativas. No uses otras entrevistas para llenar vacíos.

**Fase 2.** Propón un libro de códigos inductivo. Para cada código define significado, inclusión, exclusión y ejemplo con página. No confundas otros tableros con requisitos del Carto-Visor.

**Fase 3.** Segmenta por unidad de sentido y asigna códigos. Devuelve ID, página, fragmento literal, atribución de hablante, códigos, estatus y memo. La atribución inferida debe indicarse. No inventes marcas de tiempo.

**Fase 4.** Obtén actores, procesos, necesidades y hallazgos a partir de esos IDs. Declara qué no se puede concluir. No cuentes frecuencias de fragmentos como personas independientes ni uses reiteración como prioridad automática.

**Fase 5.** Redacta historias con rol, acción y beneficio, evidencia y criterios verificables. Distingue perfil provisional, requisito expresado y decisión técnica derivada. No añadas analítica o datos de Fiscalía a esta entrega.

**Fase 6.** Produce un blueprint con módulos, contratos, reglas de datos, permisos, prioridades, dependencias y preguntas por validar. Cada requisito debe remitir a historias y segmentos.

**Fase 7.** Empaqueta codebook, corpus, hallazgos, historias y blueprint como objetos tipados con metadatos, procedencia, versión e integridad. No inventes DOI ni afirme registro FDO o publicación en Zenodo. Registra lo pendiente.


## Adaptación para E2–E5

En las fases 1–3, sustituir E1 por la entrevista correspondiente. Regla de exclusión común: las preguntas de Emilio son contexto y no se atribuyen a la persona entrevistada como experiencia o acuerdo. En E5 se añadió la fase de diagramas de causalidad con bucles (Clase 12), marcados como hipótesis.
