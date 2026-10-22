# Necesidades e historias de usuario como FAIR Digital Objects (FDO)

**Para qué sirve esta carpeta.** Las historias de usuario son el puente entre lo que escuchamos y lo que el equipo va a construir. Aquí cada historia, necesidad, perfil y cita es un objeto digital independiente, con identificador propio y enlaces a los demás, para que en las siguientes fases (prototipo, pruebas, fase 2) cualquiera pueda seguir el hilo: *esta función existe porque esta necesidad la pide, y esta necesidad la sostiene esta frase de esta entrevista, en esta página*.

## Qué hay

| Tipo | Cuántos | Carpeta | Esquema |
|---|---|---|---|
| Historia de usuario | 11 | `objetos/historias/` | `tipos/HistoriaDeUsuario.schema.json` |
| Necesidad de información | 8 | `objetos/necesidades/` | `tipos/Necesidad.schema.json` |
| Perfil (persona) | 5 | `objetos/perfiles/` | `tipos/Perfil.schema.json` |
| Cita literal | 46 | `objetos/citas/` | `tipos/Cita.schema.json` |

Versiones tabulares para leer en una hoja de cálculo: `historias_de_usuario.csv` y `necesidades.csv`. El índice de todos los objetos es `registro.json`.

## Anatomía de un objeto

```json
{
  "pid": "urn:uuid:…",                       // identificador persistente (local)
  "kernel": {                                 // atributos mínimos de un FDO
    "digitalObjectType": "…/tipos/HistoriaDeUsuario.schema.json",
    "digitalObjectLocation": "…/objetos/historias/HU-01.json",
    "dateCreated": "2026-10-21", "version": "1.0.0", "license": "CC-BY-4.0",
    "creator": "Emilio Gómez Montuy",
    "checksum": {"algorithm": "sha256", "value": "…"}
  },
  "metadatos": {"titulo": "…", "descripcion": "…"},
  "datos": {"como": "…", "quiero": "…", "para": "…", "criterios_de_aceptacion": ["…"]},
  "relaciones": [
    {"tipo": "satisface",      "objetivo": "urn:uuid:… (N1)"},
    {"tipo": "expresadaPor",   "objetivo": "urn:uuid:… (P3)"},
    {"tipo": "evidenciadoPor", "objetivo": "urn:uuid:… (Q14)"},
    {"tipo": "derivaDe",       "objetivo": "E3-US02"}
  ]
}
```

El tipo de cada objeto apunta a un esquema JSON (`tipos/`), y `perfil_fdo.json` documenta los atributos y relaciones permitidos. La huella SHA-256 se calcula sobre el bloque `datos` en JSON canónico, así que cualquier cambio de contenido se detecta.

## Verificar

```bash
python fdo/validar_fdo.py
```

## Límite honesto
Los PID son URN UUID v5: estables y únicos, pero no resolubles en internet. Para un FDO formal habría que registrarlos en un servicio como Handle o DOI y publicar los tipos en un registro de tipos. Se dejó así porque el profesor indicó que no era necesario usar Zenodo.
