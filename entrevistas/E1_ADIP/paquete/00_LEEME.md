# Primera entrevista del proyecto Carto-Visor

Autor del trabajo: Emilio Gómez Montuy. Entrevista: E1, sesión grupal de ADIP. Preparación: 2026-10-09. Versión: 1.0.0.

Este paquete desarrolla solo la primera entrevista. Contiene el proceso intermedio que solicitó el profesor: transcripción → fragmentos → códigos → hallazgos → historias de usuario → blueprint. La conclusión es construir primero una biblioteca interna identificable de sectores y cuadrantes, con consulta sencilla, metadatos y descarga controlada. La demanda de otras dependencias permanece por validar.

## Orden de lectura y entrega
1. Leer el documento E1_ADIP_Analisis_por_fases.docx entregado junto con este ZIP.
2. Revisar el libro de códigos y corpus de 02_codificacion. JSON sirve para procesamiento y CSV para revisión en una hoja de cálculo.
3. Revisar hallazgos, actores, procesos y límites del mapa de empatía en 03_analisis.
4. Revisar historias, requisitos, contratos y orden de construcción en 04_desarrollo. Son propuestas para validar, no funciones ya implementadas.
5. Completar la revisión humana en 05_reproducibilidad. El guion permite repetir el análisis por fases con otro codificador o LLM.
6. Mantener metadatos y tipos de 06_fdo junto a cada objeto. No hay publicación ni DOI asignado.
7. Usar 07_reporte/sintesis_para_reporte.md para reemplazar el análisis general de E1 en el reporte principal; los demás archivos son material de apoyo, no páginas del cuerpo del reporte.

## Inventario del análisis
19 códigos, 48 fragmentos, 7 hallazgos, 9 historias, 9 requisitos y 8 contratos de datos. Las historias 01–06 corresponden al producto; 07–08 al soporte del desarrollo; 09 es una ampliación condicional. P0 es una prioridad propuesta para la entrega inicial, no un acuerdo ya validado con ADIP.

## Convenciones y límites
E1-S identifica fragmento; C identifica código; E1-H hallazgo; E1-US historia; E1-R requisito; E1-D decisión; E1-Q pregunta pendiente. Las páginas se refieren al PDF original. Los fragmentos mantienen el texto, con espacios normalizados. Las atribuciones de hablantes se infieren por el diálogo y no son una diarización de audio verificada. La fecha exacta de sesión no se infiere del nombre del archivo. Se conservó la fuente completa de 16 páginas y no se mezclaron las demás entrevistas.

Las referencias de segmento y página son trazabilidad del material de apoyo. La síntesis para el reporte no incorpora citas parentéticas ni una lista bibliográfica. No hay resultados de usabilidad, auditoría de las capas, concordancia entre codificadores ni ahorros medidos. No se inventaron emociones de usuarios externos.

## Preparación como objetos digitales FAIR
Cada objeto tiene identificador interno estable URN UUID, tipo semántico local, esquema cuando corresponde, versión, metadatos, procedencia, relaciones de derivación, acceso y SHA-256. Los identificadores internos permiten enlazar el paquete, pero no sustituyen un PID con resolución y conservación institucional. Los campos de DOI o PID resoluble permanecen vacíos. Cada objeto puede prepararse como registro separado y relacionarse con los otros si más adelante se pide un depósito; un único DOI del ZIP no identifica separadamente cada objeto.

El profesor indicó que no hace falta crear Zenodo. Para completar un registro FDO formal aún haría falta resolver los PID y registrar o adoptar los tipos y perfiles pertinentes. También deben confirmarse los derechos antes de hacer pública la transcripción. No se ha creado una cuenta ni un depósito. La licencia está pendiente en vez de atribuir una autorización de reutilización no otorgada.

La distinción entre PID, tipo, perfil y metadatos se revisó con la documentación primaria del FDO Forum y GO FAIR. Zenodo indica que el DOI se registra al publicar. Estas fuentes metodológicas están aquí, separadas del reporte:
- FDO Forum: https://fairdo.org/about/what_is_an_fdo/
- GO FAIR F1: https://www.gofair.foundation/f1
- Zenodo: https://help.zenodo.org/docs/deposit/create-new-upload/

## Verificación
MANIFEST.sha256 enumera la integridad de los archivos. Puede ejecutarse `python 05_reproducibilidad/validar_paquete.py` desde esta carpeta. El script valida huellas, coincidencia literal de fragmentos, IDs y relaciones. Los resultados de esta comprobación son estructurales y no sustituyen revisión humana del análisis.
