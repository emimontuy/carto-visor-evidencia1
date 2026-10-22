# Blueprint de desarrollo derivado de E1

Prototipo interno de biblioteca y visor de sectores y cuadrantes de SSC, con referencia identificable, consulta sencilla y descarga controlada.

Estado: propuesta para validar. No implementado ni probado.

## Recorrido
Acceso autorizado → catálogo → activar capa en mapa → consultar ficha → descargar la misma versión.

## Requisitos
### E1-R01 Catálogo
Catálogo de las dos capas iniciales con fuente, versión y estado de disponibilidad.
Historias: E1-US01.
Prueba propuesta: Dos registros vinculados a archivos recibidos y validados; ninguna capa anunciada sin entrega.
Tipos: CapaCatalogo.

### E1-R02 Mapa
Controles visibles de encendido y apagado, leyenda y acceso a ficha y descarga.
Historias: E1-US02.
Prueba propuesta: Prueba de tareas sin asistencia; registrar tiempo, finalización, errores y ayudas solicitadas.
Tipos: CapaCatalogo, ResultadoPruebaUsuario.

### E1-R03 Descarga
Archivo de la versión consultada y metadatos asociados; conservar el formato original recibido.
Historias: E1-US03.
Prueba propuesta: Identificador de versión y huella del archivo descargado coinciden con catálogo y manifiesto.
Tipos: VersionCapa.

### E1-R04 Ficha de metadatos
Fuente, fecha del productor, recepción, publicación, versión, CRS, descripción y limitaciones.
Historias: E1-US01, E1-US04.
Prueba propuesta: Una fecha ausente se informa como No proporcionada y nunca se reemplaza por la del visor.
Tipos: VersionCapa.

### E1-R05 Autorización
Control de lectura y descarga en servicios y archivos; usuarios de consulta sin escritura.
Historias: E1-US03, E1-US05.
Prueba propuesta: Acceso anónimo y escritura con permiso de consulta rechazados incluso por ruta directa.
Tipos: PermisoAcceso.

### E1-R06 Identidad de polígonos
Correspondencia explícita con clave y nombre oficiales, conservados en consulta y descarga.
Historias: E1-US01, E1-US03, E1-US06.
Prueba propuesta: Comparación con entrega original; reporte de claves vacías, repetidas o modificadas.
Tipos: EntidadCartografica.

### E1-R07 Ingreso de archivos
Revisión de fuente, integridad, esquema y geometrías; registro de incidencias antes de publicar.
Historias: E1-US06.
Prueba propuesta: Un archivo con fallo bloqueante permanece en revisión y no sustituye una versión validada.
Tipos: VersionCapa, InformeValidacion.

### E1-R08 Operación y transferencia
Ejecución local, inventario de dependencias e instrucciones para continuar sin suscripciones esenciales.
Historias: E1-US07, E1-US08.
Prueba propuesta: Reproducción por otra persona; catálogo, mapa y descarga funcionan desde la entrega documentada.
Tipos: DecisionArquitectura.

### E1-R09 Gestión de fases
Bitácora de decisiones, contrato ampliable y lista de cambios sujetos a nueva validación.
Historias: E1-US07, E1-US09.
Prueba propuesta: Datos de Fiscalía, apertura pública y avisos automáticos permanecen fuera del alcance inicial.
Tipos: DecisionArquitectura, AvisoCambio.

## Contratos de datos
### CapaCatalogo
Identificar cada capa disponible sin depender de su nombre de archivo.
id_capa string; titulo string; descripcion string; productor string; alcance_territorial string; version_activa string o null; estado enum recibido/revision/disponible/no_recibido
Al inicio solo sectores y cuadrantes de SSC. El catálogo apunta a una versión, no reemplaza el identificador de cada polígono.

### VersionCapa
Vincular archivo, procedencia, vigencia y representación para mapa.
id_version string; id_capa string; archivo_original string; sha256 string; formato_original string; crs_original string o null; fecha_productor date o null; fecha_recepcion date; fecha_publicacion date o null; representacion_mapa string o null; transformaciones array; limitaciones string
Fecha del productor y fecha del visor son diferentes. Conservar original; toda representación derivada apunta a él. No asumir que el archivo será SHP o GeoJSON.

