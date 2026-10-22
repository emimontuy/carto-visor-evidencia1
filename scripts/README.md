# Verificación

```bash
python scripts/verificar_entrega.py
```

En una sola ejecución comprueba:
1. que ningún archivo falte o haya cambiado (contra `MANIFEST.sha256`);
2. que los cinco paquetes son válidos (fragmentos literales, identificadores, vínculos, huellas);
3. que las citas de `sintesis/citas.csv` aparecen tal cual en la página indicada de la transcripción;
4. que los objetos de `fdo/` cumplen su esquema, conservan su huella y no tienen relaciones rotas.

Sólo usa la biblioteca estándar de Python 3.
