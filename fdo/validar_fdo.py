#!/usr/bin/env python3
"""Valida los registros FDO: esquema del sobre y del tipo, huella del bloque 'datos' y que toda relación interna apunte a un PID existente.
Uso: python fdo/validar_fdo.py   (desde la raíz del repositorio; sólo biblioteca estándar)"""
import hashlib, json, sys
from pathlib import Path
R = Path(__file__).resolve().parent
reg = json.loads((R / "registro.json").read_text(encoding="utf-8"))["objetos"]
pids = {o["pid"] for o in reg}
def chk(data, schema, ctx):
    for k in schema.get("required", []):
        assert k in data, f"{ctx}: falta {k}"
    if schema.get("additionalProperties") is False:
        extra = set(data) - set(schema.get("properties", {}))
        assert not extra, f"{ctx}: campos no definidos {extra}"
    for k, p in schema.get("properties", {}).items():
        if k not in data: continue
        v = data[k]
        if p.get("type") == "string": assert isinstance(v, str), f"{ctx}.{k}"
        if p.get("type") == "integer": assert isinstance(v, int), f"{ctx}.{k}"
        if p.get("type") == "array": assert isinstance(v, list) and len(v) >= p.get("minItems", 0), f"{ctx}.{k}"
        if "enum" in p: assert v in p["enum"], f"{ctx}.{k}"
sobre = json.loads((R / "tipos/FDO.schema.json").read_text(encoding="utf-8"))
n = 0
for o in reg:
    d = json.loads((R.parent / o["ruta"]).read_text(encoding="utf-8"))
    chk(d, sobre, o["id"])
    assert d["pid"] == o["pid"], o["id"]
    tipo = d["kernel"]["digitalObjectType"].rsplit("/", 1)[1]
    chk(d["datos"], json.loads((R / "tipos" / tipo).read_text(encoding="utf-8")), o["id"])
    canon = json.dumps(d["datos"], ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(canon).hexdigest() == d["kernel"]["checksum"]["value"], f"{o['id']}: huella"
    for r in d["relaciones"]:
        if r["objetivo"].startswith("urn:uuid:"):
            assert r["objetivo"] in pids, f"{o['id']}: relación rota {r}"
    n += 1
print(f"FDO correcto: {n} objetos ({', '.join(sorted({x['tipo'] for x in reg}))}); esquemas, huellas y relaciones verificados.")
