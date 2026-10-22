# Síntesis transversal

Aquí se juntan las cinco entrevistas. Si los paquetes de `entrevistas/` responden *qué dijo cada persona*, esta carpeta responde *qué aprendimos al leerlas juntas*.

| Archivo | Qué contiene | Dónde se usa en el reporte |
|---|---|---|
| `citas.csv` | 46 citas literales con entrevista, página y los fragmentos codificados de donde salen. El script de verificación comprueba que cada cita aparece tal cual en la transcripción. | Todas las secciones |
| `codigos_transversales.csv` | Los 10 códigos T01–T10 con definición, regla de inclusión y exclusión, y un ejemplo. | Sección 2 |
| `perfiles.json` | Los cinco perfiles (personas): qué hacen, qué les frena, qué necesitan. | Figura 2 |
| `hallazgos.csv` | Cinco hallazgos con sus citas y la implicación para el visor. | Sección 3 |
| `procesos_por_perfil.csv` | El proceso que relata cada perfil, paso por paso, con su punto de dolor y sus retornos. | Figura 4 |
| `proceso_documentado_vs_real.csv` | Cinco divergencias entre la ficha de la ADIP y lo que relatan las entrevistas. | Sección 4, Figura 3 |
| `actores.csv` | Poder, interés, posición y qué gana o cede cada actor. | Sección 5, Figura 5 |
| `visor_ideal.csv` | Lo que las personas pidieron ver en el visor (ejercicio del visor ideal). | Sección 6, Figura 6 |

**Nota sobre fragmentos.** 36 de las 46 citas coinciden con un fragmento codificado de su paquete (columna `fragmentos_del_paquete`). Las demás vienen de pasajes que el paquete no segmentó; se localizan por la página de la transcripción, y el script de verificación comprueba igual que aparecen literalmente.

**Cómo se construyó.** Leí las cinco transcripciones completas, volví a los fragmentos codificados de cada paquete y agrupé lo que se repetía entre perfiles distintos. Un hallazgo sólo entra si lo sostienen al menos dos entrevistas diferentes. Las citas se eligieron porque dicen algo con las palabras de la persona que un resumen perdería.
