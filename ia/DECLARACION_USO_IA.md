# Declaración de uso de inteligencia artificial

**Autor de la evidencia:** Emilio Gómez Montuy (A01658834)
**Consigna:** "Puedes usar inteligencia artificial para transcribir y para asistir la codificación; toda cita que uses en el reporte debe estar verificada contra el audio. Declara al final del documento la herramienta y el uso que le diste."

## Qué hizo una persona y qué hizo la IA

| Etapa | Persona (Emilio) | Herramienta de IA | Uso |
|---|---|---|---|
| 1. Entrevistas | Diseñó el guion, condujo las cinco entrevistas en persona/sesión y grabó el audio. | — | Ninguno. |
| 2. Transcripción | Revisó y corrigió cada transcripción contra el audio. | Transcripción automática con IA | Primera versión del texto a partir del audio. |
| 3. Codificación por entrevista (paquetes E1–E5) | Definió criterios, revisó fragmentos, códigos y hallazgos. | ChatGPT / Codex (OpenAI) | Segmentación en fragmentos, propuesta de libro de códigos, asignación de códigos, hallazgos, historias de usuario, blueprint y empaquetado FDO con validadores. |
| 4. Síntesis transversal y reporte | Decidió la estructura, el juicio crítico y la postura final. | ChatGPT / Codex y Claude (Anthropic) | Integración de los cinco paquetes, esquema T01–T10, redacción y revisión de estilo. |
| 5. Repositorio FAIR | Revisó y publicó. | Claude (Anthropic, sesión del 2026-10-20) | Armado del repositorio, inventario, huellas SHA-256, metadatos, script de verificación y ajuste del reporte. |
| 6. Revisión tras retroalimentación (21 oct) | Decidió qué atender, eligió el enfoque narrativo y revisó perfiles, procesos e historias. | Claude (Anthropic) | Anonimización con script, verificación automática de 46 citas, figuras generadas desde datos, consolidación de historias, objetos FDO y reescritura del reporte en Google Docs. |

## Verificación
- Las citas y fragmentos literales del reporte provienen de transcripciones corregidas por el autor contra el audio.
- Cada paquete incluye un validador (`entrevistas/*/paquete/0*_repro*/validar_paquete.py`) que comprueba que cada fragmento codificado aparece literalmente en la transcripción, junto con identificadores, vínculos y huellas.
- `scripts/verificar_entrega.py` ejecuta todos los validadores y comprueba `MANIFEST.sha256`.
- La revisión es estructural: no sustituye una segunda codificación independiente (no se calculó concordancia entre codificadores).

## Registro de llamadas a LLM
Ver `ia/registro_llamadas/`. Incluye:
- `sesion_claude_2026-10-20_21.jsonl`: registro de la sesión con Claude que armó este repositorio y ajustó el reporte (instrucción del usuario, archivos leídos, acciones y resultados).
- `prompts_reproduccion_por_fases.md`: las instrucciones por fase para repetir el análisis con cualquier LLM.
- `ia/exportaciones_chat/`: carpeta para las exportaciones originales de ChatGPT/Codex con las que se generaron los paquetes E1–E5.
