# Exportaciones de conversaciones con LLM

Carpeta para los registros originales de las conversaciones con ChatGPT/Codex con las que se generaron los paquetes E1–E5 (9–15 de octubre de 2026) y con Claude.

## Cómo agregarlas
- **ChatGPT:** Configuración → Controles de datos → Exportar datos. Llega un correo con un ZIP; copiar aquí `conversations.json` (o solo las conversaciones del proyecto Carto-Visor).
- **Codex:** guardar los registros de sesión (`~/.codex/sessions/`) de esas fechas.
- **Claude:** Configuración → Privacidad → Exportar datos.

Antes de subirlas, revisar que no contengan datos personales ajenos al proyecto. Después de agregarlas, regenerar `MANIFEST.sha256` con `python scripts/verificar_entrega.py --actualizar`.
