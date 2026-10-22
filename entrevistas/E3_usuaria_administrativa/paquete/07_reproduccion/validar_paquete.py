from pathlib import Path
import csv, hashlib, json, sys, unicodedata
base=Path(__file__).resolve().parents[1]
read=lambda p:json.loads((base/p).read_text(encoding='utf-8'))
normal=lambda s:' '.join(unicodedata.normalize('NFC',s).split())
codes=read('02_codificacion/libro_de_codigos.json')['codigos']
segments=read('02_codificacion/corpus_codificado.json')['segmentos']
analysis=read('03_analisis/hallazgos_y_mapas.json')
stories=read('04_desarrollo/historias_de_usuario.json')['historias']
blueprint=read('04_desarrollo/blueprint.json')
contracts=read('04_desarrollo/contratos_de_datos.json')['contratos']
pages=(base/'01_fuente/transcripcion_por_paginas.txt').read_text().split('\f')
code_ids={x['id'] for x in codes};segment_ids={x['id'] for x in segments}
finding_ids={x['id'] for x in analysis['hallazgos']}
story_ids={x['id'] for x in stories};requirement_ids={x['id'] for x in blueprint['requisitos']}
for values,key in [(codes,'id'),(segments,'id'),(analysis['hallazgos'],'id'),(stories,'id'),(blueprint['requisitos'],'id')]:
 assert len(values)==len({x[key] for x in values}), 'Identificador repetido'
for x in segments:
 assert normal(x['fragmento_literal']) in normal(pages[x['pagina']-1]), x['id']
 assert set(x['codigos'])<=code_ids, x['id']
for x in codes: assert x['ejemplo_segmento'] in segment_ids, x['id']
for x in analysis['hallazgos']:
 assert set(x['segmentos'])<=segment_ids and set(x['codigos'])<=code_ids, x['id']
for name in ['actores','proceso','empatia','afinidad']:
 for x in analysis[name]: assert set(x['segmentos'])<=segment_ids, name
for x in stories:
 assert set(x['segmentos'])<=segment_ids and set(x['hallazgos'])<=finding_ids and set(x['requisitos'])<=requirement_ids, x['id']
for x in blueprint['requisitos']:
 assert set(x['historias'])<=story_ids, x['id']
 for story_id in x['historias']:
  assert x['id'] in next(s for s in stories if s['id']==story_id)['requisitos'], x['id']
for x in blueprint['decisiones']:
 assert set(x['segmentos'])<=segment_ids and set(x['requisitos'])<=requirement_ids, x['id']
for x in contracts: assert set(x['segmentos'])<=segment_ids, x['tipo']
objects=read('05_metadatos/registro_de_objetos.json')['objetos']
object_ids={x['id'] for x in objects}
for x in objects:
 assert set(x['deriva_de'])<=object_ids, x['nombre']
 assert hashlib.sha256((base/x['ruta']).read_bytes()).hexdigest()==x['sha256'], x['nombre']
 assert x['pid'] is None, 'PID no asignado en esta entrega'
for line in (base/'checksums.sha256').read_text().splitlines():
 expected,relative=line.split('  ',1)
 assert hashlib.sha256((base/relative).read_bytes()).hexdigest()==expected, relative
from local_schema import validate_local_schema
for x in objects:
 if x['esquema_local']:
  validate_local_schema(read(x['ruta']),read(x['esquema_local']))
print('Correcto: citas literales, identificadores, vínculos, integridad y campos de los esquemas locales.')
print(f"E3: {len(pages)} páginas fuente, {len(segments)} fragmentos, {len(codes)} códigos, {len(analysis['hallazgos'])} hallazgos y {len(stories)} historias.")
