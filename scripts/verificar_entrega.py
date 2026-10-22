#!/usr/bin/env python3
"""Verifica la entrega FAIR de la Evidencia 1 (Carto-Visor).

Uso (desde la raíz del repositorio):
    python scripts/verificar_entrega.py              # verifica huellas y paquetes
    python scripts/verificar_entrega.py --actualizar # regenera MANIFEST.sha256 e inventario

Solo usa la biblioteca estándar de Python 3.8+.
"""
import csv
import hashlib
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MANIFEST = RAIZ / "MANIFEST.sha256"
INVENTARIO = RAIZ / "metadatos" / "inventario.csv"
EXCLUIR = {"MANIFEST.sha256", "metadatos/inventario.csv"}

TIPOS = {
    ".pdf": "fuente_pdf", ".txt": "texto", ".csv": "tabla", ".json": "datos_json",
    ".md": "documentacion", ".docx": "documento", ".py": "codigo", ".png": "figura",
    ".sha256": "huellas", ".cff": "citacion", ".jsonl": "registro_llm",
}


def archivos():
    for p in sorted(RAIZ.rglob("*")):
        rel = p.relative_to(RAIZ).as_posix()
        if p.is_file() and not rel.startswith(".git/") and "__pycache__" not in rel and rel not in EXCLUIR:
            yield p, rel


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(65536), b""):
            h.update(b)
    return h.hexdigest()


def entrevista(rel):
    partes = rel.split("/")
    return partes[1].split("_")[0] if partes[0] == "entrevistas" and len(partes) > 1 else "general"


def actualizar():
    filas = [(rel, sha256(p), p.stat().st_size) for p, rel in archivos()]
    MANIFEST.write_text("".join(f"{h}  {rel}\n" for rel, h, _ in filas), encoding="utf-8")
    with open(INVENTARIO, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ruta", "entrevista", "tipo", "bytes", "sha256"])
        for rel, h, n in filas:
            w.writerow([rel, entrevista(rel), TIPOS.get(Path(rel).suffix.lower(), "otro"), n, h])
    print(f"MANIFEST.sha256 e inventario.csv regenerados: {len(filas)} archivos.")


def verificar():
    ok = True
    esperados = {}
    for linea in MANIFEST.read_text(encoding="utf-8").splitlines():
        h, rel = linea.split("  ", 1)
        esperados[rel] = h
    presentes = {rel: p for p, rel in archivos()}
    for rel, h in esperados.items():
        if rel not in presentes:
            print(f"FALTA   {rel}"); ok = False
        elif sha256(presentes[rel]) != h:
            print(f"ALTERADO {rel}"); ok = False
    for rel in presentes.keys() - esperados.keys():
        print(f"SIN REGISTRAR {rel}"); ok = False
    print(f"Huellas: {len(esperados)} archivos revisados.")

    for validador in sorted(RAIZ.glob("entrevistas/*/paquete/0*_repro*/validar_paquete.py")):
        paquete = validador.parent.parent
        r = subprocess.run([sys.executable, str(validador.relative_to(paquete))], cwd=paquete,
                           capture_output=True, text=True)
        salida = (r.stdout + r.stderr).strip().splitlines()
        print(f"[{paquete.parent.name}] {'OK' if r.returncode == 0 else 'ERROR'}: {salida[-1] if salida else ''}")
        ok &= r.returncode == 0
    # citas de la síntesis
    import unicodedata
    norm = lambda t: " ".join(unicodedata.normalize("NFC", t).split())
    malas = 0
    with open(RAIZ / "sintesis" / "citas.csv", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    for fila in filas:
        txt = (RAIZ / fila["transcripcion"].replace("_anonimizada.pdf", "").rsplit("/", 1)[0]).glob("*.txt")
        pagina = next(txt).read_text(encoding="utf-8").split("\f")[int(fila["pagina"]) - 1]
        if norm(fila["cita_literal"]) not in norm(pagina):
            print(f"CITA NO ENCONTRADA {fila['id']}"); malas += 1
    print(f"[citas] {'OK' if not malas else 'ERROR'}: {len(filas) - malas} de {len(filas)} citas aparecen literalmente en su página.")
    ok &= malas == 0
    r = subprocess.run([sys.executable, str(RAIZ / "fdo" / "validar_fdo.py")], capture_output=True, text=True)
    print(f"[fdo] {'OK' if r.returncode == 0 else 'ERROR'}: {(r.stdout + r.stderr).strip().splitlines()[-1]}")
    ok &= r.returncode == 0
    print("RESULTADO:", "entrega íntegra, paquetes, citas y FDO válidos" if ok else "hay problemas")
    return ok


if __name__ == "__main__":
    if "--actualizar" in sys.argv:
        actualizar()
    else:
        sys.exit(0 if verificar() else 1)
