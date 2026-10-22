# Metadatos

- `entrevistas.csv`: una fila por entrevista con perfil, tipo de actor, modalidad, fecha, páginas y conteos de análisis.
- `metadata.json`: descripción del conjunto en el esquema DataCite 4.5 (título, autoría, fechas, licencias, métodos, relación con el reporte).
- `inventario.csv`: cada archivo del repositorio con su tipo, tamaño y huella SHA-256. Se regenera con `python scripts/verificar_entrega.py --actualizar`.
