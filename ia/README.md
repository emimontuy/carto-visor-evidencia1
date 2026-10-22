# Uso de inteligencia artificial

La consigna permite usar IA para transcribir y asistir la codificación, con la condición de verificar las citas contra el audio y declararlo. Aquí está todo lo necesario para revisar ese uso.

- [`DECLARACION_USO_IA.md`](DECLARACION_USO_IA.md): qué hizo una persona y qué hizo la IA en cada etapa.
- [`registro_llamadas/`](registro_llamadas/): las instrucciones por fase que se dieron al LLM para analizar cada entrevista, y el registro de las sesiones con Claude que armaron este repositorio y la versión final del reporte.
- [`exportaciones_chat/`](exportaciones_chat/): espacio para las exportaciones originales de ChatGPT/Codex de la etapa de codificación (9–15 oct).

La garantía de que la IA no inventó citas no es la confianza: es `scripts/verificar_entrega.py`, que comprueba que cada cita y cada fragmento aparecen literalmente en la transcripción.