### EntidadCartografica
Conservar la identidad oficial de cada sector o cuadrante.
id_capa string; id_version string; clave_oficial string; nombre_oficial string; geometria Polygon o MultiPolygon; atributos_originales object
Los nombres reales de columnas se confirman al recibir la entrega. Las claves se preservan como texto para no perder ceros. No inventar relación cuadrante-sector si no viene documentada.

### PermisoAcceso
Separar consulta de mantenimiento y reservar el acceso a personas autorizadas.
id_principal string; ambito_dependencia string o null; acciones array leer/descargar/mantener; recursos array; estado activo/revocado; mecanismo_identidad string pendiente de definir
La persona de consulta tiene leer y descargar, no mantener. Autenticación institucional, altas y granularidad de roles se validan antes de un despliegue.

### InformeValidacion
Registrar qué se revisó y por qué una versión está disponible o detenida.
id_informe string; id_version string; fecha datetime; comprobaciones array; incidencias array; resultado apto/revision/rechazado; revisor string o null
Comprobar integridad, esquema, claves, geometrías, CRS y campos sensibles. Reportar fallas, no corregir silenciosamente. La compatibilidad declarada por [Directora ADIP] no sustituye esta prueba.

### DecisionArquitectura
Conservar acuerdos y pendientes para otro equipo o fase.
id_decision string; tema string; alternativa_elegida string o null; razon string; segmentos array; estatus propuesta/acordada/pendiente; responsable_por_confirmar string o null; version string
Distinguir decisión de este análisis de un acuerdo aprobado por ADIP. Mantener documentación de ejecución y alcance junto a la entrega.

### ResultadoPruebaUsuario
Comprobar tareas del perfil provisional sin inventar resultados.
id_prueba string; perfil string; tarea string; finalizada boolean o null; tiempo_segundos number o null; errores array; ayudas_solicitadas number o null; observaciones string; fecha date o null
No hay resultados todavía. Umbrales de éxito se acuerdan antes de la prueba y se documentan también los casos que fallan.

### AvisoCambio
Documentar una posible solicitud de nueva versión en una fase posterior.
id_aviso string; id_capa string; productor string; fecha_version_declarada date o null; canal string; estado recibido/solicitado/validado/publicado/rechazado; id_version_resultante string o null
Un aviso no actualiza ni autoriza por sí solo. El proceso completo y sus responsables están pendientes de validación; no es función obligatoria del MVP.

## Orden de construcción
1. Cerrar arquitectura y decisiones de acceso, fuente y metadatos. Dependencias: E1-Q02, E1-Q03, E1-Q04.
2. Recibir, conservar y revisar las dos capas. Dependencias: Entrega de SSC por [Directora ADIP] y [Enlace ADIP].
3. Construir catálogo, mapa, ficha y descarga con control de acceso. Dependencias: Pasos 1 y 2.
4. Probar las tareas con usuarios y documentar correcciones. Dependencias: E1-Q01, E1-Q05, Prototipo local.
5. Entregar instrucciones y preparar integración institucional si se acuerda. Dependencias: E1-Q06, Revisión de ADIP.

## Preguntas por validar
E1-Q01: ¿Qué tarea concreta hace una persona de otra dependencia con sectores o cuadrantes y qué problema enfrenta con la referencia actual?
E1-Q02: ¿Qué archivos, campos, CRS, fechas y conteos trae la entrega de SSC?
E1-Q03: ¿Quién da de alta, autoriza y revoca accesos? ¿Las cuentas son personales o por dependencia?
E1-Q04: ¿Quién confirma vigencia, autoriza publicación y recibe incidencias de datos?
E1-Q05: ¿Qué tareas y umbrales demostrarían uso sin explicación externa?
E1-Q06: ¿Qué condiciones técnicas y de acceso exige el servidor de ADIP?
